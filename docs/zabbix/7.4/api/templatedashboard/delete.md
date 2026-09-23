## templatedashboard.delete

### Description
This method allows to delete template dashboards. This method is only available to Admin and Super admin user types.

### Parameters
- **templateDashboardIds** (array) - Required - IDs of the template dashboards to delete.

### Return values
- **dashboardids** (array) - Returns an object containing the IDs of the deleted template dashboards.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templatedashboard.delete",
    "params": [
        "45",
        "46"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "dashboardids": [
            "45",
            "46"
        ]
    },
    "id": 1
}
