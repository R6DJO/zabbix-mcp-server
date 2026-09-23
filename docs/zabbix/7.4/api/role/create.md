## role.create

### Description
This method allows to create new roles. This method is only available to Super admin user type.

### Parameters
- **roles** (object/array) - Required - Roles to create.
- **rules** (array) - Optional - Role rules to be created for the role.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "role.create",
    "params": {
        "name": "Operator",
        "type": "1",
        "rules": {
            "ui": [
                {
                    "name": "monitoring.hosts",
                    "status": "0"
                },
                {
                    "name": "monitoring.maps",
                    "status": "0"
                }
            ]
        }
    },
    "id": 1
}

### Response
#### Success Response
- **roleids** (array) - IDs of the created roles.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "roleids": [
            "5"
        ]
    },
    "id": 1
}
