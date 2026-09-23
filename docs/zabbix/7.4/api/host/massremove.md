## host.massremove

### Description
This method allows to remove related objects from multiple hosts. This method is only available to Admin and Super admin user types.

### Parameters
- **hostids** (ID/array) - Required - IDs of the hosts to be updated.
- **groupids** (ID/array) - Optional - IDs of the host groups to remove the given hosts from.
- **interfaces** (object/array) - Optional - Host interfaces to remove from the given hosts. The host interface object must have only the ip, dns and port properties defined.
- **macros** (string/array) - Optional - User macros to delete from the given hosts.
- **templateids** (ID/array) - Optional - IDs of the templates to unlink from the given hosts.
- **templateids_clear** (ID/array) - Optional - IDs of the templates to unlink and clear from the given hosts.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "host.massremove",
    "params": {
        "hostids": ["69665", "69666"],
        "templateids_clear": "325"
    },
    "id": 1
}

### Response
#### Success Response (200)
- **hostids** (array) - IDs of the updated hosts.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "hostids": [
            "69665",
            "69666"
        ]
    },
    "id": 1
}
