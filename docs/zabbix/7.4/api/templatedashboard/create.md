## templatedashboard.create

### Description
This method allows to create new template dashboards. This method is only available to Admin and Super admin user types.

### Parameters
- **templateDashboards** (object/array) - Required - Template dashboards to create.
- **pages** (array) - Required - Template dashboard pages to be created for the dashboard.

### Return values
- **dashboardids** (object) - Returns an object containing the IDs of the created template dashboards.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templatedashboard.create",
    "params": {
        "templateid": "10318",
        "name": "Graphs",
        "pages": [
            {
                "widgets": [
                    {
                        "type": "graph",
                        "x": 0,
                        "y": 0,
                        "width": 12,
                        "height": 5,
                        "view_mode": 0,
                        "fields": [
                            {
                                "type": 6,
                                "name": "graphid",
                                "value": "1123"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "dashboardids": [
            "32"
        ]
    },
    "id": 1
}
