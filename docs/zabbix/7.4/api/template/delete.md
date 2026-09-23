## template.delete

### Description
This method allows to delete templates. Deleting a template will cause deletion of all template entities (items, triggers, graphs, etc.).

### Parameters
- **templateIds** (array) - Required - IDs of the templates to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "template.delete",
    "params": [
        "13",
        "32"
    ],
    "id": 1
}

### Response
#### Success Response
- **templateids** (array) - Returns an object containing the IDs of the deleted templates.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "templateids": [
            "13",
            "32"
        ]
    },
    "id": 1
}
