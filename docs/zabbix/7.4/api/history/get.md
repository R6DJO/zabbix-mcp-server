## history.get

### Description
The method allows to retrieve history data according to the given parameters. This method may return historical data of a deleted entity if this data has not been removed by the housekeeper yet.

### Parameters
- **history** (integer) - Optional - History object types to return (0: numeric float, 1: character, 2: log, 3: numeric unsigned, 4: text, 5: binary).
- **hostids** (ID/array) - Optional - Return only history from the given hosts.
- **itemids** (ID/array) - Optional - Return only history from the given items.
- **time_from** (timestamp) - Optional - Return only values received after or at the given time.
- **time_till** (timestamp) - Optional - Return only values received before or at the given time.
- **sortfield** (string/array) - Optional - Sort the result by properties (itemid, clock, ns).
- **search** (object) - Optional - Return results that match the given pattern.
- **countOutput** (boolean) - Optional - Return the count of retrieved objects.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "history.get",
    "params": {
        "output": "extend",
        "history": 0,
        "itemids": "23296",
        "sortfield": "clock",
        "sortorder": "DESC",
        "limit": 10
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (array/integer) - Returns an array of objects or the count of retrieved objects.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "itemid": "23296",
            "clock": "1351090996",
            "value": "0.085",
            "ns": "563157632"
        }
    ],
    "id": 1
}
