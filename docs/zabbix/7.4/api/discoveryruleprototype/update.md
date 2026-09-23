## discoveryruleprototype.update

### Description
This method allows to update existing LLD rule prototypes. Note that the updating of already discovered prototypes is limited. This method is only available to Admin and Super admin user types.

### Parameters
- **lldRules** (object/array) - Required - LLD rule prototype properties to be updated. The itemid property must be defined for each LLD rule prototype.
- **filter** (object) - Optional - LLD rule prototype filter to replace the existing filter.
- **preprocessing** (object/array) - Optional - LLD rule prototype preprocessing options to replace the existing preprocessing options.
- **lld_macro_paths** (object/array) - Optional - LLD rule prototype lld_macro_path options to replace the existing lld_macro_path options.
- **overrides** (object/array) - Optional - LLD rule prototype overrides options to replace the existing overrides options.

### Return values
- **itemids** (object) - Returns an object containing the IDs of the updated LLD rule prototypes.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryruleprototype.update",
    "params": {
        "itemid": "47253",
        "preprocessing": [
            {
                "type": 12,
                "params": "$.tablespaces",
                "error_handler": 1
            }
        ]
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "47253"
        ]
    },
    "id": 1
}
