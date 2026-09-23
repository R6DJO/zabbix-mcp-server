## templategroup.update

### Description
Updates existing template groups. Only the provided properties are updated; others remain unchanged.

### Parameters
- **templateGroups** (object/array) - Required - Template group properties to be updated. The `groupid` property must be defined for each template group.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templategroup.update",
    "params": {
        "groupid": "7",
        "name": "Templates/Databases"
    },
    "id": 1
}

### Response
#### Success Response
- **groupids** (array) - IDs of the updated template groups.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "groupids": [
            "7"
        ]
    },
    "id": 1
}
