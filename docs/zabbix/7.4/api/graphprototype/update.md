## graphprototype.update

### Description
Updates existing graph prototypes. This method is restricted to Admin and Super admin user types.

### Parameters
- **graphPrototypes** (object/array) - Required - Graph prototype properties to be updated. The `graphid` property must be defined for each object.
- **gitems** (array) - Optional - Graph items to replace existing ones. If `gitemid` is provided, the item is updated; otherwise, a new item is created.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "graphprototype.update",
    "params": {
        "graphid": "439",
        "width": 1100,
        "height": 400
    },
    "id": 1
}

### Response
#### Success Response (200)
- **graphids** (array) - IDs of the updated graph prototypes.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "graphids": [
            "439"
        ]
    },
    "id": 1
}
