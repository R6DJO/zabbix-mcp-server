## itemprototype.delete

### Description
This method allows to delete item prototypes. This method is only available to Admin and Super admin user types.

### Parameters
- **itemPrototypeIds** (array) - Required - IDs of the item prototypes to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "itemprototype.delete",
    "params": [
        "27352",
        "27356"
    ],
    "id": 1
}

### Response
#### Success Response
- **prototypeids** (array) - IDs of the deleted item prototypes.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "prototypeids": [
            "27352",
            "27356"
        ]
    },
    "id": 1
}
