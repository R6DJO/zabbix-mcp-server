## discoveryruleprototype.create

### Description
This method allows to create new LLD rule prototypes. This method is only available to Admin and Super admin user types.

### Parameters
- **lldRules** (object/array) - Required - LLD rule prototypes to create.
- **filter** (object) - Optional - LLD rule prototype filter for the LLD rule.
- **preprocessing** (object/array) - Optional - LLD rule prototype preprocessing options.
- **lld_macro_paths** (object/array) - Optional - LLD rule prototype lld_macro_path options.
- **overrides** (object/array) - Optional - LLD rule prototype overrides options.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryruleprototype.create",
    "params": {
        "name": "Discover tablespaces for {#DB}",
        "key_": "db.tablespace.discovery[{#DB}]",
        "hostid": "10084",
        "ruleid": "47251",
        "type": 23
    },
    "id": 1
}

### Response
#### Success Response (200)
- **itemids** (array) - Returns an object containing the IDs of the created LLD rule prototypes.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "47252"
        ]
    },
    "id": 1
}
