## item.delete

### Description
This method allows to delete items. Web items cannot be deleted via the Zabbix API. This method is only available to Admin and Super admin user types.

### Parameters
- **itemIds** (array) - Required - IDs of the items to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "item.delete",
    "params": [
        "22982",
        "22986"
    ],
    "id": 1
}

### Response
#### Success Response
- **itemids** (array) - Returns an object containing the IDs of the deleted items.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "22982",
            "22986"
        ]
    },
    "id": 1
}
