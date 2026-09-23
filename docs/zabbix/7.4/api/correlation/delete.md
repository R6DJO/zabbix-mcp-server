## correlation.delete

### Description
This method allows to delete correlations. This method is only available to Super admin user type.

### Parameters
- **correlationids** (array) - Required - IDs of the correlations to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "correlation.delete",
    "params": [
        "1",
        "2"
    ],
    "id": 1
}

### Response
#### Success Response
- **correlationids** (array) - IDs of the deleted correlations.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "correlationids": [
            "1",
            "2"
        ]
    },
    "id": 1
}
