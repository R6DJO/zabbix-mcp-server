## templategroup.create

### Description
This method allows to create new template groups. This method is only available to Super admin user type.

### Parameters
- **templateGroups** (object/array) - Required - Template groups to create. The method accepts template groups with the standard template group properties.

### Return values
- **groupids** (object) - Returns an object containing the IDs of the created template groups.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templategroup.create",
    "params": {
        "name": "Templates/Databases"
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "groupids": [
            "107820"
        ]
    },
    "id": 1
}
