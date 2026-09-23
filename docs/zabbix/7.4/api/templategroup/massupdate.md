## templategroup.massupdate

### Description
This method allows to replace templates with the specified ones in multiple template groups.

### Parameters
- **groups** (object/array) - Required - Template groups to be updated. The template groups must have only the groupid property defined.
- **templates** (object/array) - Required - Templates to replace the current template on the given template groups. All other templates, except the ones mentioned, will be excluded from template groups. The templates must have only the templateid property defined.

### Return values
- **groupids** (array) - Returns an object containing the IDs of the updated template groups.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templategroup.massupdate",
    "params": {
        "groups": [
            {
                "groupid": "8"
            }
        ],
        "templates": [
            {
                "templateid": "40050"
            }
        ]
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "groupids": [
            "8"
        ]
    },
    "id": 1
}
