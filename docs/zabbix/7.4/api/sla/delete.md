## sla.delete

### Description
This method allows to delete SLA entries. This method is only available to Admin and Super admin user types.

### Parameters
- **slaids** (array) - Required - IDs of the SLAs to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "sla.delete",
    "params": [
        "4",
        "5"
    ],
    "id": 1
}

### Response
#### Success Response
- **slaids** (array) - Returns an object containing the IDs of the deleted SLAs.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "slaids": [
            "4",
            "5"
        ]
    },
    "id": 1
}
