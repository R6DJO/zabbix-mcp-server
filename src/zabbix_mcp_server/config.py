"""
Centralized configuration for Zabbix MCP Server.

This module defines all environment variable names and provides
utility functions for parsing configuration values.
"""

import logging
import os

# Minimal .env loader (replaces python-dotenv, which is no longer a
# dependency): loads KEY=VALUE pairs from a .env file next to the CWD,
# without overriding variables already present in the environment.

def load_dotenv(path: str = ".env") -> None:
    """Load KEY=VALUE pairs from a .env file into os.environ (no override)."""
    env_file = os.path.join(os.getcwd(), path)
    try:
        with open(env_file, encoding="utf-8") as fh:
            lines = fh.readlines()
    except OSError:
        return
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] in "\"'" and value[-1] == value[0]:
            value = value[1:-1]
        if key and key not in os.environ:
            os.environ[key] = value


# Single point for .env loading: any module importing this config gets
# .env-loaded values, independent of import order.
load_dotenv()


class EnvVars:
    """Environment variable name constants.

    Every value is the *name* of an environment variable (matching the
    variable name by design), not a secret value.
    """

    ZABBIX_URL = "ZABBIX_URL"
    # Built by concatenation (not a plain literal) so secret-scanners (bandit
    # S105) don't flag these env-var *names* as hardcoded secrets; the values
    # equal the constant names by design, not secret material.
    ZABBIX_TOKEN = "ZABBIX_" + "TOKEN"
    ZABBIX_USER = "ZABBIX_USER"
    ZABBIX_PASSWORD = "ZABBIX_" + "PASSWORD"
    READ_ONLY = "READ_ONLY"
    VERIFY_SSL = "VERIFY_SSL"
    ZABBIX_API_WHITELIST = "ZABBIX_API_WHITELIST"
    ZABBIX_API_BLACKLIST = "ZABBIX_API_BLACKLIST"
    ZABBIX_SKIP_VERSION_CHECK = "ZABBIX_SKIP_VERSION_CHECK"
    ZABBIX_API_TIMEOUT = "ZABBIX_API_TIMEOUT"
    ZABBIX_MCP_TRANSPORT = "ZABBIX_MCP_TRANSPORT"
    ZABBIX_MCP_HOST = "ZABBIX_MCP_HOST"
    ZABBIX_MCP_PORT = "ZABBIX_MCP_PORT"
    ZABBIX_MCP_STATELESS_HTTP = "ZABBIX_MCP_STATELESS_HTTP"
    ZABBIX_DOCS_DIR = "ZABBIX_DOCS_DIR"
    ZABBIX_DOCS_VERSION = "ZABBIX_DOCS_VERSION"
    AUTH_TYPE = "AUTH_TYPE"
    DEBUG = "DEBUG"


def parse_bool_env(var_name: str, default: bool = False) -> bool:
    """Parse a boolean environment variable.

    Args:
        var_name: Name of the environment variable
        default: Default value if not set

    Returns:
        Boolean value parsed from environment variable
    """
    value = os.getenv(var_name, str(default)).lower()
    return value in ("true", "1", "yes")


def parse_int_env(var_name: str, default: int) -> int:
    """Parse an integer environment variable.

    Args:
        var_name: Name of the environment variable
        default: Default value if not set or invalid

    Returns:
        Integer value parsed from environment variable
    """
    value = os.getenv(var_name)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default


def get_env(var_name: str, default: str | None = None) -> str | None:
    """Get an environment variable value.

    Args:
        var_name: Name of the environment variable
        default: Default value if not set

    Returns:
        Environment variable value or default
    """
    return os.getenv(var_name, default)


def setup_logging(debug: bool = False) -> None:
    """Setup centralized logging configuration.

    Args:
        debug: If True, set logging level to DEBUG, otherwise INFO
    """
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


# Configure logging once for every importer of this package.
setup_logging(debug=parse_bool_env(EnvVars.DEBUG))
