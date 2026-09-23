## map.update

### Description
Updates existing network maps. The mapid property is required for each map, while other properties are optional and will be updated if provided.

### Parameters
- **maps** (object/array) - Required - Map properties to be updated.
- **links** (array) - Optional - Map links to replace existing links.
- **selements** (array) - Optional - Map elements to replace existing elements.
- **urls** (array) - Optional - Map URLs to replace existing URLs.
- **users** (array) - Optional - Map user shares to replace existing shares.
- **userGroups** (array) - Optional - Map user group shares to replace existing shares.
- **shapes** (array) - Optional - Map shapes to replace existing shapes.
- **lines** (array) - Optional - Map lines to replace existing lines.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "map.update",
    "params": {
        "sysmapid": "8",
        "width": 1200,
        "height": 1200
    },
    "id": 1
}

### Response
#### Success Response (200)
- **sysmapids** (array) - IDs of the updated maps.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "sysmapids": [
            "8"
        ]
    },
    "id": 1
}
