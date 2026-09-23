## housekeeping.update

### Description
Updates existing housekeeping settings. This method is only available to Super admin user type.

### Parameters
- **housekeeping** (object) - Required - Housekeeping properties to be updated.

### Return values
- **result** (array) - Returns an array with the names of updated parameters.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "housekeeping.update",
    "params": {
        "hk_events_mode": "1",
        "hk_events_trigger": "200d",
        "hk_events_internal": "2d",
        "hk_events_discovery": "2d"
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        "hk_events_mode",
        "hk_events_trigger",
        "hk_events_internal",
        "hk_events_discovery"
    ],
    "id": 1
}
