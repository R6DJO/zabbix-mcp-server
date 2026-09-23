## item.update

### Description
This method allows to update existing items. Web items cannot be updated via the Zabbix API. This method is only available to Admin and Super admin user types.

### Parameters
- **items** (object/array) - Required - Item properties to be updated. The itemid property must be defined for each item.
- **preprocessing** (array) - Optional - Item preprocessing options to replace the current preprocessing options.
- **tags** (array) - Optional - Item tags.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "item.update",
    "params": {
        "itemid": "10092",
        "status": 0
    },
    "id": 1
}

### Response
#### Success Response (200)
- **itemids** (array) - IDs of the updated items.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "10092"
        ]
    },
    "id": 1
}
