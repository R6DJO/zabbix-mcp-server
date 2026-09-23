## task.get

### Description
The method allows to retrieve tasks according to the given parameters. This method is only available to Super admin user type.

### Parameters
- **taskids** (ID/array) - Optional - Return only tasks with the given IDs.
- **output** (query) - Optional - These parameters are described in the reference commentary.
- **preservekeys** (boolean) - Optional

### Request Example
{
    "jsonrpc": "2.0",
    "method": "task.get",
    "params": {
        "output": "extend",
        "taskids": "1"
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (array) - Returns an array of task objects.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "taskid": "1",
            "type": "7",
            "status": "3",
            "clock": "1601039076",
            "ttl": "3600",
            "proxyid": null,
            "request": {},
            "result": {}
        }
    ],
    "id": 1
}
