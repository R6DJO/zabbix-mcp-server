## history.clear

### Description
This method allows to clear item history. This method is only available to Admin and Super admin user types.

### Parameters
- **itemids** (array) - Required - IDs of items to clear.

### Return values
- **itemids** (array) - Returns an object containing the IDs of the cleared items.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "history.clear",
    "params": [
        "10325",
        "13205"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "10325",
            "13205"
        ]
    },
    "id": 1
}
