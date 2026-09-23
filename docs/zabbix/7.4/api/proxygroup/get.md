## proxygroup.get

### Description
The method allows to retrieve proxy groups according to the given parameters. This method is available to users of any type.

### Parameters
- **proxy_groupids** (ID/array) - Optional - Return only proxy groups with the given IDs.
- **proxyids** (ID/array) - Optional - Return only proxy groups that contain the given proxies.
- **selectProxies** (query) - Optional - Return a proxies property with the proxies that belong to the proxy group.
- **sortfield** (string/array) - Optional - Sort the result by the given properties (proxy_groupid, name).
- **countOutput** (boolean) - Optional - Return the count of retrieved objects.
- **editable** (boolean) - Optional
- **excludeSearch** (boolean) - Optional
- **filter** (object) - Optional
- **limit** (integer) - Optional
- **output** (query) - Optional
- **preservekeys** (boolean) - Optional
- **search** (object) - Optional
- **searchByAny** (boolean) - Optional
- **searchWildcardsEnabled** (boolean) - Optional
- **sortorder** (string/array) - Optional
- **startSearch** (boolean) - Optional

### Request Example
{
    "jsonrpc": "2.0",
    "method": "proxygroup.get",
    "params": {
        "output": "extend",
        "selectProxies": ["proxyid", "name"]
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (integer/array) - Returns an array of objects or the count of retrieved objects.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "proxy_groupid": "1",
            "name": "Proxy group 1",
            "failover_delay": "1m",
            "min_online": "3",
            "description": "",
            "state": "1",
            "proxies": [
                {
                    "proxyid": "1",
                    "name": "proxy 1"
                },
                {
                    "proxyid": "2",
                    "name": "proxy 2"
                }
            ]
        }
    ],
    "id": 1
}
