## graphprototype.get

### Description
The method allows to retrieve graph prototypes according to the given parameters.

### Parameters
- **discoveryids** (ID/array) - Optional - Return only graph prototypes that belong to the given discovery rules.
- **graphids** (ID/array) - Optional - Return only graph prototypes with the given IDs.
- **groupids** (ID/array) - Optional - Return only graph prototypes that belong to hosts or templates in the given host groups or template groups.
- **hostids** (ID/array) - Optional - Return only graph prototypes that belong to the given hosts.
- **inherited** (boolean) - Optional - If set to true return only graph prototypes inherited from a template.
- **itemids** (ID/array) - Optional - Return only graph prototypes that contain the given item prototypes.
- **templated** (boolean) - Optional - If set to true return only graph prototypes that belong to templates.
- **templateids** (ID/array) - Optional - Return only graph prototypes that belong to the given templates.
- **selectDiscoveryData** (query) - Optional - Return a discoveryData property with the graph prototype discovery object data.
- **selectDiscoveryRule** (query) - Optional - Return a discoveryRule property with the LLD rule that the graph prototype belongs to.
- **selectDiscoveryRulePrototype** (query) - Optional - Return a discoveryRulePrototype property with the parent LLD rule prototype that the graph prototype belongs to.
- **selectGraphItems** (query) - Optional - Return a gitems property with the graph items used in the graph prototype.
- **selectHostGroups** (query) - Optional - Return a hostgroups property with the host groups that the graph prototype belongs to.
- **selectHosts** (query) - Optional - Return a hosts property with the hosts that the graph prototype belongs to.
- **selectItems** (query) - Optional - Return an items property with the items and item prototypes used in the graph prototype.
- **selectTemplateGroups** (query) - Optional - Return a templategroups property with the template groups that the graph prototype belongs to.
- **selectTemplates** (query) - Optional - Return a templates property with the templates that the graph prototype belongs to.
- **filter** (object) - Optional - Return only those results that exactly match the given filter.
- **sortfield** (string/array) - Optional - Sort the result by the given properties.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "graphprototype.get",
    "params": {
        "output": "extend",
        "discoveryids": "27426"
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (array) - Returns an array of graph prototype objects or the count of objects if countOutput is used.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "graphid": "1017",
            "name": "Disk space usage {#FSNAME}",
            "width": "600",
            "height": "340",
            "templateid": "442",
            "graphtype": "2",
            "flags": "2"
        }
    ],
    "id": 1
}
