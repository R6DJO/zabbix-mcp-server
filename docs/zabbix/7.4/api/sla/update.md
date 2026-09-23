## sla.update

### Description
Updates existing SLA entries. This method is restricted to Admin and Super admin user types.

### Parameters
- **slaids** (object/array) - Required - SLA properties to be updated. The 'slaid' property must be defined for each SLA.
- **service_tags** (array) - Optional - SLA service tags to replace the current ones.
- **schedule** (array) - Optional - SLA schedule to replace the current one. An empty array sets the schedule to 24x7.
- **excluded_downtimes** (array) - Optional - SLA excluded downtimes to replace the current ones.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "sla.update",
    "params": [
        {
            "slaid": "5",
            "name": "NoSQL Database engines",
            "slo": "95",
            "period": 2,
            "service_tags": [
                {
                    "tag": "database",
                    "operator": "0",
                    "value": "redis"
                }
            ]
        }
    ],
    "id": 1
}

### Response
#### Success Response (200)
- **slaids** (array) - IDs of the updated SLAs.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "slaids": [
            "5"
        ]
    },
    "id": 1
}
