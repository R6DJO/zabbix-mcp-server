## iconmap.delete

### Description
This method allows to delete icon maps. This method is only available to Super admin user type.

### Parameters
- **iconMapIds** (array) - Required - IDs of the icon maps to delete.

### Return values
- **iconmapids** (array) - Returns an object containing the IDs of the deleted icon maps.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "iconmap.delete",
    "params": [
        "2",
        "5"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "iconmapids": [
            "2",
            "5"
        ]
    },
    "id": 1
}
