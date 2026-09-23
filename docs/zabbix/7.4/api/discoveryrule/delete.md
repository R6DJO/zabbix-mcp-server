## discoveryrule.delete

### Description
This method allows to delete LLD rules. This method is only available to Admin and Super admin user types.

### Parameters
- **lldRuleIds** (array) - Required - IDs of the LLD rules to delete.

### Return values
- **ruleids** (array) - Returns an object containing the IDs of the deleted LLD rules.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryrule.delete",
    "params": [
        "27665",
        "27668"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "ruleids": [
            "27665",
            "27668"
        ]
    },
    "id": 1
}
