#!/usr/bin/env python3
"""
Zabbix MCP Server - Unified API interface using python-zabbix-utils

This server provides complete access to ALL Zabbix API functionality through
a single unified tool, enabling AI assistants to interact with Zabbix monitoring
systems dynamically.

Author: Zabbix MCP Server Contributors
License: GPL-3.0-or-later
"""

import logging
from typing import Any

from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

from .client import get_zabbix_client
from .config import EnvVars, get_env, parse_bool_env, parse_int_env
from .local_docs import LocalDocsError, get_method_docs, list_methods
from .utils import (
    check_method_allowed,
    format_response,
    is_read_only,
    is_read_operation,
)

logger = logging.getLogger(__name__)

_ZABBIX_URL = get_env(EnvVars.ZABBIX_URL, "not configured")


def _with_server_url(fn):
    """Prepend Zabbix server URL to tool docstring."""
    if fn.__doc__:
        fn.__doc__ = f"Zabbix server: {_ZABBIX_URL}\n\n" + fn.__doc__
    return fn


mcp = FastMCP("Zabbix MCP Server")


@mcp.tool()
@_with_server_url
def zabbix_api(method: str, params: dict[str, Any] | None = None) -> str:
    """Execute Zabbix API method.

    This is the main tool for interacting with Zabbix. It requires multiple
    iterations to achieve complex goals. Use other tools for guidance.

    WORKFLOW:
    1. If unsure about method/params: call zabbix_api_docs(method) first
    2. If unsure about available methods: call zabbix_api_list() first
    3. Execute the API call with this tool
    4. If empty results or errors: iterate with different params/filters
    5. Continue iterating until goal is achieved

    COMMON PATTERNS:
    - Finding an object requires 2+ calls (find ID, then get details)
    - CPU usage example: Find host by name, get its items, filter CPU item, get history
    - Empty results often mean wrong filters - try broader search first

    Args:
        method: Zabbix API method (format: 'object.action').
        Examples: 'host.get', 'item.create', 'trigger.update'
        params: Method parameters (optional). For 'get' operations,
        specify 'output' to limit fields (by default all fields are returned).

    Returns:
        JSON response from Zabbix API.

    Examples:
    # Simple query
    zabbix_api('host.get', {'output': ['hostid', 'name']})

    # Multi-step: Find host, then get items
    # Step 1: Find host ID
    hosts = zabbix_api('host.get', {'filter': {'host': 'my-srv-01'}, 'output': ['hostid']})
    # Step 2: Get CPU items for that host
    items = zabbix_api('item.get', {'hostids': ['12345'], 'search': {'name': 'CPU'}, 'output': ['itemid', 'name']})
    # Step 3: Get history for specific item
    history = zabbix_api('history.get', {'itemids': ['67890'], 'output': 'extend', 'history': 0, 'limit': 10})

    Note:
    - Use zabbix_api_docs() for method documentation
    - Use zabbix_api_list() for available methods
    - Iterate multiple times - complex queries need 2-5 API calls
    """
    check_method_allowed(method)

    if is_read_only() and not is_read_operation(method):
        raise ValueError(
            f"Server is in read-only mode - operation '{method}' is not allowed. "
            f"Only safe read operations (get, version, check, export) are permitted. "
            f"Write operations (create, update, delete) are blocked."
        )

    client = get_zabbix_client()

    if params is None:
        params = {}

    parts = method.split(".")
    if len(parts) != 2:
        raise ValueError(
            f"Invalid method format: '{method}'. "
            f"Expected format: 'object.action' (e.g., 'host.get', 'item.create')"
        )

    api_object, api_action = parts

    try:
        api_obj = getattr(client, api_object)
        api_method = getattr(api_obj, api_action)
    except AttributeError:
        available = sorted(attr for attr in dir(client) if not attr.startswith("_"))
        raise ValueError(
            f"Unknown API object or method: '{method}'. "
            f"Available API objects: {', '.join(available)}"
        ) from None

    try:
        if params:
            result = api_method(**params)
        else:
            result = api_method()

        logger.info(f"Successfully executed {method}")
        return format_response(result)

    except Exception as e:
        logger.error(f"Error executing {method}: {e}")
        raise


@mcp.tool()
def zabbix_api_docs(method: str, version: str | None = None) -> str:
    """Get Zabbix API method documentation from the local docs snapshot.

    Call this BEFORE zabbix_api() if you are unsure about method parameters.
    Shows method description, required/optional parameters, and return value.
    Documentation is served from a pre-downloaded local snapshot (no
    internet access); see the README for how to refresh it.

    Args:
        method: Zabbix API method (format: \'object.action\').
        Examples: \'host.get\', \'item.create\', \'trigger.update\'
        version: Zabbix version (e.g., \'7.4\'). If omitted, uses the running
        Zabbix server version, falling back to ZABBIX_DOCS_VERSION or the
        newest locally available snapshot.

    Returns:
        Structured documentation with method description, parameters, and return value.

    Example:
        zabbix_api_docs(\'host.create\')
        zabbix_api_docs(\'host.get\', version=\'7.4\')

    Note:
        - Always call this when in doubt about parameters
        - Combine with zabbix_api_list() to discover available methods
    """
    try:
        return get_method_docs(method, version)
    except (LocalDocsError, ValueError) as e:
        logger.error(f"Error getting docs for {method}: {e}")
        raise


@mcp.tool()
def zabbix_api_list(resource: str | None = None) -> dict[str, list[str]]:
    """Get available Zabbix API objects and methods.

    Call this to discover what API methods are available before using zabbix_api().
    Returns objects and methods known from the local docs snapshot.

    Args:
        resource: Specific API object (e.g., 'host', 'item'). If omitted, returns all.

    Returns:
        Dictionary mapping API objects to their available methods.

    Examples:
        All objects: zabbix_api_list()
        Specific object: zabbix_api_list(resource='host')
        # Returns: {"host": ["create", "delete", "get", ...]}

    Note:
        - Use this to discover available methods
        - Then use zabbix_api_docs() for detailed parameter info
        - Finally use zabbix_api() to execute the call
    """
    api_objects = list_methods()
    if resource is None:
        return api_objects

    resource_lower = resource.lower()
    if resource_lower not in api_objects:
        available = ", ".join(sorted(api_objects.keys()))
        raise ValueError(
            f"Unknown API object: '{resource}'. Available objects: {available}"
        )

    return {resource_lower: api_objects[resource_lower]}


def _validate_transport_type(transport: str) -> None:
    valid_transports = ["stdio", "streamable-http"]
    if transport not in valid_transports:
        raise ValueError(
            f"Invalid {EnvVars.ZABBIX_MCP_TRANSPORT}: {transport}. "
            f"Must be 'stdio' or 'streamable-http'"
        )


def _validate_http_auth() -> None:
    auth_type = (get_env(EnvVars.AUTH_TYPE, "") or "").lower()
    if auth_type != "no-auth":
        raise ValueError(
            f"{EnvVars.AUTH_TYPE} must be set to 'no-auth' when using streamable-http transport"
        )


def _get_http_config() -> dict[str, Any]:
    return {
        "host": get_env(EnvVars.ZABBIX_MCP_HOST, "127.0.0.1"),
        "port": parse_int_env(EnvVars.ZABBIX_MCP_PORT, 8000),
        "stateless_http": parse_bool_env(EnvVars.ZABBIX_MCP_STATELESS_HTTP),
    }


def get_transport_config() -> dict[str, Any]:
    transport = (get_env(EnvVars.ZABBIX_MCP_TRANSPORT, "stdio") or "stdio").lower()
    _validate_transport_type(transport)

    config: dict[str, Any] = {"transport": transport}

    if transport == "streamable-http":
        _validate_http_auth()
        http_config = _get_http_config()
        config.update(http_config)
        logger.info(
            f"HTTP transport configured: {http_config['host']}:{http_config['port']}, "
            f"stateless_http={http_config['stateless_http']}"
        )

    return config


def main():
    logger.info("Starting Zabbix MCP Server")

    try:
        transport_config = get_transport_config()
        logger.info(f"Transport: {transport_config['transport']}")
    except ValueError as e:
        logger.error(f"Transport configuration error: {e}")
        return 1

    logger.info(f"Read-only mode: {is_read_only()}")
    logger.info(f"Zabbix URL: {get_env(EnvVars.ZABBIX_URL, 'Not configured')}")

    try:
        if transport_config["transport"] == "stdio":
            mcp.run()
        else:
            mcp.run(
                transport="streamable-http",
                host=transport_config["host"],
                port=transport_config["port"],
                stateless_http=transport_config["stateless_http"],
            )
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise


@mcp.custom_route("/health", methods=["GET"])
async def health(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok"})


if __name__ == "__main__":
    main()
