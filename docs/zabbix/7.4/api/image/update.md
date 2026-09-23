## image.update

### Description
This method allows to update existing images. This method is only available to Super admin user type.

### Parameters
- **images** (object/array) - Required - Image properties to be updated. The imageid property must be defined for each image.

### Return values
- **imageids** (array) - Returns an object containing the IDs of the updated images.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "image.update",
    "params": {
        "imageid": "2",
        "name": "Cloud icon"
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "imageids": [
            "2"
        ]
    },
    "id": 1
}
