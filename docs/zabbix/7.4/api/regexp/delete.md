## regexp.delete

### Description
This method allows to delete global regular expressions. This method is only available to Super admin user types.

### Parameters
- **regexpids** (array) - Required - IDs of the regular expressions to delete.

### Return values
- **regexpids** (array) - Returns an object containing the IDs of the deleted regular expressions.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "regexp.delete",
    "params": [
        "16",
        "17"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "regexpids": [
            "16",
            "17"
        ]
    },
    "id": 1
}
