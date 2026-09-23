## discoveryrule.get

### Description
Retrieves LLD rules based on the provided parameters. This method supports filtering by item IDs, host IDs, or specific rule attributes.

### Parameters
- **itemids** (array) - Optional - Return only LLD rules with the given IDs.
- **hostids** (array/string) - Optional - Return only LLD rules that belong to the given hosts.
- **filter** (object) - Optional - Return only results that exactly match the given filter (e.g., type, url).
- **output** (array/string) - Optional - Specifies the object properties to return.
- **selectFilter** (string) - Optional - Return the filter object for the LLD rule.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryrule.get",
    "params": {
        "output": ["name"],
        "selectFilter": "extend",
        "itemids": ["24681"]
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (array) - Returns an array of LLD rule objects.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "itemid": "24681",
            "name": "Filtered LLD rule",
            "filter": {
                "evaltype": "1",
                "formula": "",
                "conditions": [],
                "eval_formula": "A and B and C and D"
            }
        }
    ],
    "id": 1
}
