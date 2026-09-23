## host.get

### Description
Retrieves hosts according to the given parameters. Supports filtering, searching, and selecting related data.

### Parameters
#### Query Parameters
- **selectHostGroups** (query) - Optional - Return a `hostgroups` property with host groups data.
- **selectHttpTests** (query) - Optional - Return an `httpTests` property with host web scenarios.
- **selectInterfaces** (query) - Optional - Return an `interfaces` property with host interfaces.
- **selectInventory** (query) - Optional - Return an `inventory` property with host inventory data.
- **selectItems** (query) - Optional - Return an `items` property with host items.
- **selectMacros** (query) - Optional - Return a `macros` property with host macros.
- **selectParentTemplates** (query) - Optional - Return a `parentTemplates` property with linked templates.
- **selectDashboards** (query) - Optional - Return a `dashboards` property.
- **selectTags** (query) - Optional - Return a `tags` property with host tags.
- **selectInheritedTags** (query) - Optional - Return an `inheritedTags` property with inherited tags.
- **selectTriggers** (query) - Optional - Return a `triggers` property with host triggers.
- **selectValueMaps** (query) - Optional - Return a `valuemaps` property with host value maps.
- **selectDiscoveryRules** (query) - Optional - Return a `discoveryRules` property with host low-level discovery rules.
- **selectHostDiscovery** (query) - Optional - Return a `hostDiscovery` property with host discovery object data.
- **filter** (object) - Optional - Return only results that exactly match the given filter.
- **limitSelects** (integer) - Optional - Limits the number of records returned by subselects.
- **search** (object) - Optional - Return results that match the given pattern (case-insensitive).
- **searchInventory** (object) - Optional - Return hosts with inventory data matching the pattern.
- **sortfield** (string/array) - Optional - Sort the result by properties: `hostid`, `host`, `name`, `status`.

### Response
#### Success Response
- **result** (integer/array) - Returns an array of objects or the count of retrieved objects if `countOutput` is used.
