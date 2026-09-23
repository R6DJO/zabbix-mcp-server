## discoveryrule.update

### Description
Updates existing LLD rules. The itemid property must be defined for each LLD rule, and only the passed properties will be updated.

### Parameters
- **lldRules** (object/array) - Required - LLD rule properties to be updated.
  - **itemid** (string) - Required - ID of the LLD rule.
  - **filter** (object) - Optional - LLD rule filter to replace the existing filter.
  - **preprocessing** (object/array) - Optional - LLD rule preprocessing options to replace the existing preprocessing options.
  - **lld_macro_paths** (object/array) - Optional - LLD rule lld_macro_path options to replace the existing lld_macro_path options.
  - **overrides** (object/array) - Optional - LLD rule overrides options to replace the existing overrides options.

### Return values
- **itemids** (array) - Returns an object containing the IDs of the updated LLD rules.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryrule.update",
    "params": {
        "itemid": "22450",
        "filter": {
            "evaltype": 1,
            "conditions": [
                {
                    "macro": "{#FSTYPE}",
                    "value": "@File systems for discovery"
                }
            ]
        }
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "22450"
        ]
    },
    "id": 1
}
