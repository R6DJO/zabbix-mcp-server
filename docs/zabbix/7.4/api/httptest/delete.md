## httptest.delete

### Description
This method allows to delete web scenarios. This method is only available to Admin and Super admin user types.

### Parameters
- **webScenarioIds** (array) - Required - IDs of the web scenarios to delete.

### Return values
- **httptestids** (array) - Returns an object containing the IDs of the deleted web scenarios.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "httptest.delete",
    "params": [
        "2",
        "3"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "httptestids": [
            "2",
            "3"
        ]
    },
    "id": 1
}
