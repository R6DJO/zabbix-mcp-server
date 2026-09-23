## maintenance.delete

### Description
This method allows to delete maintenance periods. This method is only available to Admin and Super admin user types.

### Parameters
- **maintenanceIds** (array) - Required - IDs of the maintenance periods to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "maintenance.delete",
    "params": [
        "3",
        "1"
    ],
    "id": 1
}

### Response
#### Success Response
- **maintenanceids** (array) - IDs of the deleted maintenance periods.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "maintenanceids": [
            "3",
            "1"
        ]
    },
    "id": 1
}
