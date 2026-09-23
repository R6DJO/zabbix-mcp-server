## template.get

### Description
The method allows to retrieve templates according to the given parameters. This method is available to users of any type.

### Parameters
- **templateids** (ID/array) - Optional - Return only templates with the given template IDs.
- **groupids** (ID/array) - Optional - Return only templates that belong to the given template groups.
- **parentTemplateids** (ID/array) - Optional - Return only templates that the given template is linked to.
- **hostids** (ID/array) - Optional - Return only templates that are linked to the given hosts/templates.
- **graphids** (ID/array) - Optional - Return only templates that contain the given graphs.
- **itemids** (ID/array) - Optional - Return only templates that contain the given items.
- **triggerids** (ID/array) - Optional - Return only templates that contain the given triggers.
- **with_items** (flag) - Optional - Return only templates that have items.
- **with_triggers** (flag) - Optional - Return only templates that have triggers.
- **with_graphs** (flag) - Optional - Return only templates that have graphs.
- **with_httptests** (flag) - Optional - Return only templates that have web scenarios.
- **evaltype** (integer) - Optional - Tag evaluation method (0: And/Or, 2: Or).
- **tags** (object/array) - Optional - Return only templates with the given tags.
- **selectTags** (query) - Optional - Return template tags in the tags property.
- **selectDiscoveryRules** (query) - Optional - Return a discoveryRules property with template LLD rules.
- **selectHosts** (query) - Optional - Return the hosts that are linked to the template in the hosts property.
- **selectTemplateGroups** (query) - Optional - Return the template groups that the template belongs to in the templategroups property.
- **selectTemplates** (query) - Optional - Return templates to which the given template is linked in the templates property.
- **selectParentTemplates** (query) - Optional - Return templates that are linked to the given template in the parentTemplates property.
- **selectHttpTests** (query) - Optional - Return the web scenarios from the template in the httpTests property.
- **selectItems** (query) - Optional - Return items from the template in the items property.
- **selectTriggers** (query) - Optional - Return triggers from the template in the triggers property.
- **selectGraphs** (query) - Optional - Return graphs from the template in the graphs property.
- **selectMacros** (query) - Optional - Return the macros from the template in the macros property.
- **selectDashboards** (query) - Optional - Return dashboards from the template in the dashboards property.
- **selectValueMaps** (query) - Optional - Return a valuemaps property with template value maps.
- **limitSelects** (integer) - Optional - Limits the number of records returned by subselects.
- **sortfield** (string/array) - Optional - Sort the result by the given properties (hostid, host, name, status).

### Response
#### Success Response
- **result** (integer/array) - Returns either an array of objects or the count of retrieved objects if countOutput is used.
