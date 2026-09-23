## discoveryrule.create

### Description
This method allows to create a new LLD rule.

### Parameters
- **name** (string) - Required - Name of the LLD rule.
- **key_** (string) - Required - LLD rule key.
- **hostid** (string) - Required - ID of the host that the LLD rule belongs to.
- **type** (integer) - Required - LLD rule type.
- **interfaceid** (string) - Optional - ID of the host interface.
- **delay** (string) - Optional - Update interval of the LLD rule.
- **filter** (object) - Optional - LLD rule filter object.
- **query_fields** (array) - Optional - Query fields for HTTP agent LLD rules.
- **headers** (array) - Optional - Headers for HTTP agent LLD rules.
- **preprocessing** (array) - Optional - LLD rule preprocessing options.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryrule.create",
    "params": {
        "name": "Filtered LLD rule",
        "key_": "lld",
        "hostid": "10116",
        "type": 0,
        "interfaceid": "13",
        "delay": "30s",
        "filter": {
            "evaltype": 3,
            "formula": "(A and B) and (C or D)",
            "conditions": [
                {"macro": "{#MACRO1}", "value": "@regex1", "formulaid": "A"},
                {"macro": "{#MACRO1}", "value": "@regex2", "formulaid": "B"},
                {"macro": "{#MACRO2}", "value": "@regex3", "formulaid": "C"},
                {"macro": "{#MACRO2}", "value": "@regex4", "formulaid": "D"}
            ]
        }
    },
    "id": 1
}

### Response
#### Success Response (200)
- **itemids** (array) - Returns an array of IDs of the created LLD rules.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": ["27665"]
    },
    "id": 1
}
