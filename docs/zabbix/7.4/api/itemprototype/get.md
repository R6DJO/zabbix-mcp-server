## itemprototype.get

### Description
Retrieves all item prototypes for a specific LLD rule ID.

### Parameters
- **output** (string) - Required - Specifies the output format (e.g., "extend").
- **discoveryids** (string) - Required - The ID of the LLD rule to retrieve prototypes for.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "itemprototype.get",
    "params": {
        "output": "extend",
        "discoveryids": "27426"
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (array) - A list of item prototype objects.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "itemid": "23077",
            "name": "Incoming network traffic on en0",
            "key_": "net.if.in[en0]"
        }
    ],
    "id": 1
}
