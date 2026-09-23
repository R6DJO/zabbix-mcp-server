## dashboard.update

### Description
Updates existing dashboards. This method is available to users of any type, subject to user role permissions.

### Parameters
- **dashboards** (object/array) - Required - Dashboard properties to be updated. The `dashboardid` must be defined.
- **pages** (array) - Optional - Dashboard pages to replace existing ones.
- **users** (array) - Optional - Dashboard user shares to replace existing elements.
- **userGroups** (array) - Optional - Dashboard user group shares to replace existing elements.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "dashboard.update",
    "params": {
        "dashboardid": "2",
        "name": "SQL server status"
    },
    "id": 1
}

### Response
#### Success Response
- **dashboardids** (array) - IDs of the updated dashboards.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "dashboardids": [
            "2"
        ]
    },
    "id": 1
}
