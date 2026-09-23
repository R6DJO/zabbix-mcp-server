## connector.delete

### Description
This method allows to delete connector entries. This method is only available to Super admin user type.

### Parameters
- **connectorids** (array) - Required - IDs of the connectors to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "connector.delete",
    "params": [
        3,
        5
    ],
    "id": 1
}

### Response
#### Success Response
- **connectorids** (array) - Returns an object containing the IDs of the deleted connectors.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "connectorids": [
            "3",
            "5"
        ]
    },
    "id": 1
}
