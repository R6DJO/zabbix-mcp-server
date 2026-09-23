## history.push

### Description
Sends item history data to the Zabbix server. This method can be called by users of any type, provided they have the necessary permissions.

### Parameters
- **itemid** (ID) - Required if host and key are not set - ID of the related item.
- **host** (string) - Required if itemid is not set - Technical name of the host.
- **key** (string) - Required if itemid is not set - Item key.
- **value** (mixed) - Required - Item value.
- **clock** (timestamp) - Optional - Time when the value was received.
- **ns** (integer) - Optional - Nanoseconds when the value was received.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "history.push",
    "params": [
        {
            "itemid": 10600,
            "value": 0.5,
            "clock": 1690891294,
            "ns": 45440940
        }
    ],
    "id": 1
}

### Response
#### Success Response (200)
- **response** (string) - Status of the operation.
- **data** (array) - List of results for each item processed.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "response": "success",
        "data": [
            {
                "itemid": "10600"
            }
        ]
    },
    "id": 1
}
