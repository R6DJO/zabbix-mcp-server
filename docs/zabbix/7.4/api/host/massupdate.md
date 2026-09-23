## host.massupdate

### Description
This method allows to simultaneously replace or remove related objects and update properties on multiple hosts. This method is only available to Admin and Super admin user types.

### Parameters
- **hosts** (object/array) - Required - Hosts to be updated. The hosts must have only the hostid property defined.
- **groups** (object/array) - Optional - Host groups to replace the current host groups the hosts belong to. The host groups must have only the groupid property defined.
- **interfaces** (object/array) - Optional - Host interfaces to replace the current host interfaces on the given hosts.
- **inventory** (object) - Optional - Host inventory properties.
- **macros** (object/array) - Optional - User macros to replace the current user macros on the given hosts.
- **templates** (object/array) - Optional - Templates to replace the currently linked templates on the given hosts. The templates must have only the templateid property defined.
- **templates_clear** (object/array) - Optional - Templates to unlink and clear from the given hosts. The templates must have only the templateid property defined.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "host.massupdate",
    "params": {
        "hosts": [
            {
                "hostid": "69665"
            },
            {
                "hostid": "69666"
            }
        ],
        "status": 0
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
