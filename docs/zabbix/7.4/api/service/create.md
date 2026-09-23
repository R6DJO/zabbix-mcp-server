## service.create

### Description
This method allows to create new services. It is available to users of any type, subject to user role permissions.

### Parameters
- **services** (object/array) - Required - Services to create.
- **children** (array) - Optional - Child services to be linked to the service (must have serviceid defined).
- **parents** (array) - Optional - Parent services to be linked to the service (must have serviceid defined).
- **tags** (array) - Optional - Service tags to be created.
- **problem_tags** (array) - Optional - Problem tags to be created.
- **status_rules** (array) - Optional - Status rules to be created.

### Return values
- **serviceids** (array) - Returns an object containing the IDs of the created services.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "service.create",
    "params": {
        "name": "Server 1",
        "algorithm": 1,
        "sortorder": 1
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "serviceids": [
            "5"
        ]
    },
    "id": 1
}
