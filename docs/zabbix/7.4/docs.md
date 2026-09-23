<!-- Zabbix 7.4 API docs snapshot
     Context7 library: /websites/zabbix_current_en
     Docs source: https://www.zabbix.com/documentation/current/en/manual/api
     Fetched: 2026-09-23T07:07:09+00:00
-->
<!-- method: action.create -->
## action.create

### Description
Creates new actions.

### Parameters
- **actions** (array) - The actions to create.
<!-- method: action.delete -->
## action.delete

### Description
Deletes actions.

### Method
POST

### Endpoint
action.delete
<!-- method: action.get -->
## action.get

### Description
Retrieves actions based on the given parameters.
<!-- method: action.update -->
## action.update

### Description
Updates actions.

### Method
POST

### Endpoint
action.update
<!-- method: apiinfo.version -->
## apiinfo.version

{
    "jsonrpc": "2.0",
    "method": "apiinfo.version",
    "params": [],
    "id": 1
}

{
    "jsonrpc": "2.0",
    "result": "7.4.0",
    "id": 1
}
<!-- method: authentication.update -->
## authentication.update

### Description
Updates authentication settings.
<!-- method: configuration.export -->
## configuration.export

### Description
Exports Zabbix configuration data.
<!-- method: configuration.import -->
## configuration.import

### Description
Imports configuration data from a file or string.
<!-- method: configuration.importcompare -->
## configuration.importcompare

### Description
Compares the template contained in the XML string to the current system elements and shows what will be changed if this template is imported.

### Parameters
- **format** (string) - Required - The format of the source string (e.g., "xml").
- **rules** (object) - Required - Import rules defining how to handle discoveryRules, graphs, host_groups, template_groups, httptests, items, templateLinkage, templates, templateDashboards, triggers, and valueMaps (createMissing, updateExisting, deleteMissing).
- **source** (string) - Required - The XML string containing the template data to compare.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "configuration.importcompare",
    "params": {
        "format": "xml",
        "rules": {
            "discoveryRules": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            },
            "graphs": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            },
            "host_groups": {
                "createMissing": true,
                "updateExisting": true
            },
            "template_groups": {
                "createMissing": true,
                "updateExisting": true
            },
            "httptests": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            },
            "items": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            },
            "templateLinkage": {
                "createMissing": true,
                "deleteMissing": true
            },
            "templates": {
                "createMissing": true,
                "updateExisting": true
            },
            "templateDashboards": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            },
            "triggers": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            },
            "valueMaps": {
                "createMissing": true,
                "updateExisting": true,
                "deleteMissing": true
            }
        },
        "source": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<zabbix_export>...</zabbix_export>"
    },
    "id": 1
}
<!-- method: connector.delete -->
## connector.delete

### Description
This method allows to delete connector entries. This method is only available to Super admin user type.

### Parameters
- **connectorids** (array) - Required - IDs of the connectors to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "connector.delete",
    "params": [
        3,
        5
    ],
    "id": 1
}

### Response
#### Success Response
- **connectorids** (array) - Returns an object containing the IDs of the deleted connectors.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "connectorids": [
            "3",
            "5"
        ]
    },
    "id": 1
}
<!-- method: connector.update -->
## connector.update

### Description
Updates a connector.
<!-- method: correlation.delete -->
## correlation.delete

### Description
This method allows to delete correlations. This method is only available to Super admin user type.

### Parameters
- **correlationids** (array) - Required - IDs of the correlations to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "correlation.delete",
    "params": [
        "1",
        "2"
    ],
    "id": 1
}

### Response
#### Success Response
- **correlationids** (array) - IDs of the deleted correlations.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "correlationids": [
            "1",
            "2"
        ]
    },
    "id": 1
}
<!-- method: dashboard.create -->
## dashboard.create

### Description
Creates a new dashboard.

### Method
JSON-RPC

### Parameters
- **Dashboard object** (object) - Required - The dashboard object to create.
<!-- method: dashboard.delete -->
## dashboard.delete

### Description
Deletes a dashboard.
<!-- method: dashboard.update -->
## dashboard.update

### Description
Updates existing dashboards. This method is available to users of any type, subject to user role permissions.

### Parameters
- **dashboards** (object/array) - Required - Dashboard properties to be updated. The `dashboardid` must be defined.
- **pages** (array) - Optional - Dashboard pages to replace existing ones.
- **users** (array) - Optional - Dashboard user shares to replace existing elements.
- **userGroups** (array) - Optional - Dashboard user group shares to replace existing elements.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "dashboard.update",
    "params": {
        "dashboardid": "2",
        "name": "SQL server status"
    },
    "id": 1
}

### Response
#### Success Response
- **dashboardids** (array) - IDs of the updated dashboards.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "dashboardids": [
            "2"
        ]
    },
    "id": 1
}
<!-- method: discoveryrule.create -->
## discoveryrule.create

### Description
This method allows to create a new LLD rule.

### Parameters
- **name** (string) - Required - Name of the LLD rule.
- **key_** (string) - Required - LLD rule key.
- **hostid** (string) - Required - ID of the host that the LLD rule belongs to.
- **type** (integer) - Required - LLD rule type.
- **interfaceid** (string) - Optional - ID of the host interface.
- **delay** (string) - Optional - Update interval of the LLD rule.
- **filter** (object) - Optional - LLD rule filter object.
- **query_fields** (array) - Optional - Query fields for HTTP agent LLD rules.
- **headers** (array) - Optional - Headers for HTTP agent LLD rules.
- **preprocessing** (array) - Optional - LLD rule preprocessing options.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryrule.create",
    "params": {
        "name": "Filtered LLD rule",
        "key_": "lld",
        "hostid": "10116",
        "type": 0,
        "interfaceid": "13",
        "delay": "30s",
        "filter": {
            "evaltype": 3,
            "formula": "(A and B) and (C or D)",
            "conditions": [
                {"macro": "{#MACRO1}", "value": "@regex1", "formulaid": "A"},
                {"macro": "{#MACRO1}", "value": "@regex2", "formulaid": "B"},
                {"macro": "{#MACRO2}", "value": "@regex3", "formulaid": "C"},
                {"macro": "{#MACRO2}", "value": "@regex4", "formulaid": "D"}
            ]
        }
    },
    "id": 1
}

### Response
#### Success Response (200)
- **itemids** (array) - Returns an array of IDs of the created LLD rules.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": ["27665"]
    },
    "id": 1
}
<!-- method: discoveryrule.delete -->
## discoveryrule.delete

### Description
This method allows to delete LLD rules. This method is only available to Admin and Super admin user types.

### Parameters
- **lldRuleIds** (array) - Required - IDs of the LLD rules to delete.

### Return values
- **ruleids** (array) - Returns an object containing the IDs of the deleted LLD rules.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryrule.delete",
    "params": [
        "27665",
        "27668"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "ruleids": [
            "27665",
            "27668"
        ]
    },
    "id": 1
}
<!-- method: discoveryrule.get -->
## discoveryrule.get

### Description
Retrieves LLD rules based on the provided parameters. This method supports filtering by item IDs, host IDs, or specific rule attributes.

### Parameters
- **itemids** (array) - Optional - Return only LLD rules with the given IDs.
- **hostids** (array/string) - Optional - Return only LLD rules that belong to the given hosts.
- **filter** (object) - Optional - Return only results that exactly match the given filter (e.g., type, url).
- **output** (array/string) - Optional - Specifies the object properties to return.
- **selectFilter** (string) - Optional - Return the filter object for the LLD rule.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryrule.get",
    "params": {
        "output": ["name"],
        "selectFilter": "extend",
        "itemids": ["24681"]
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (array) - Returns an array of LLD rule objects.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "itemid": "24681",
            "name": "Filtered LLD rule",
            "filter": {
                "evaltype": "1",
                "formula": "",
                "conditions": [],
                "eval_formula": "A and B and C and D"
            }
        }
    ],
    "id": 1
}
<!-- method: discoveryrule.update -->
## discoveryrule.update

### Description
Updates existing LLD rules. The itemid property must be defined for each LLD rule, and only the passed properties will be updated.

### Parameters
- **lldRules** (object/array) - Required - LLD rule properties to be updated.
  - **itemid** (string) - Required - ID of the LLD rule.
  - **filter** (object) - Optional - LLD rule filter to replace the existing filter.
  - **preprocessing** (object/array) - Optional - LLD rule preprocessing options to replace the existing preprocessing options.
  - **lld_macro_paths** (object/array) - Optional - LLD rule lld_macro_path options to replace the existing lld_macro_path options.
  - **overrides** (object/array) - Optional - LLD rule overrides options to replace the existing overrides options.

### Return values
- **itemids** (array) - Returns an object containing the IDs of the updated LLD rules.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryrule.update",
    "params": {
        "itemid": "22450",
        "filter": {
            "evaltype": 1,
            "conditions": [
                {
                    "macro": "{#FSTYPE}",
                    "value": "@File systems for discovery"
                }
            ]
        }
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "22450"
        ]
    },
    "id": 1
}
<!-- method: discoveryruleprototype.create -->
## discoveryruleprototype.create

### Description
This method allows to create new LLD rule prototypes. This method is only available to Admin and Super admin user types.

### Parameters
- **lldRules** (object/array) - Required - LLD rule prototypes to create.
- **filter** (object) - Optional - LLD rule prototype filter for the LLD rule.
- **preprocessing** (object/array) - Optional - LLD rule prototype preprocessing options.
- **lld_macro_paths** (object/array) - Optional - LLD rule prototype lld_macro_path options.
- **overrides** (object/array) - Optional - LLD rule prototype overrides options.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryruleprototype.create",
    "params": {
        "name": "Discover tablespaces for {#DB}",
        "key_": "db.tablespace.discovery[{#DB}]",
        "hostid": "10084",
        "ruleid": "47251",
        "type": 23
    },
    "id": 1
}

### Response
#### Success Response (200)
- **itemids** (array) - Returns an object containing the IDs of the created LLD rule prototypes.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "47252"
        ]
    },
    "id": 1
}
<!-- method: discoveryruleprototype.get -->
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
<!-- method: discoveryruleprototype.update -->
## discoveryruleprototype.update

### Description
This method allows to update existing LLD rule prototypes. Note that the updating of already discovered prototypes is limited. This method is only available to Admin and Super admin user types.

### Parameters
- **lldRules** (object/array) - Required - LLD rule prototype properties to be updated. The itemid property must be defined for each LLD rule prototype.
- **filter** (object) - Optional - LLD rule prototype filter to replace the existing filter.
- **preprocessing** (object/array) - Optional - LLD rule prototype preprocessing options to replace the existing preprocessing options.
- **lld_macro_paths** (object/array) - Optional - LLD rule prototype lld_macro_path options to replace the existing lld_macro_path options.
- **overrides** (object/array) - Optional - LLD rule prototype overrides options to replace the existing overrides options.

### Return values
- **itemids** (object) - Returns an object containing the IDs of the updated LLD rule prototypes.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "discoveryruleprototype.update",
    "params": {
        "itemid": "47253",
        "preprocessing": [
            {
                "type": 12,
                "params": "$.tablespaces",
                "error_handler": 1
            }
        ]
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "47253"
        ]
    },
    "id": 1
}
<!-- method: drule.delete -->
## drule.delete

### Description
Deletes a discovery rule.
<!-- method: event.acknowledge -->
## event.acknowledge

### Description
This method allows you to update events, such as closing, acknowledging, unacknowledging, adding messages, changing severity, suppressing, or changing event rank.

### Parameters
- **eventids** (ID/array) - Required - IDs of the events to acknowledge.
- **action** (integer) - Required - Event update action(s) as a bitmask (e.g., 1 - close, 4 - add message, 6 - acknowledge, 8 - change severity, 16 - unacknowledge, 32 - suppress, 64 - unsuppress, 128 - rank to cause, 256 - rank to symptom).
- **cause_eventid** (ID) - Required if action contains 256 - Cause event ID.
- **message** (string) - Required if action contains 4 - Text of the message.
- **severity** (integer) - Required if action contains 8 - New severity (0-5).
- **suppress_until** (integer) - Required if action contains 32 - Unix timestamp for suppression end (0 for indefinite).

### Return values
- **eventids** (array) - IDs of the updated events.
<!-- method: event.get -->
## event.get

## JSON-RPC event.get

### Description
Retrieves events based on the provided parameters, such as object IDs.

### Request Parameters
- **output** (string) - Specifies the output properties to return.
- **selectAcknowledges** (string) - Specifies whether to include acknowledgment data.
- **selectSuppressionData** (string) - Specifies whether to include suppression data.
- **selectTags** (string) - Specifies whether to include event tags.
- **objectids** (string) - The ID of the object (e.g., trigger) to filter events by.
- **sortfield** (array) - Fields to sort the results by.
- **sortorder** (string) - The order of sorting (e.g., DESC).

### Request Example
{
    "jsonrpc": "2.0",
    "method": "event.get",
    "params": {
        "output": "extend",
        "selectAcknowledges": "extend",
        "selectSuppressionData": "extend",
        "selectTags": "extend",
        "objectids": "22395",
        "sortfield": ["clock", "eventid"],
        "sortorder": "DESC"
    },
    "id": 1
}

### Response
#### Success Response
- **result** (array) - A list of event objects matching the criteria.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "eventid": "20",
            "name": "Load average is too high",
            "tags": []
        }
    ],
    "id": 1
}
<!-- method: graph.create -->
## graph.create

### Description
Creates a new graph.

### Method
JSON-RPC

### Parameters
- **Graph object** (object) - Required - The graph object to create.
<!-- method: graphitem.get -->
## graphitem.get

### Description
Retrieves graph items.
<!-- method: graphprototype.create -->
## graphprototype.create

### Description
Creates a new graph prototype.
<!-- method: graphprototype.delete -->
## graphprototype.delete

### Description
This method allows to delete graph prototypes. This method is only available to Admin and Super admin user types.

### Parameters
- **graphPrototypeIds** (array) - Required - IDs of the graph prototypes to delete.

### Return values
- **graphids** (array) - Returns an object containing the IDs of the deleted graph prototypes.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "graphprototype.delete",
    "params": [
        "652",
        "653"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "graphids": [
            "652",
            "653"
        ]
    },
    "id": 1
}
<!-- method: graphprototype.get -->
## graphprototype.get

### Description
The method allows to retrieve graph prototypes according to the given parameters.

### Parameters
- **discoveryids** (ID/array) - Optional - Return only graph prototypes that belong to the given discovery rules.
- **graphids** (ID/array) - Optional - Return only graph prototypes with the given IDs.
- **groupids** (ID/array) - Optional - Return only graph prototypes that belong to hosts or templates in the given host groups or template groups.
- **hostids** (ID/array) - Optional - Return only graph prototypes that belong to the given hosts.
- **inherited** (boolean) - Optional - If set to true return only graph prototypes inherited from a template.
- **itemids** (ID/array) - Optional - Return only graph prototypes that contain the given item prototypes.
- **templated** (boolean) - Optional - If set to true return only graph prototypes that belong to templates.
- **templateids** (ID/array) - Optional - Return only graph prototypes that belong to the given templates.
- **selectDiscoveryData** (query) - Optional - Return a discoveryData property with the graph prototype discovery object data.
- **selectDiscoveryRule** (query) - Optional - Return a discoveryRule property with the LLD rule that the graph prototype belongs to.
- **selectDiscoveryRulePrototype** (query) - Optional - Return a discoveryRulePrototype property with the parent LLD rule prototype that the graph prototype belongs to.
- **selectGraphItems** (query) - Optional - Return a gitems property with the graph items used in the graph prototype.
- **selectHostGroups** (query) - Optional - Return a hostgroups property with the host groups that the graph prototype belongs to.
- **selectHosts** (query) - Optional - Return a hosts property with the hosts that the graph prototype belongs to.
- **selectItems** (query) - Optional - Return an items property with the items and item prototypes used in the graph prototype.
- **selectTemplateGroups** (query) - Optional - Return a templategroups property with the template groups that the graph prototype belongs to.
- **selectTemplates** (query) - Optional - Return a templates property with the templates that the graph prototype belongs to.
- **filter** (object) - Optional - Return only those results that exactly match the given filter.
- **sortfield** (string/array) - Optional - Sort the result by the given properties.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "graphprototype.get",
    "params": {
        "output": "extend",
        "discoveryids": "27426"
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (array) - Returns an array of graph prototype objects or the count of objects if countOutput is used.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "graphid": "1017",
            "name": "Disk space usage {#FSNAME}",
            "width": "600",
            "height": "340",
            "templateid": "442",
            "graphtype": "2",
            "flags": "2"
        }
    ],
    "id": 1
}
<!-- method: graphprototype.update -->
## graphprototype.update

### Description
Updates existing graph prototypes. This method is restricted to Admin and Super admin user types.

### Parameters
- **graphPrototypes** (object/array) - Required - Graph prototype properties to be updated. The `graphid` property must be defined for each object.
- **gitems** (array) - Optional - Graph items to replace existing ones. If `gitemid` is provided, the item is updated; otherwise, a new item is created.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "graphprototype.update",
    "params": {
        "graphid": "439",
        "width": 1100,
        "height": 400
    },
    "id": 1
}

### Response
#### Success Response (200)
- **graphids** (array) - IDs of the updated graph prototypes.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "graphids": [
            "439"
        ]
    },
    "id": 1
}
<!-- method: hanode.get -->
## hanode.get

### Description
The hanode.get method allows for the retrieval of High availability node objects from the Zabbix server.

### Parameters
- **output** (query/body) - Optional - Specifies the properties to return.
- **ha_nodeids** (query/body) - Optional - Filter by specific node IDs.
- **sortfield** (query/body) - Optional - Sort the results by the given property.
<!-- method: history.clear -->
## history.clear

### Description
This method allows to clear item history. This method is only available to Admin and Super admin user types.

### Parameters
- **itemids** (array) - Required - IDs of items to clear.

### Return values
- **itemids** (array) - Returns an object containing the IDs of the cleared items.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "history.clear",
    "params": [
        "10325",
        "13205"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "10325",
            "13205"
        ]
    },
    "id": 1
}
<!-- method: history.get -->
## history.get

### Description
The method allows to retrieve history data according to the given parameters. This method may return historical data of a deleted entity if this data has not been removed by the housekeeper yet.

### Parameters
- **history** (integer) - Optional - History object types to return (0: numeric float, 1: character, 2: log, 3: numeric unsigned, 4: text, 5: binary).
- **hostids** (ID/array) - Optional - Return only history from the given hosts.
- **itemids** (ID/array) - Optional - Return only history from the given items.
- **time_from** (timestamp) - Optional - Return only values received after or at the given time.
- **time_till** (timestamp) - Optional - Return only values received before or at the given time.
- **sortfield** (string/array) - Optional - Sort the result by properties (itemid, clock, ns).
- **search** (object) - Optional - Return results that match the given pattern.
- **countOutput** (boolean) - Optional - Return the count of retrieved objects.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "history.get",
    "params": {
        "output": "extend",
        "history": 0,
        "itemids": "23296",
        "sortfield": "clock",
        "sortorder": "DESC",
        "limit": 10
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (array/integer) - Returns an array of objects or the count of retrieved objects.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "itemid": "23296",
            "clock": "1351090996",
            "value": "0.085",
            "ns": "563157632"
        }
    ],
    "id": 1
}
<!-- method: history.push -->
## history.push

### Description
Sends item history data to the Zabbix server. This method can be called by users of any type, provided they have the necessary permissions.

### Parameters
- **itemid** (ID) - Required if host and key are not set - ID of the related item.
- **host** (string) - Required if itemid is not set - Technical name of the host.
- **key** (string) - Required if itemid is not set - Item key.
- **value** (mixed) - Required - Item value.
- **clock** (timestamp) - Optional - Time when the value was received.
- **ns** (integer) - Optional - Nanoseconds when the value was received.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "history.push",
    "params": [
        {
            "itemid": 10600,
            "value": 0.5,
            "clock": 1690891294,
            "ns": 45440940
        }
    ],
    "id": 1
}

### Response
#### Success Response (200)
- **response** (string) - Status of the operation.
- **data** (array) - List of results for each item processed.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "response": "success",
        "data": [
            {
                "itemid": "10600"
            }
        ]
    },
    "id": 1
}
<!-- method: host.create -->
## host.create

### Description
This method allows to create a new host.

### Parameters
- **host** (string) - Required - Technical name of the host.
- **interfaces** (array) - Optional - Host interfaces to be created for the host.
- **groups** (array) - Required - Host groups to add the host to.
- **tags** (array) - Optional - Host tags.
- **templates** (array) - Optional - Templates to link to the host.
- **macros** (array) - Optional - User macros to create for the host.
- **inventory_mode** (integer) - Optional - Host inventory mode.
- **inventory** (object) - Optional - Host inventory properties.
- **tls_accept** (integer) - Optional - Connections from host.
- **tls_connect** (integer) - Optional - Connections to host.
- **tls_psk_identity** (string) - Optional - PSK identity.
- **tls_psk** (string) - Optional - PSK.
- **monitored_by** (integer) - Optional - Monitoring mode (0 - server, 1 - proxy, 2 - proxy group).
- **proxyid** (id) - Optional - ID of the proxy.
- **proxy_groupid** (id) - Optional - ID of the proxy group.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "Linux server",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.3.1",
                "port": "10050"
            }
        ],
        "groups": [
            { "groupid": "50" }
        ]
    },
    "id": 1
}

### Response
#### Success Response (200)
- **hostids** (array) - Returns an array of IDs of the created hosts.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "hostids": ["107819"]
    },
    "id": 1
}
<!-- method: host.delete -->
## host.delete

### Description
Deletes hosts from the Zabbix system.
<!-- method: host.get -->
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
<!-- method: host.massremove -->
## host.massremove

### Description
This method allows to remove related objects from multiple hosts. This method is only available to Admin and Super admin user types.

### Parameters
- **hostids** (ID/array) - Required - IDs of the hosts to be updated.
- **groupids** (ID/array) - Optional - IDs of the host groups to remove the given hosts from.
- **interfaces** (object/array) - Optional - Host interfaces to remove from the given hosts. The host interface object must have only the ip, dns and port properties defined.
- **macros** (string/array) - Optional - User macros to delete from the given hosts.
- **templateids** (ID/array) - Optional - IDs of the templates to unlink from the given hosts.
- **templateids_clear** (ID/array) - Optional - IDs of the templates to unlink and clear from the given hosts.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "host.massremove",
    "params": {
        "hostids": ["69665", "69666"],
        "templateids_clear": "325"
    },
    "id": 1
}

### Response
#### Success Response (200)
- **hostids** (array) - IDs of the updated hosts.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "hostids": [
            "69665",
            "69666"
        ]
    },
    "id": 1
}
<!-- method: host.massupdate -->
## host.massupdate

### Description
This method allows to simultaneously replace or remove related objects and update properties on multiple hosts. This method is only available to Admin and Super admin user types.

### Parameters
- **hosts** (object/array) - Required - Hosts to be updated. The hosts must have only the hostid property defined.
- **groups** (object/array) - Optional - Host groups to replace the current host groups the hosts belong to. The host groups must have only the groupid property defined.
- **interfaces** (object/array) - Optional - Host interfaces to replace the current host interfaces on the given hosts.
- **inventory** (object) - Optional - Host inventory properties.
- **macros** (object/array) - Optional - User macros to replace the current user macros on the given hosts.
- **templates** (object/array) - Optional - Templates to replace the currently linked templates on the given hosts. The templates must have only the templateid property defined.
- **templates_clear** (object/array) - Optional - Templates to unlink and clear from the given hosts. The templates must have only the templateid property defined.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "host.massupdate",
    "params": {
        "hosts": [
            {
                "hostid": "69665"
            },
            {
                "hostid": "69666"
            }
        ],
        "status": 0
    },
    "id": 1
}

### Response
#### Success Response (200)
- **hostids** (array) - IDs of the updated hosts.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "hostids": [
            "69665",
            "69666"
        ]
    },
    "id": 1
}
<!-- method: host.update -->
## host.update

### Description
This method allows to update existing hosts. It is restricted to Admin and Super admin user types.

### Parameters
- **hosts** (object/array) - Required - Host properties to be updated. The `hostid` property must be defined for each host.

#### Additional Parameters
- **groups** (object/array) - Optional - Host groups to replace the current host groups.
- **interfaces** (object/array) - Optional - Host interfaces to replace the current host interfaces.
- **tags** (object/array) - Optional - Host tags to replace the current host tags.
- **inventory** (object) - Optional - Host inventory properties.
- **macros** (object/array) - Optional - User macros to replace the current user macros.
- **templates** (object/array) - Optional - Templates to replace the currently linked templates.
- **templates_clear** (object/array) - Optional - Templates to unlink and clear from the host.

### Return values
- **hostids** (object) - Returns an object containing the IDs of the updated hosts.
<!-- method: hostgroup.create -->
## hostgroup.create

### Description
Creates new host groups.
<!-- method: hostgroup.delete -->
## hostgroup.delete

### Description
Deletes host groups.
<!-- method: hostgroup.get -->
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
<!-- method: hostgroup.update -->
## hostgroup.update

### Description
Updates host groups.
<!-- method: hostinterface.create -->
## hostinterface.create

### Description
Creates new host interfaces.
<!-- method: hostinterface.delete -->
## hostinterface.delete

### Description
Deletes host interfaces.
<!-- method: hostinterface.get -->
## hostinterface.get

### Description
Retrieves host interfaces.
<!-- method: hostinterface.massremove -->
## hostinterface.massremove

### Description
This method allows to remove host interfaces from the given hosts. This method is only available to Admin and Super admin user types.

### Parameters
- **interfaces** (object/array) - Required - Host interfaces to remove from the given hosts. The object must have only the `ip`, `dns` and `port` properties defined.
- **hostids** (ID/array) - Required - IDs of the hosts to be updated.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "hostinterface.massremove",
    "params": {
        "hostids": [
            "30050",
            "30052"
        ],
        "interfaces": {
            "dns": "",
            "ip": "127.0.0.1",
            "port": "161"
        }
    },
    "id": 1
}

### Response
#### Success Response (200)
- **interfaceids** (array) - IDs of the deleted host interfaces.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "interfaceids": [
            "30069",
            "30070"
        ]
    },
    "id": 1
}
<!-- method: hostinterface.replacehostinterfaces -->
## hostinterface.replacehostinterfaces

{
    "jsonrpc": "2.0",
    "method": "hostinterface.replacehostinterfaces",
    "params": {
        "hostid": "30052",
        "interfaces": {
            "dns": "",
            "ip": "127.0.0.1",
            "main": 1,
            "port": "10050",
            "type": 1,
            "useip": 1
        }
    },
    "id": 1
}

{
    "jsonrpc": "2.0",
    "result": {
        "interfaceids": [
            "30081"
        ]
    },
    "id": 1
}
<!-- method: hostinterface.update -->
## hostinterface.update

### Description
Updates host interfaces.
<!-- method: hostprototype.create -->
## hostprototype.create

### Description
This method allows to create new host prototypes. It is restricted to Admin and Super admin user types.

### Parameters
- **hostPrototypes** (object/array) - Required - Host prototypes to create.
- **ruleid** (ID) - Required - ID of the LLD rule that the host prototype belongs to.
- **groupLinks** (array) - Optional - Group links to be created for the host prototype.
- **groupPrototypes** (array) - Optional - Group prototypes to be created for the host prototype.
- **macros** (object/array) - Optional - User macros to be created for the host prototype.
- **tags** (object/array) - Optional - Host prototype tags.
- **interfaces** (object/array) - Optional - Host prototype custom interfaces.
- **templates** (object/array) - Optional - Templates to be linked to the host prototype.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "hostprototype.create",
    "params": {
        "host": "{#VM.NAME}",
        "ruleid": "23542",
        "custom_interfaces": "1",
        "groupLinks": [
            {
                "groupid": "2"
            }
        ],
        "groupPrototypes": [
            {
                "name": "{#HV.NAME}"
            }
        ],
        "tags": [
            {
                "tag": "datacenter",
                "value": "{#DATACENTER.NAME}"
            }
        ],
        "interfaces": [
            {
                "main": "1",
                "type": "2",
                "useip": "1",
                "ip": "127.0.0.1",
                "dns": "",
                "port": "161",
                "details": {
                    "version": "2",
                    "bulk": "1",
                    "community": "{$SNMP_COMMUNITY}"
                }
            }
        ]
    },
    "id": 1
}

### Response
#### Success Response
- **hostids** (array) - IDs of the created host prototypes.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "hostids": [
            "10103"
        ]
    },
    "id": 1
}
<!-- method: hostprototype.delete -->
## hostprototype.delete

### Description
Deletes host prototypes.
<!-- method: hostprototype.get -->
## hostprototype.get

### Description
Retrieves host prototypes.
<!-- method: hostprototype.update -->
## hostprototype.update

### Description
Updates host prototypes.
<!-- method: housekeeping.update -->
## housekeeping.update

### Description
Updates existing housekeeping settings. This method is only available to Super admin user type.

### Parameters
- **housekeeping** (object) - Required - Housekeeping properties to be updated.

### Return values
- **result** (array) - Returns an array with the names of updated parameters.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "housekeeping.update",
    "params": {
        "hk_events_mode": "1",
        "hk_events_trigger": "200d",
        "hk_events_internal": "2d",
        "hk_events_discovery": "2d"
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        "hk_events_mode",
        "hk_events_trigger",
        "hk_events_internal",
        "hk_events_discovery"
    ],
    "id": 1
}
<!-- method: httptest.delete -->
## httptest.delete

### Description
This method allows to delete web scenarios. This method is only available to Admin and Super admin user types.

### Parameters
- **webScenarioIds** (array) - Required - IDs of the web scenarios to delete.

### Return values
- **httptestids** (array) - Returns an object containing the IDs of the deleted web scenarios.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "httptest.delete",
    "params": [
        "2",
        "3"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "httptestids": [
            "2",
            "3"
        ]
    },
    "id": 1
}
<!-- method: iconmap.create -->
## iconmap.create

### Description
Creates new icon maps.
<!-- method: iconmap.delete -->
## iconmap.delete

### Description
This method allows to delete icon maps. This method is only available to Super admin user type.

### Parameters
- **iconMapIds** (array) - Required - IDs of the icon maps to delete.

### Return values
- **iconmapids** (array) - Returns an object containing the IDs of the deleted icon maps.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "iconmap.delete",
    "params": [
        "2",
        "5"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "iconmapids": [
            "2",
            "5"
        ]
    },
    "id": 1
}
<!-- method: iconmap.get -->
## iconmap.get

### Description
Retrieves icon maps.
<!-- method: iconmap.update -->
## iconmap.update

### Description
Updates existing icon maps.
<!-- method: image.delete -->
## image.delete

{
    "jsonrpc": "2.0",
    "method": "image.delete",
    "params": [
        "188",
        "192"
    ],
    "id": 1
}

{
    "jsonrpc": "2.0",
    "result": {
        "imageids": [
            "188",
            "192"
        ]
    },
    "id": 1
}
<!-- method: image.update -->
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
<!-- method: item.create -->
## item.create

## POST /api_jsonrpc.php

### Description
Creates a new item on a host using the provided configuration parameters.

### Method
POST

### Endpoint
https://example.com/zabbix/api_jsonrpc.php

### Request Body
- **method** (string) - Required - "item.create"
- **params** (object) - Required - Item configuration (name, key_, hostid, type, value_type, interfaceid, delay)

### Request Example
{
    "jsonrpc": "2.0",
    "method": "item.create",
    "params": {
        "name": "Free disk space on /home/joe/",
        "key_": "vfs.fs.size[/home/joe/,free]",
        "hostid": "10084",
        "type": 0,
        "value_type": 3,
        "interfaceid": "1",
        "delay": 30
    },
    "id": 3
}
<!-- method: item.delete -->
## item.delete

### Description
This method allows to delete items. Web items cannot be deleted via the Zabbix API. This method is only available to Admin and Super admin user types.

### Parameters
- **itemIds** (array) - Required - IDs of the items to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "item.delete",
    "params": [
        "22982",
        "22986"
    ],
    "id": 1
}

### Response
#### Success Response
- **itemids** (array) - Returns an object containing the IDs of the deleted items.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "22982",
            "22986"
        ]
    },
    "id": 1
}
<!-- method: item.get -->
## item.get

### Description
Retrieves items matching the specified criteria, such as host IDs, trigger associations, and key patterns.

### Parameters
- **output** (string) - The output format of the result.
- **hostids** (string) - Filter by host ID.
- **with_triggers** (boolean) - If true, returns only items used in triggers.
- **search** (object) - Search criteria for item fields (e.g., key_).
- **sortfield** (string) - Field to sort the results by.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": "extend",
        "hostids": "10084",
        "with_triggers": true,
        "search": {
            "key_": "system.cpu"
        },
        "sortfield": "name"
    },
    "id": 1
}

### Response
#### Success Response
- **result** (array) - A list of item objects matching the criteria.
<!-- method: item.update -->
## item.update

### Description
This method allows to update existing items. Web items cannot be updated via the Zabbix API. This method is only available to Admin and Super admin user types.

### Parameters
- **items** (object/array) - Required - Item properties to be updated. The itemid property must be defined for each item.
- **preprocessing** (array) - Optional - Item preprocessing options to replace the current preprocessing options.
- **tags** (array) - Optional - Item tags.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "item.update",
    "params": {
        "itemid": "10092",
        "status": 0
    },
    "id": 1
}

### Response
#### Success Response (200)
- **itemids** (array) - IDs of the updated items.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "itemids": [
            "10092"
        ]
    },
    "id": 1
}
<!-- method: itemprototype.create -->
## itemprototype.create

### Description
Creates new item prototypes.
<!-- method: itemprototype.delete -->
## itemprototype.delete

### Description
This method allows to delete item prototypes. This method is only available to Admin and Super admin user types.

### Parameters
- **itemPrototypeIds** (array) - Required - IDs of the item prototypes to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "itemprototype.delete",
    "params": [
        "27352",
        "27356"
    ],
    "id": 1
}

### Response
#### Success Response
- **prototypeids** (array) - IDs of the deleted item prototypes.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "prototypeids": [
            "27352",
            "27356"
        ]
    },
    "id": 1
}
<!-- method: itemprototype.get -->
## itemprototype.get

### Description
Retrieves all item prototypes for a specific LLD rule ID.

### Parameters
- **output** (string) - Required - Specifies the output format (e.g., "extend").
- **discoveryids** (string) - Required - The ID of the LLD rule to retrieve prototypes for.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "itemprototype.get",
    "params": {
        "output": "extend",
        "discoveryids": "27426"
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (array) - A list of item prototype objects.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "itemid": "23077",
            "name": "Incoming network traffic on en0",
            "key_": "net.if.in[en0]"
        }
    ],
    "id": 1
}
<!-- method: itemprototype.update -->
## itemprototype.update

### Description
Updates existing item prototypes.
<!-- method: maintenance.delete -->
## maintenance.delete

### Description
This method allows to delete maintenance periods. This method is only available to Admin and Super admin user types.

### Parameters
- **maintenanceIds** (array) - Required - IDs of the maintenance periods to delete.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "maintenance.delete",
    "params": [
        "3",
        "1"
    ],
    "id": 1
}

### Response
#### Success Response
- **maintenanceids** (array) - IDs of the deleted maintenance periods.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "maintenanceids": [
            "3",
            "1"
        ]
    },
    "id": 1
}
<!-- method: map.delete -->
## map.delete

### Description
This method allows to delete maps. This method is available to users of any type.

### Parameters
- **mapIds** (array) - Required - IDs of the maps to delete.

### Return values
- **sysmapids** (array) - Returns an object containing the IDs of the deleted maps.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "map.delete",
    "params": [
        "12",
        "34"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "sysmapids": [
            "12",
            "34"
        ]
    },
    "id": 1
}
<!-- method: map.update -->
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
<!-- method: mediatype.delete -->
## mediatype.delete

{
    "jsonrpc": "2.0",
    "method": "mediatype.delete",
    "params": [
        "3",
        "5"
    ],
    "id": 1
}

{
    "jsonrpc": "2.0",
    "result": {
        "mediatypeids": [
            "3",
            "5"
        ]
    },
    "id": 1
}
<!-- method: mfa.create -->
## mfa.create

{
    "jsonrpc": "2.0",
    "method": "mfa.create",
    "params": {
        "type": 1,
        "name": "Zabbix TOTP",
        "hash_function": 1,
        "code_length": 6
    },
    "id": 1
}

{
    "jsonrpc": "2.0",
    "result": {
        "mfaids": [
            "1"
        ]
    },
    "id": 1
}
<!-- method: mfa.delete -->
## mfa.delete

{
    "jsonrpc": "2.0",
    "method": "mfa.delete",
    "params": [
        "2"
    ],
    "id": 1
}

{
    "jsonrpc": "2.0",
    "result": {
        "mfaids": [
            "2"
        ]
    },
    "id": 1
}
<!-- method: mfa.get -->
## mfa.get

{
    "jsonrpc": "2.0",
    "method": "mfa.get",
    "params": {
        "output": "extend",
        "search": {
            "name": "Zabbix"
        }
    },
    "id": 1
}

{
    "jsonrpc": "2.0",
    "result": [
        {
            "mfaid": "1",
            "type": "1",
            "name": "Zabbix TOTP 1",
            "hash_function": "1",
            "code_length": "6",
            "api_hostname": "",
            "clientid": ""
        },
        {
            "mfaid": "2",
            "type": "1",
            "name": "Zabbix TOTP 2",
            "hash_function": "3",
            "code_length": "8",
            "api_hostname": "",
            "clientid": ""
        }
    ],
    "id": 1
}
<!-- method: mfa.update -->
## mfa.update

{
    "jsonrpc": "2.0",
    "method": "mfa.update",
    "params": {
        "mfaid": "1",
        "hash_function": 3,
        "code_length": 8
    },
    "id": 1
}

{
    "jsonrpc": "2.0",
    "result": {
        "mfaids": [
            "1"
        ]
    },
    "id": 1
}
<!-- method: module.create -->
## module.create

### Description
Installs a new frontend module.

### Method
POST

### Endpoint
module.create
<!-- method: module.delete -->
## module.delete

### Description
Uninstalls modules.

### Method
POST

### Endpoint
module.delete
<!-- method: proxy.get -->
## proxy.get

### Description
The method allows to retrieve proxies according to the given parameters. This method is available to users of any type.

### Parameters
- **proxyids** (ID/array) - Optional - Return only proxies with the given IDs.
- **proxy_groupids** (ID/array) - Optional - Return only proxies that belong to the given proxy groups.
- **selectAssignedHosts** (query) - Optional - Return an assignedHosts property with the hosts assigned to the proxy. Supports count.
- **selectHosts** (query) - Optional - Return a hosts property with the hosts monitored by the proxy. Supports count.
- **selectProxyGroup** (query) - Optional - Return a proxyGroup property with the proxy group object.
- **sortfield** (string/array) - Optional - Sort the result by the given properties (proxyid, name, operating_mode).
- **countOutput** (boolean) - Optional - Return the count of retrieved objects.
- **editable** (boolean) - Optional
- **excludeSearch** (boolean) - Optional
- **filter** (object) - Optional
- **limit** (integer) - Optional
- **output** (query) - Optional
- **preservekeys** (boolean) - Optional
- **search** (object) - Optional
- **searchByAny** (boolean) - Optional
- **searchWildcardsEnabled** (boolean) - Optional
- **sortorder** (string/array) - Optional
- **startSearch** (boolean) - Optional

### Request Example
{
    "jsonrpc": "2.0",
    "method": "proxy.get",
    "params": {
        "output": "extend"
    },
    "id": 1
}

### Response
Returns an array of objects or the count of retrieved objects if countOutput is used.
<!-- method: proxy.update -->
## proxy.update

### Description
Updates existing proxy configurations. The `proxyid` property is required for each proxy being updated.

### Parameters
- **proxies** (object/array) - Required - Proxy properties to be updated.
- **hosts** (array) - Optional - Hosts to be monitored by the proxy. Must contain objects with `hostid` defined.

### Return values
- **proxyids** (array) - Returns an object containing the IDs of the updated proxies.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "proxy.update",
    "params": {
        "proxyid": "10293",
        "hosts": [
            { "hostid": "10294" },
            { "hostid": "10295" }
        ]
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "proxyids": ["10293"]
    },
    "id": 1
}
<!-- method: proxygroup.create -->
## proxygroup.create

### Description
Creates a new proxy group.
<!-- method: proxygroup.delete -->
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
<!-- method: proxygroup.get -->
## proxygroup.get

### Description
The method allows to retrieve proxy groups according to the given parameters. This method is available to users of any type.

### Parameters
- **proxy_groupids** (ID/array) - Optional - Return only proxy groups with the given IDs.
- **proxyids** (ID/array) - Optional - Return only proxy groups that contain the given proxies.
- **selectProxies** (query) - Optional - Return a proxies property with the proxies that belong to the proxy group.
- **sortfield** (string/array) - Optional - Sort the result by the given properties (proxy_groupid, name).
- **countOutput** (boolean) - Optional - Return the count of retrieved objects.
- **editable** (boolean) - Optional
- **excludeSearch** (boolean) - Optional
- **filter** (object) - Optional
- **limit** (integer) - Optional
- **output** (query) - Optional
- **preservekeys** (boolean) - Optional
- **search** (object) - Optional
- **searchByAny** (boolean) - Optional
- **searchWildcardsEnabled** (boolean) - Optional
- **sortorder** (string/array) - Optional
- **startSearch** (boolean) - Optional

### Request Example
{
    "jsonrpc": "2.0",
    "method": "proxygroup.get",
    "params": {
        "output": "extend",
        "selectProxies": ["proxyid", "name"]
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (integer/array) - Returns an array of objects or the count of retrieved objects.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "proxy_groupid": "1",
            "name": "Proxy group 1",
            "failover_delay": "1m",
            "min_online": "3",
            "description": "",
            "state": "1",
            "proxies": [
                {
                    "proxyid": "1",
                    "name": "proxy 1"
                },
                {
                    "proxyid": "2",
                    "name": "proxy 2"
                }
            ]
        }
    ],
    "id": 1
}
<!-- method: proxygroup.update -->
## proxygroup.update

### Description
Updates an existing proxy group.
<!-- method: regexp.create -->
## regexp.create

### Description
Allows to create new global regular expressions. This method is only available to Super admin user types.

### Parameters
- **regularExpressions** (object/array) - Required - Regular expressions to create.
- **expressions** (array) - Required - Expressions options.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "regexp.create",
    "params": {
      "name": "Storage devices for SNMP discovery",
      "test_string": "/boot",
      "expressions": [
        {
          "expression": "^(Physical memory|Virtual memory|Memory buffers|Cached memory|Swap space)$",
          "expression_type": "4",
          "case_sensitive": "1"
        }
      ]
    },
    "id": 1
}

### Response
#### Success Response
- **regexpids** (array) - IDs of the created regular expressions.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "regexpids": [
            "16"
        ]
    },
    "id": 1
}
<!-- method: regexp.delete -->
## regexp.delete

### Description
This method allows to delete global regular expressions. This method is only available to Super admin user types.

### Parameters
- **regexpids** (array) - Required - IDs of the regular expressions to delete.

### Return values
- **regexpids** (array) - Returns an object containing the IDs of the deleted regular expressions.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "regexp.delete",
    "params": [
        "16",
        "17"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "regexpids": [
            "16",
            "17"
        ]
    },
    "id": 1
}
<!-- method: regexp.update -->
## regexp.update

### Description
Updates regular expressions.
<!-- method: report.delete -->
## report.delete

### Description
Deletes scheduled reports.
<!-- method: report.update -->
## report.update

### Description
Update scheduled reports.
<!-- method: role.create -->
## role.create

### Description
This method allows to create new roles. This method is only available to Super admin user type.

### Parameters
- **roles** (object/array) - Required - Roles to create.
- **rules** (array) - Optional - Role rules to be created for the role.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "role.create",
    "params": {
        "name": "Operator",
        "type": "1",
        "rules": {
            "ui": [
                {
                    "name": "monitoring.hosts",
                    "status": "0"
                },
                {
                    "name": "monitoring.maps",
                    "status": "0"
                }
            ]
        }
    },
    "id": 1
}

### Response
#### Success Response
- **roleids** (array) - IDs of the created roles.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "roleids": [
            "5"
        ]
    },
    "id": 1
}
<!-- method: role.delete -->
## role.delete

### Description
Deletes existing user roles.
<!-- method: role.update -->
## role.update

### Description
Updates existing user roles.
<!-- method: script.getscriptsbyevents -->
## script.getscriptsbyevents

### Description
Retrieves all available scripts on the given event or a specific script if a script ID is provided. This method is available to all user types.

### Parameters
- **eventid** (ID) - Required - ID of the event to return scripts for.
- **scriptid** (ID) - Optional - ID of the script to return.
- **manualinput** (string) - Optional - Value of the user-provided {MANUALINPUT} macro.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "script.getscriptsbyevents",
    "params": [
      {
         "eventid": "632"
      },
      {
         "eventid": "614"
      }
    ],
    "id": 1
}

### Response
- **result** (object) - Returns an object with event IDs as properties and arrays of available scripts as values.
<!-- method: service.create -->
## service.create

### Description
This method allows to create new services. It is available to users of any type, subject to user role permissions.

### Parameters
- **services** (object/array) - Required - Services to create.
- **children** (array) - Optional - Child services to be linked to the service (must have serviceid defined).
- **parents** (array) - Optional - Parent services to be linked to the service (must have serviceid defined).
- **tags** (array) - Optional - Service tags to be created.
- **problem_tags** (array) - Optional - Problem tags to be created.
- **status_rules** (array) - Optional - Status rules to be created.

### Return values
- **serviceids** (array) - Returns an object containing the IDs of the created services.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "service.create",
    "params": {
        "name": "Server 1",
        "algorithm": 1,
        "sortorder": 1
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "serviceids": [
            "5"
        ]
    },
    "id": 1
}
<!-- method: service.delete -->
## service.delete

### Description
Deletes an existing service.

### Method
JSON-RPC
<!-- method: settings.get -->
## settings.get

{
    "jsonrpc": "2.0",
    "method": "settings.get",
    "params": {
        "output": "extend"
    },
    "id": 1
}

{
    "jsonrpc": "2.0",
    "result": {
        "default_theme": "blue-theme",
        "search_limit": "1000",
        "max_in_table": "50",
        "server_check_interval": "10",
        "work_period": "1-5,09:00-18:00",
        "show_technical_errors": "0",
        "history_period": "24h",
        "period_default": "1h",
        "max_period": "2y",
        "severity_color_0": "97AAB3",
        "severity_color_1": "7499FF",
        "severity_color_2": "FFC859",
        "severity_color_3": "FFA059",
        "severity_color_4": "E97659",
        "severity_color_5": "E45959",
        "severity_name_0": "Not classified",
        "severity_name_1": "Information",
        "severity_name_2": "Warning",
        "severity_name_3": "Average",
        "severity_name_4": "High",
        "severity_name_5": "Disaster",
        "custom_color": "0",
        "ok_period": "5m",
        "blink_period": "2m",
        "problem_unack_color": "CC0000",
        "problem_ack_color": "CC0000",
        "ok_unack_color": "009900",
        "ok_ack_color": "009900",
        "problem_unack_style": "1",
        "problem_ack_style": "1",
        "ok_unack_style": "1",
        "ok_ack_style": "1",
        "discovery_groupid": "5",
        "default_inventory_mode": "-1",
        "alert_usrgrpid": "7",
        "snmptrap_logging": "1",
        "default_lang": "en_US",
        "default_timezone": "system",
        "login_attempts": "5",
        "login_block": "30s",
        "validate_uri_schemes": "1",
        "uri_valid_schemes": "http,https,ftp,file,mailto,tel,ssh",
        "x_frame_options": "SAMEORIGIN",
        "iframe_sandboxing_enabled": "1",
        "iframe_sandboxing_exceptions": "",
        "max_overview_table_size": "50",
        "connect_timeout": "3s",
        "socket_timeout": "3s",
        "media_type_test_timeout": "65s",
        "script_timeout": "60s",
        "item_test_timeout": "60s",
        "url": "",
        "report_test_timeout": "60s",
        "auditlog_enabled": "1",
        "auditlog_mode": "1",
        "ha_failover_delay": "1m",
        "geomaps_tile_provider": "OpenStreetMap.Mapnik",
        "geomaps_tile_url": "",
        "geomaps_max_zoom": "0",
        "geomaps_attribution": "",
        "vault_provider": "0",
        "timeout_zabbix_agent": "3s",
        "timeout_simple_check": "3s",
        "timeout_snmp_agent": "3s",
        "timeout_external_check": "3s",
        "timeout_db_monitor": "3s",
        "timeout_http_agent": "3s",
        "timeout_ssh_agent": "3s",
        "timeout_telnet_agent": "3s",
        "timeout_script": "3s"
    },
    "id": 1
}
<!-- method: sla.delete -->
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
<!-- method: sla.update -->
## sla.update

### Description
Updates existing SLA entries. This method is restricted to Admin and Super admin user types.

### Parameters
- **slaids** (object/array) - Required - SLA properties to be updated. The 'slaid' property must be defined for each SLA.
- **service_tags** (array) - Optional - SLA service tags to replace the current ones.
- **schedule** (array) - Optional - SLA schedule to replace the current one. An empty array sets the schedule to 24x7.
- **excluded_downtimes** (array) - Optional - SLA excluded downtimes to replace the current ones.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "sla.update",
    "params": [
        {
            "slaid": "5",
            "name": "NoSQL Database engines",
            "slo": "95",
            "period": 2,
            "service_tags": [
                {
                    "tag": "database",
                    "operator": "0",
                    "value": "redis"
                }
            ]
        }
    ],
    "id": 1
}

### Response
#### Success Response (200)
- **slaids** (array) - IDs of the updated SLAs.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "slaids": [
            "5"
        ]
    },
    "id": 1
}
<!-- method: task.create -->
## task.create

### Description
Creates new tasks, such as executing item checks or refreshing proxy configurations immediately.

### Method
JSON-RPC

### Parameters
- **tasks** (array) - Required - The list of task objects to create.
<!-- method: task.get -->
## task.get

### Description
The method allows to retrieve tasks according to the given parameters. This method is only available to Super admin user type.

### Parameters
- **taskids** (ID/array) - Optional - Return only tasks with the given IDs.
- **output** (query) - Optional - These parameters are described in the reference commentary.
- **preservekeys** (boolean) - Optional

### Request Example
{
    "jsonrpc": "2.0",
    "method": "task.get",
    "params": {
        "output": "extend",
        "taskids": "1"
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (array) - Returns an array of task objects.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "taskid": "1",
            "type": "7",
            "status": "3",
            "clock": "1601039076",
            "ttl": "3600",
            "proxyid": null,
            "request": {},
            "result": {}
        }
    ],
    "id": 1
}
<!-- method: template.delete -->
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
<!-- method: template.get -->
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
<!-- method: template.massremove -->
## template.massremove

### Description
Removes related objects from templates.
<!-- method: templatedashboard.create -->
## templatedashboard.create

### Description
This method allows to create new template dashboards. This method is only available to Admin and Super admin user types.

### Parameters
- **templateDashboards** (object/array) - Required - Template dashboards to create.
- **pages** (array) - Required - Template dashboard pages to be created for the dashboard.

### Return values
- **dashboardids** (object) - Returns an object containing the IDs of the created template dashboards.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templatedashboard.create",
    "params": {
        "templateid": "10318",
        "name": "Graphs",
        "pages": [
            {
                "widgets": [
                    {
                        "type": "graph",
                        "x": 0,
                        "y": 0,
                        "width": 12,
                        "height": 5,
                        "view_mode": 0,
                        "fields": [
                            {
                                "type": 6,
                                "name": "graphid",
                                "value": "1123"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "dashboardids": [
            "32"
        ]
    },
    "id": 1
}
<!-- method: templatedashboard.delete -->
## templatedashboard.delete

### Description
This method allows to delete template dashboards. This method is only available to Admin and Super admin user types.

### Parameters
- **templateDashboardIds** (array) - Required - IDs of the template dashboards to delete.

### Return values
- **dashboardids** (array) - Returns an object containing the IDs of the deleted template dashboards.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templatedashboard.delete",
    "params": [
        "45",
        "46"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "dashboardids": [
            "45",
            "46"
        ]
    },
    "id": 1
}
<!-- method: templategroup.create -->
## templategroup.create

### Description
This method allows to create new template groups. This method is only available to Super admin user type.

### Parameters
- **templateGroups** (object/array) - Required - Template groups to create. The method accepts template groups with the standard template group properties.

### Return values
- **groupids** (object) - Returns an object containing the IDs of the created template groups.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templategroup.create",
    "params": {
        "name": "Templates/Databases"
    },
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "groupids": [
            "107820"
        ]
    },
    "id": 1
}
<!-- method: templategroup.delete -->
## templategroup.delete

### Description
This method allows to delete template groups. A template group cannot be deleted if it contains templates that belong to this group only. This method is only available to Admin and Super admin user types.

### Parameters
- **templateGroupIds** (array) - Required - IDs of the template groups to delete.

### Return values
- **groupids** (array) - Returns an object containing the IDs of the deleted template groups.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templategroup.delete",
    "params": [
        "107814",
        "107815"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "groupids": [
            "107814",
            "107815"
        ]
    },
    "id": 1
}
<!-- method: templategroup.get -->
## templategroup.get

### Description
The method allows to retrieve template groups according to the given parameters.

### Parameters
- **graphids** (ID/array) - Optional - Return only template groups that contain templates with the given graphs.
- **groupids** (ID/array) - Optional - Return only template groups with the given template group IDs.
- **templateids** (ID/array) - Optional - Return only template groups that contain the given templates.
- **triggerids** (ID/array) - Optional - Return only template groups that contain templates with the given triggers.
- **with_graphs** (boolean) - Optional - Return only template groups that contain templates with graphs.
- **with_graph_prototypes** (boolean) - Optional - Return only template groups that contain templates with graph prototypes.
- **with_httptests** (boolean) - Optional - Return only template groups that contain templates with web checks.
- **with_items** (boolean) - Optional - Return only template groups that contain templates with items.
- **with_item_prototypes** (boolean) - Optional - Return only template groups that contain templates with item prototypes.
- **with_simple_graph_item_prototypes** (boolean) - Optional - Return only template groups that contain templates with item prototypes, which are enabled for creation and have numeric type of information.
- **with_simple_graph_items** (boolean) - Optional - Return only template groups that contain templates with numeric items.
- **with_templates** (boolean) - Optional - Return only template groups that contain templates.
- **with_triggers** (boolean) - Optional - Return only template groups that contain templates with triggers.
- **selectTemplates** (query) - Optional - Return a templates property with the templates that belong to the template group.
- **limitSelects** (integer) - Optional - Limits the number of records returned by subselects.
- **sortfield** (string/array) - Optional - Sort the result by the given properties (groupid, name).

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templategroup.get",
    "params": {
        "output": "extend",
        "filter": {
            "name": [
                "Templates/Databases",
                "Templates/Modules"
            ]
        }
    },
    "id": 1
}

### Response
#### Success Response (200)
- **result** (integer/array) - Returns an array of objects or the count of retrieved objects.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": [
        {
            "groupid": "13",
            "name": "Templates/Databases",
            "uuid": "748ad4d098d447d492bb935c907f652f"
        },
        {
            "groupid": "8",
            "name": "Templates/Modules",
            "uuid": "57b7ae836ca64446ba2c296389c009b7"
        }
    ],
    "id": 1
}
<!-- method: templategroup.massadd -->
## templategroup.massadd

### Description
Adds related objects to multiple template groups.
<!-- method: templategroup.massremove -->
## templategroup.massremove

### Description
Removes related objects from template groups.
<!-- method: templategroup.massupdate -->
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
<!-- method: templategroup.propagate -->
## templategroup.propagate

### Description
This method allows to apply permissions to all template groups' subgroups. This method is only available to Super admin user types.

### Parameters
- **groups** (object/array) - Required - Template groups to propagate. Must have only the groupid property defined.
- **permissions** (boolean) - Required - Set true if need to propagate permissions.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templategroup.propagate",
    "params": {
        "groups": [
            {
                "groupid": "15"
            }
        ],
        "permissions": true
    },
    "id": 1
}

### Response
#### Success Response (200)
- **groupids** (array) - IDs of the propagated template groups.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "groupids": [
            "15"
        ]
    },
    "id": 1
}
<!-- method: templategroup.update -->
## templategroup.update

### Description
Updates existing template groups. Only the provided properties are updated; others remain unchanged.

### Parameters
- **templateGroups** (object/array) - Required - Template group properties to be updated. The `groupid` property must be defined for each template group.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "templategroup.update",
    "params": {
        "groupid": "7",
        "name": "Templates/Databases"
    },
    "id": 1
}

### Response
#### Success Response
- **groupids** (array) - IDs of the updated template groups.

#### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "groupids": [
            "7"
        ]
    },
    "id": 1
}
<!-- method: token.delete -->
## token.delete

### Description
This method allows to delete tokens. The Manage API tokens permission is required for the user role to manage tokens for other users.

### Parameters
- **tokenids** (array) - Required - IDs of the tokens to delete.

### Return values
- **tokenids** (array) - Returns an object containing the IDs of the deleted tokens.

### Request Example
{
    "jsonrpc": "2.0",
    "method": "token.delete",
    "params": [
        "188",
        "192"
    ],
    "id": 1
}

### Response Example
{
    "jsonrpc": "2.0",
    "result": {
        "tokenids": [
            "188",
            "192"
        ]
    },
    "id": 1
}
