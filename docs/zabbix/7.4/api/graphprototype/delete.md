## graphprototype.delete

### Description
This method allows to delete graph prototypes. This method is only available to Admin and Super admin user types.

### Parameters
- **graphPrototypeIds** (array) - Required - IDs of the graph prototypes to delete.

### Return values
- **graphids** (array) - Returns an object containing the IDs of the deleted graph prototypes.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "graphprototype.delete",
    "params": [
        "652",
        "653"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "graphids": [
            "652",
            "653"
        ]
    },
    "id": 1
}
