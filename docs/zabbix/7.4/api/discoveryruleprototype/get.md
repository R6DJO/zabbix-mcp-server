## discoveryruleprototype.get

### Description
Retrieves LLD rule prototypes according to the given parameters. This method is available to all user types.

### Parameters
- **itemids** (ID/array) - Return only LLD rule prototypes with the given IDs.
- **groupids** (ID/array) - Return only LLD rule prototypes that belong to the hosts from the given groups.
- **hostids** (ID/array) - Return only LLD rule prototypes that belong to the given hosts.
- **inherited** (boolean) - If set to true, return only LLD rule prototypes inherited from a template.
- **interfaceids** (ID/array) - Return only LLD rule prototypes using the given host interfaces.
- **monitored** (boolean) - If set to true, return only enabled LLD rule prototypes that belong to monitored hosts.
- **templated** (boolean) - If set to true, return only LLD rule prototypes that belong to templates.
- **templateids** (ID/array) - Return only LLD rule prototypes that belong to the given templates.
- **selectDiscoveryRule** (query) - Return a discoveryRule property with the parent LLD rule.
- **selectDiscoveryRulePrototype** (query) - Return a discoveryRulePrototype property with the parent LLD rule prototype.
- **selectDiscoveryRulePrototypes** (query) - Return a discoveryRulePrototypes property with child LLD rule prototypes.
- **selectFilter** (query) - Return a filter property with data of the filter used.
- **selectGraphs** (query) - Return a graphs property with graph prototypes.
- **selectHostPrototypes** (query) - Return a hostPrototypes property with host prototypes.
- **selectHosts** (query) - Return a hosts property with an array of hosts.
- **selectItems** (query) - Return an items property with item prototypes.
- **selectTriggers** (query) - Return a triggers property with trigger prototypes.
- **selectLLDMacroPaths** (query) - Return an lld_macro_paths property.
- **selectPreprocessing** (query) - Return a preprocessing property.
- **selectOverrides** (query) - Return an lld_rule_overrides property.
- **filter** (object) - Return only results that match the given filter.
- **limitSelects** (integer) - Limits the number of records returned by subselects.
- **sortfield** (string/array) - Sort the result by properties: itemid, name, key_, delay, type, status.

### Return Values
- **(integer/array)** Returns an array of objects or the count of retrieved objects if countOutput is used.
