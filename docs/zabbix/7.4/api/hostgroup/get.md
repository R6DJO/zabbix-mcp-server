## hostgroup.get

### Description
The method allows to retrieve host groups according to the given parameters. This method is available to users of any type.

### Parameters
- **graphids** (ID/array) - Return only host groups that contain hosts with the given graphs.
- **groupids** (ID/array) - Return only host groups with the given host group IDs.
- **hostids** (ID/array) - Return only host groups that contain the given hosts.
- **maintenanceids** (ID/array) - Return only host groups that are affected by the given maintenances.
- **triggerids** (ID/array) - Return only host groups that contain hosts with the given triggers.
- **with_graphs** (boolean) - Return only host groups that contain hosts with graphs.
- **with_graph_prototypes** (boolean) - Return only host groups that contain hosts with graph prototypes.
- **with_hosts** (boolean) - Return only host groups that contain hosts.
- **with_httptests** (boolean) - Return only host groups that contain hosts with web checks.
- **with_items** (boolean) - Return only host groups that contain hosts with items.
- **with_item_prototypes** (boolean) - Return only host groups that contain hosts with item prototypes.
- **with_simple_graph_item_prototypes** (boolean) - Return only host groups that contain hosts with item prototypes, which are enabled for creation and have numeric type of information.
- **with_monitored_httptests** (boolean) - Return only host groups that contain hosts with enabled web checks.
- **with_monitored_hosts** (boolean) - Return only host groups that contain monitored hosts.
- **with_monitored_items** (boolean) - Return only host groups that contain hosts with enabled items.
- **with_monitored_triggers** (boolean) - Return only host groups that contain hosts with enabled triggers.
- **with_simple_graph_items** (boolean) - Return only host groups that contain hosts with numeric items.
- **with_triggers** (boolean) - Return only host groups that contain hosts with triggers.
- **selectDiscoveryRules** (query) - Return a discoveryRules property with the LLD rules that discovered the host group.
- **selectDiscoveryData** (query) - Return a discoveryData property with the host group discovery objects.
- **selectHostPrototypes** (query) - Return a hostPrototypes property with host prototypes that discovered this host group.
- **selectHosts** (query) - Return a hosts property with the hosts that belong to the host group.
- **limitSelects** (integer) - Limits the number of records returned by subselects.
- **sortfield** (string/array) - Sort the result by the given properties (groupid, name).
- **countOutput** (boolean) - Return the count of retrieved objects.
- **editable** (boolean) - Return only host groups that the user has write permissions to.
- **excludeSearch** (boolean) - Exclude results that match the search criteria.
- **filter** (object) - Filter by exact match.
- **limit** (integer) - Limit the number of records.
- **output** (query) - Define the output properties.
- **preservekeys** (boolean) - Use IDs as keys in the result array.
- **search** (object) - Search by pattern.
- **searchByAny** (boolean) - Return results that match any of the search criteria.
- **searchWildcardsEnabled** (boolean) - Enable wildcards for search.
- **sortorder** (string/array) - Sort order.
- **startSearch** (boolean) - Start search.
- **selectGroupDiscoveries** (query) - Return a groupDiscoveries property (deprecated).

### Response
- **Returns** (integer/array) - Returns an array of objects or the count of retrieved objects if countOutput is used.
