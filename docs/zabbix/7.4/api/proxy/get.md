## proxy.get

### Description
The method allows to retrieve proxies according to the given parameters. This method is available to users of any type.

### Parameters
- **proxyids** (ID/array) - Optional - Return only proxies with the given IDs.
- **proxy_groupids** (ID/array) - Optional - Return only proxies that belong to the given proxy groups.
- **selectAssignedHosts** (query) - Optional - Return an assignedHosts property with the hosts assigned to the proxy. Supports count.
- **selectHosts** (query) - Optional - Return a hosts property with the hosts monitored by the proxy. Supports count.
- **selectProxyGroup** (query) - Optional - Return a proxyGroup property with the proxy group object.
- **sortfield** (string/array) - Optional - Sort the result by the given properties (proxyid, name, operating_mode).
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
    "method": "proxy.get",
    "params": {
        "output": "extend"
    },
    "id": 1
}

### Response
Returns an array of objects or the count of retrieved objects if countOutput is used.
