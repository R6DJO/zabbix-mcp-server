## token.delete

### Description
This method allows to delete tokens. The Manage API tokens permission is required for the user role to manage tokens for other users.

### Parameters
- **tokenids** (array) - Required - IDs of the tokens to delete.

### Return values
- **tokenids** (array) - Returns an object containing the IDs of the deleted tokens.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "token.delete",
    "params": [
        "188",
        "192"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "tokenids": [
            "188",
            "192"
        ]
    },
    "id": 1
}
