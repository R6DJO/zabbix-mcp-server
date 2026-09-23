## map.delete

### Description
This method allows to delete maps. This method is available to users of any type.

### Parameters
- **mapIds** (array) - Required - IDs of the maps to delete.

### Return values
- **sysmapids** (array) - Returns an object containing the IDs of the deleted maps.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "map.delete",
    "params": [
        "12",
        "34"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "sysmapids": [
            "12",
            "34"
        ]
    },
    "id": 1
}
