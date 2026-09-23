## item.get

### Description
Retrieves items matching the specified criteria, such as host IDs, trigger associations, and key patterns.

### Parameters
- **output** (string) - The output format of the result.
- **hostids** (string) - Filter by host ID.
- **with_triggers** (boolean) - If true, returns only items used in triggers.
- **search** (object) - Search criteria for item fields (e.g., key_).
- **sortfield** (string) - Field to sort the results by.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": "extend",
        "hostids": "10084",
        "with_triggers": true,
        "search": {
            "key_": "system.cpu"
        },
        "sortfield": "name"
    },
    "id": 1
}

### Response
#### Success Response
- **result** (array) - A list of item objects matching the criteria.
