## templategroup.delete

### Description
This method allows to delete template groups. A template group cannot be deleted if it contains templates that belong to this group only. This method is only available to Admin and Super admin user types.

### Parameters
- **templateGroupIds** (array) - Required - IDs of the template groups to delete.

### Return values
- **groupids** (array) - Returns an object containing the IDs of the deleted template groups.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templategroup.delete",
    "params": [
        "107814",
        "107815"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "groupids": [
            "107814",
            "107815"
        ]
    },
    "id": 1
}
