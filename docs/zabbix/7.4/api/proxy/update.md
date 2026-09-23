## proxy.update

### Description
Updates existing proxy configurations. The `proxyid` property is required for each proxy being updated.

### Parameters
- **proxies** (object/array) - Required - Proxy properties to be updated.
- **hosts** (array) - Optional - Hosts to be monitored by the proxy. Must contain objects with `hostid` defined.

### Return values
- **proxyids** (array) - Returns an object containing the IDs of the updated proxies.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "proxy.update",
    "params": {
        "proxyid": "10293",
        "hosts": [
            { "hostid": "10294" },
            { "hostid": "10295" }
        ]
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "proxyids": ["10293"]
    },
    "id": 1
}
