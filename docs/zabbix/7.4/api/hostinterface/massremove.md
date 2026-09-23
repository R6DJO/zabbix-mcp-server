## hostinterface.massremove

### Description
This method allows to remove host interfaces from the given hosts. This method is only available to Admin and Super admin user types.

### Parameters
- **interfaces** (object/array) - Required - Host interfaces to remove from the given hosts. The object must have only the `ip`, `dns` and `port` properties defined.
- **hostids** (ID/array) - Required - IDs of the hosts to be updated.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "hostinterface.massremove",
    "params": {
        "hostids": [
            "30050",
            "30052"
        ],
        "interfaces": {
            "dns": "",
            "ip": "127.0.0.1",
            "port": "161"
        }
    },
    "id": 1
}

### Response
#### Success Response (200)
- **interfaceids** (array) - IDs of the deleted host interfaces.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "interfaceids": [
            "30069",
            "30070"
        ]
    },
    "id": 1
}
