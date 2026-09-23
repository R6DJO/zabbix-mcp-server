## proxygroup.delete

### Description
Allows to delete proxy groups. This method is only available to Super admin user type.

### Parameters
- **proxyGroupIds** (array) - Required - IDs of proxy groups to delete.

### Return values
- **proxy_groupids** (array) - IDs of the deleted proxy groups.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "proxygroup.delete",
    "params": [
        "5",
        "10"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "proxy_groupids": [
            "5",
            "10"
        ]
    },
    "id": 1
}
