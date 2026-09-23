## hostprototype.create

### Description
This method allows to create new host prototypes. It is restricted to Admin and Super admin user types.

### Parameters
- **hostPrototypes** (object/array) - Required - Host prototypes to create.
- **ruleid** (ID) - Required - ID of the LLD rule that the host prototype belongs to.
- **groupLinks** (array) - Optional - Group links to be created for the host prototype.
- **groupPrototypes** (array) - Optional - Group prototypes to be created for the host prototype.
- **macros** (object/array) - Optional - User macros to be created for the host prototype.
- **tags** (object/array) - Optional - Host prototype tags.
- **interfaces** (object/array) - Optional - Host prototype custom interfaces.
- **templates** (object/array) - Optional - Templates to be linked to the host prototype.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "hostprototype.create",
    "params": {
        "host": "{#VM.NAME}",
        "ruleid": "23542",
        "custom_interfaces": "1",
        "groupLinks": [
            {
                "groupid": "2"
            }
        ],
        "groupPrototypes": [
            {
                "name": "{#HV.NAME}"
            }
        ],
        "tags": [
            {
                "tag": "datacenter",
                "value": "{#DATACENTER.NAME}"
            }
        ],
        "interfaces": [
            {
                "main": "1",
                "type": "2",
                "useip": "1",
                "ip": "127.0.0.1",
                "dns": "",
                "port": "161",
                "details": {
                    "version": "2",
                    "bulk": "1",
                    "community": "{$SNMP_COMMUNITY}"
                }
            }
        ]
    },
    "id": 1
}

### Response
#### Success Response
- **hostids** (array) - IDs of the created host prototypes.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "hostids": [
            "10103"
        ]
    },
    "id": 1
}
