## event.get

## JSON-RPC event.get

### Description
Retrieves events based on the provided parameters, such as object IDs.

### Request Parameters
- **output** (string) - Specifies the output properties to return.
- **selectAcknowledges** (string) - Specifies whether to include acknowledgment data.
- **selectSuppressionData** (string) - Specifies whether to include suppression data.
- **selectTags** (string) - Specifies whether to include event tags.
- **objectids** (string) - The ID of the object (e.g., trigger) to filter events by.
- **sortfield** (array) - Fields to sort the results by.
- **sortorder** (string) - The order of sorting (e.g., DESC).

### Request Example
{
    "jsonrpc": "2.0",
    "method": "event.get",
    "params": {
        "output": "extend",
        "selectAcknowledges": "extend",
        "selectSuppressionData": "extend",
        "selectTags": "extend",
        "objectids": "22395",
        "sortfield": ["clock", "eventid"],
        "sortorder": "DESC"
    },
    "id": 1
}

### Response
#### Success Response
- **result** (array) - A list of event objects matching the criteria.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "eventid": "20",
            "name": "Load average is too high",
            "tags": []
        }
    ],
    "id": 1
}
