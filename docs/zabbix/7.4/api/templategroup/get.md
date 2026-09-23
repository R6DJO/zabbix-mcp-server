## templategroup.get

### Description
The method allows to retrieve template groups according to the given parameters.

### Parameters
- **graphids** (ID/array) - Optional - Return only template groups that contain templates with the given graphs.
- **groupids** (ID/array) - Optional - Return only template groups with the given template group IDs.
- **templateids** (ID/array) - Optional - Return only template groups that contain the given templates.
- **triggerids** (ID/array) - Optional - Return only template groups that contain templates with the given triggers.
- **with_graphs** (boolean) - Optional - Return only template groups that contain templates with graphs.
- **with_graph_prototypes** (boolean) - Optional - Return only template groups that contain templates with graph prototypes.
- **with_httptests** (boolean) - Optional - Return only template groups that contain templates with web checks.
- **with_items** (boolean) - Optional - Return only template groups that contain templates with items.
- **with_item_prototypes** (boolean) - Optional - Return only template groups that contain templates with item prototypes.
- **with_simple_graph_item_prototypes** (boolean) - Optional - Return only template groups that contain templates with item prototypes, which are enabled for creation and have numeric type of information.
- **with_simple_graph_items** (boolean) - Optional - Return only template groups that contain templates with numeric items.
- **with_templates** (boolean) - Optional - Return only template groups that contain templates.
- **with_triggers** (boolean) - Optional - Return only template groups that contain templates with triggers.
- **selectTemplates** (query) - Optional - Return a templates property with the templates that belong to the template group.
- **limitSelects** (integer) - Optional - Limits the number of records returned by subselects.
- **sortfield** (string/array) - Optional - Sort the result by the given properties (groupid, name).

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templategroup.get",
    "params": {
        "output": "extend",
        "filter": {
            "name": [
                "Templates/Databases",
                "Templates/Modules"
            ]
        }
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
            "groupid": "13",
            "name": "Templates/Databases",
            "uuid": "748ad4d098d447d492bb935c907f652f"
        },
        {
            "groupid": "8",
            "name": "Templates/Modules",
            "uuid": "57b7ae836ca64446ba2c296389c009b7"
        }
    ],
    "id": 1
}
