## templategroup.propagate

### Description
This method allows to apply permissions to all template groups' subgroups. This method is only available to Super admin user types.

### Parameters
- **groups** (object/array) - Required - Template groups to propagate. Must have only the groupid property defined.
- **permissions** (boolean) - Required - Set true if need to propagate permissions.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templategroup.propagate",
    "params": {
        "groups": [
            {
                "groupid": "15"
            }
        ],
        "permissions": true
    },
    "id": 1
}

### Response
#### Success Response (200)
- **groupids** (array) - IDs of the propagated template groups.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "groupids": [
            "15"
        ]
    },
    "id": 1
}
