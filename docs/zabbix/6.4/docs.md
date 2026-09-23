<!-- Zabbix 6.4 API docs snapshot
     Source: zabbix.com official documentation
     Docs source: https://www.zabbix.com/documentation/6.4/en/manual/api
     Fetched: 2026-09-23T09:25:36+00:00
-->
<!-- method: action.create -->
## action.create

### Description
object action.create(object/array actions)
This method allows to create new actions.

### Parameters
(object/array) Actions to create.
Additionally to the standard action properties , the
method accepts the following parameters.

- **filter** (object): Action filter object for the action.
- **operations** (array): Action operations to create for the action.
- **recovery_operations** (array): Action recovery operations to create for the action.
- **update_operations** (array): Action update operations to create for the action.

### Return value
(object) Returns an object containing the IDs of the created actions
under the actionids property. The order of the returned IDs matches
the order of the passed actions.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/action/create

<!-- method: action.delete -->
## action.delete

### Description
object action.delete(array actionIds)
This method allows to delete actions.

### Parameters
(array) IDs of the actions to delete.

### Return value
(object) Returns an object containing the IDs of the deleted actions
under the actionids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/action/delete

<!-- method: action.get -->
## action.get

### Description
integer/array action.get(object parameters)
The method allows to retrieve actions according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **actionids** (string/array): Return only actions with the given IDs.
- **groupids** (string/array): Return only actions that use the given host groups in action conditions.
- **hostids** (string/array): Return only actions that use the given hosts in action conditions.
- **triggerids** (string/array): Return only actions that use the given triggers in action conditions.
- **mediatypeids** (string/array): Return only actions that use the given media types to send messages.
- **usrgrpids** (string/array): Return only actions that are configured to send messages to the given user groups.
- **userids** (string/array): Return only actions that are configured to send messages to the given users.
- **scriptids** (string/array): Return only actions that are configured to run the given scripts.
- **selectFilter** (query): Return a filter property with the action condition filter.
- **selectOperations** (query): Return an operations property with action operations.
- **selectRecoveryOperations** (query): Return a recovery_operations property with action recovery operations.
- **selectUpdateOperations** (query): Return an update_operations property with action update operations.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: actionid , name , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in the reference commentary .
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/action/get

<!-- method: action.update -->
## action.update

### Description
object action.update(object/array actions)
This method allows to update existing actions.

### Parameters
(object/array) Action properties to be updated.
The actionid property must be defined for each action, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard action properties , the
method accepts the following parameters.

- **filter** (object): Action filter object to replace the current filter.
- **operations** (array): Action operations to replace existing operations.
- **recovery_operations** (array): Action recovery operations to replace existing recovery operations. Parameter behavior : - supported if eventsource of Action object is set to "event created by a trigger", "internal event", or "event created on service status update"
- **update_operations** (array): Action update operations to replace existing update operations. Parameter behavior : - supported if eventsource of Action object is set to "event created by a trigger" or "event created on service status update"

### Return value
(object) Returns an object containing the IDs of the updated actions
under the actionids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/action/update

<!-- method: alert.get -->
## alert.get

### Description
integer/array alert.get(object parameters)
The method allows to retrieve alerts according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **alertids** (string/array): Return only alerts with the given IDs.
- **actionids** (string/array): Return only alerts generated by the given actions.
- **eventids** (string/array): Return only alerts generated by the given events.
- **groupids** (string/array): Return only alerts generated by objects from the given host groups.
- **hostids** (string/array): Return only alerts generated by objects from the given hosts.
- **mediatypeids** (string/array): Return only message alerts that used the given media types.
- **objectids** (string/array): Return only alerts generated by the given objects
- **userids** (string/array): Return only message alerts that were sent to the given users.
- **eventobject** (integer): Return only alerts generated by events related to objects of the given type. See event "object" for a list of supported object types. Default: 0 - trigger.
- **eventsource** (integer): Return only alerts generated by events of the given type. See event "source" for a list of supported event types. Default: 0 - trigger events.
- **time_from** (timestamp): Return only alerts that have been generated after the given time.
- **time_till** (timestamp): Return only alerts that have been generated before the given time.
- **selectHosts** (query): Return a hosts property with data of hosts that triggered the action operation.
- **selectMediatypes** (query): Return a mediatypes property with an array of the media types that were used for the message alert.
- **selectUsers** (query): Return a users property with an array of the users that the message was addressed to.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: alertid , clock , eventid , mediatypeid , sendto , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/alert/get

<!-- method: apiinfo.version -->
## apiinfo.version

### Description
string apiinfo.version(array)
This method allows to retrieve the version of the Zabbix API.

### Parameters
(array) The method accepts an empty array.

### Return value
(string) Returns the version of the Zabbix API.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/apiinfo/version

<!-- method: auditlog.get -->
## auditlog.get

### Description
integer/array auditlog.get(object parameters)
The method allows to retrieve audit log records according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **auditids** (string/array): Return only audit log with the given IDs.
- **userids** (string/array): Return only audit log that were created by the given users.
- **time_from** (timestamp): Returns only audit log entries that have been created after or at the given time.
- **time_till** (timestamp): Returns only audit log entries that have been created before or at the given time.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: auditid , userid , clock .
- **filter** (object): Return only results that exactly match the given filter. Accepts an array, where the keys are property names, and the values are either a single value or an array of values to match against.
- **search** (object): Case insensitive sub-string search in content of fields: username , ip , resourcename , details .
- **countOutput** (boolean): These parameters being common for all get methods are described in the reference commentary .
- **excludeSearch** (boolean)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/auditlog/get

<!-- method: authentication.get -->
## authentication.get

### Description
object authentication.get(object parameters)
The method allows to retrieve authentication object according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports only one parameter.

- **output** (query): This parameter being common for all get methods described in the reference commentary .

### Return value
(object) Returns authentication object.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/authentication/get

<!-- method: authentication.update -->
## authentication.update

### Description
object authentication.update(object authentication)
This method allows to update existing authentication settings.

### Parameters
(object) Authentication properties to be updated.

### Return value
(array) Returns an array with the names of updated parameters.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/authentication/update

<!-- method: autoregistration.get -->
## autoregistration.get

### Description
object autoregistration.get(object parameters)
The method allows to retrieve autoregistration object according to the
given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports only one parameter.

- **output** (query): This parameter being common for all get methods described in the reference commentary .

### Return value
(object) Returns autoregistration object.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/autoregistration/get

<!-- method: autoregistration.update -->
## autoregistration.update

### Description
object autoregistration.update(object autoregistration)
This method allows to update existing autoregistration.

### Parameters
(object) Autoregistration properties to be updated.

### Return value
(boolean ) Returns boolean true as result on successful update.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/autoregistration/update

<!-- method: configuration.export -->
## configuration.export

### Description
string configuration.export(object parameters)
This method allows to export configuration data as a serialized string.

### Parameters
(object) Parameters defining the objects to be exported and the format to use.

- **format** (string): Format in which the data must be exported. Possible values: yaml - YAML; xml - XML; json - JSON; raw - unprocessed PHP array. Parameter behavior : - required
- **prettyprint** (boolean): Make the output more human readable by adding indentation. Possible values: true - add indentation; false - (default) do not add indentation.
- **options** (object): Objects to be exported. The options object has the following parameters: host_groups - (array) IDs of host groups to export; hosts - (array) IDs of hosts to export; images - (array) IDs of images to export; maps - (array) IDs of maps to export; mediaTypes - (array) IDs of media types to export; template_groups - (array) IDs of template groups to export; templates - (array) IDs of templates to export. Parameter behavior : - required

### Return value
(string) Returns a serialized string containing the requested configuration data.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/configuration/export

<!-- method: configuration.import -->
## configuration.import

### Description
boolean configuration.import(object parameters)
This method allows to import configuration data from a serialized string.

### Parameters
(object) Parameters containing the data to import and rules how the data should be handled.
The rules object supports the following parameters.

- **format** (string): Format of the serialized string. Possible values: yaml - YAML; xml - XML; json - JSON. Parameter behavior : - required
- **source** (string): Serialized string containing the configuration data. Parameter behavior : - required
- **rules** (object): Rules on how new and existing objects should be imported. The rules parameter is described in detail in the table below. Parameter behavior : - required
- **discoveryRules** (object): Rules on how to import LLD rules. Supported parameters: createMissing - (boolean) if set to true , new LLD rules will be created; default: false ; updateExisting - (boolean) if set to true , existing LLD rules will be updated; default: false ; deleteMissing - (boolean) if set to true , LLD rules not present in the imported data will be deleted from the database; default: false .
- **graphs** (object): Rules on how to import graphs. Supported parameters: createMissing - (boolean) if set to true , new graphs will be created; default: false ; updateExisting - (boolean) if set to true , existing graphs will be updated; default: false ; deleteMissing - (boolean) if set to true , graphs not present in the imported data will be deleted from the database; default: false .
- **host_groups** (object): Rules on how to import host groups. Supported parameters: createMissing - (boolean) if set to true , new host groups will be created; default: false ; updateExisting - (boolean) if set to true , existing host groups will be updated; default: false .
- **template_groups** (object): Rules on how to import template groups. Supported parameters: createMissing - (boolean) if set to true , new template groups will be created; default: false ; updateExisting - (boolean) if set to true , existing template groups will be updated; default: false .
- **hosts** (object): Rules on how to import hosts. Supported parameters: createMissing - (boolean) if set to true , new hosts will be created; default: false ; updateExisting - (boolean) if set to true , existing hosts will be updated; default: false .
- **httptests** (object): Rules on how to import web scenarios. Supported parameters: createMissing - (boolean) if set to true , new web scenarios will be created; default: false ; updateExisting - (boolean) if set to true , existing web scenarios will be updated; default: false ; deleteMissing - (boolean) if set to true , web scenarios not present in the imported data will be deleted from the database; default: false .
- **images** (object): Rules on how to import images. Supported parameters: createMissing - (boolean) if set to true , new images will be created; default: false ; updateExisting - (boolean) if set to true , existing images will be updated; default: false .
- **items** (object): Rules on how to import items. Supported parameters: createMissing - (boolean) if set to true , new items will be created; default: false ; updateExisting - (boolean) if set to true , existing items will be updated; default: false ; deleteMissing - (boolean) if set to true , items not present in the imported data will be deleted from the database; default: false .
- **maps** (object): Rules on how to import maps. Supported parameters: createMissing - (boolean) if set to true , new maps will be created; default: false ; updateExisting - (boolean) if set to true , existing maps will be updated; default: false .
- **mediaTypes** (object): Rules on how to import media types. Supported parameters: createMissing - (boolean) if set to true , new media types will be created; default: false ; updateExisting - (boolean) if set to true , existing media types will be updated; default: false .
- **templateLinkage** (object): Rules on how to import template links. Supported parameters: createMissing - (boolean) if set to true , templates that are not linked to the host or template being imported, but are present in the imported data, will be linked; default: false ; deleteMissing - (boolean) if set to true , templates that are linked to the host or template being imported, but are not present in the imported data, will be unlinked without removing entities (items, triggers, etc.) inherited from the unlinked templates; default: false .
- **templates** (object): Rules on how to import templates. Supported parameters: createMissing - (boolean) if set to true , new templates will be created; default: false ; updateExisting - (boolean) if set to true , existing templates will be updated; default: false .
- **templateDashboards** (object): Rules on how to import template dashboards. Supported parameters: createMissing - (boolean) if set to true , new template dashboards will be created; default: false ; updateExisting - (boolean) if set to true , existing template dashboards will be updated; default: false ; deleteMissing - (boolean) if set to true , template dashboards not present in the imported data will be deleted from the database; default: false .
- **triggers** (object): Rules on how to import triggers. Supported parameters: createMissing - (boolean) if set to true , new triggers will be created; default: false ; updateExisting - (boolean) if set to true , existing triggers will be updated; default: false ; deleteMissing - (boolean) if set to true , triggers not present in the imported data will be deleted from the database; default: false .
- **valueMaps** (object): Rules on how to import host or template value maps. Supported parameters: createMissing - (boolean) if set to true , new value maps will be created; default: false ; updateExisting - (boolean) if set to true , existing value maps will be updated; default: false ; deleteMissing - (boolean) if set to true , value maps not present in the imported data will be deleted from the database; default: false .

### Return value
(boolean) Returns true if importing has been successful.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/configuration/import

<!-- method: configuration.importcompare -->
## configuration.importcompare

### Description
array configuration.importcompare(object parameters)
This method allows to compare import file with current system elements and shows what will be changed if this import file will be imported.

### Parameters
(object) Parameters containing the possible data to import and rules how the data should be handled.
The rules object supports the following parameters.

- **format** (string): Format of the serialized string. Possible values: yaml - YAML; xml - XML; json - JSON. Parameter behavior : - required
- **source** (string): Serialized string containing the configuration data. Parameter behavior : - required
- **rules** (object): Rules on how new and existing objects should be compared. The rules parameter is described in detail in the table below. Parameter behavior : - required
- **discoveryRules** (object): Rules on how to import LLD rules. Supported parameters: createMissing - (boolean) if set to true , new LLD rules will be created; default: false ; updateExisting - (boolean) if set to true , existing LLD rules will be updated; default: false ; deleteMissing - (boolean) if set to true , LLD rules not present in the imported data will be deleted from the database; default: false .
- **graphs** (object): Rules on how to import graphs. Supported parameters: createMissing - (boolean) if set to true , new graphs will be created; default: false ; updateExisting - (boolean) if set to true , existing graphs will be updated; default: false ; deleteMissing - (boolean) if set to true , graphs not present in the imported data will be deleted from the database; default: false .
- **host_groups** (object): Rules on how to import host groups. Supported parameters: createMissing - (boolean) if set to true , new host groups will be created; default: false ; updateExisting - (boolean) if set to true , existing host groups will be updated; default: false .
- **template_groups** (object): Rules on how to import template groups. Supported parameters: createMissing - (boolean) if set to true , new template groups will be created; default: false ; updateExisting - (boolean) if set to true , existing template groups will be updated; default: false .
- **hosts** (object): Rules on how to import hosts. Supported parameters: createMissing - (boolean) if set to true , new hosts will be created; default: false ; updateExisting - (boolean) if set to true , existing hosts will be updated; default: false . This parameter will make no difference to the output. It is allowed only for consistency with configuration.import .
- **httptests** (object): Rules on how to import web scenarios. Supported parameters: createMissing - (boolean) if set to true , new web scenarios will be created; default: false ; updateExisting - (boolean) if set to true , existing web scenarios will be updated; default: false ; deleteMissing - (boolean) if set to true , web scenarios not present in the imported data will be deleted from the database; default: false .
- **images** (object): Rules on how to import images. Supported parameters: createMissing - (boolean) if set to true , new images will be created; default: false ; updateExisting - (boolean) if set to true , existing images will be updated; default: false . This parameter will make no difference to the output. It is allowed only for consistency with configuration.import .
- **items** (object): Rules on how to import items. Supported parameters: createMissing - (boolean) if set to true , new items will be created; default: false ; updateExisting - (boolean) if set to true , existing items will be updated; default: false ; deleteMissing - (boolean) if set to true , items not present in the imported data will be deleted from the database; default: false .
- **maps** (object): Rules on how to import maps. Supported parameters: createMissing - (boolean) if set to true , new maps will be created; default: false ; updateExisting - (boolean) if set to true , existing maps will be updated; default: false . This parameter will make no difference to the output. It is allowed only for consistency with configuration.import .
- **mediaTypes** (object): Rules on how to import media types. Supported parameters: createMissing - (boolean) if set to true , new media types will be created; default: false ; updateExisting - (boolean) if set to true , existing media types will be updated; default: false . This parameter will make no difference to the output. It is allowed only for consistency with configuration.import .
- **templateLinkage** (object): Rules on how to import template links. Supported parameters: createMissing - (boolean) if set to true , templates that are not linked to the host or template being imported, but are present in the imported data, will be linked; default: false ; deleteMissing - (boolean) if set to true , templates that are linked to the host or template being imported, but are not present in the imported data, will be unlinked without removing entities (items, triggers, etc.) inherited from the unlinked templates; default: false .
- **templates** (object): Rules on how to import templates. Supported parameters: createMissing - (boolean) if set to true , new templates will be created; default: false ; updateExisting - (boolean) if set to true , existing templates will be updated; default: false .
- **templateDashboards** (object): Rules on how to import template dashboards. Supported parameters: createMissing - (boolean) if set to true , new template dashboards will be created; default: false ; updateExisting - (boolean) if set to true , existing template dashboards will be updated; default: false ; deleteMissing - (boolean) if set to true , template dashboards not present in the imported data will be deleted from the database; default: false .
- **triggers** (object): Rules on how to import triggers. Supported parameters: createMissing - (boolean) if set to true , new triggers will be created; default: false ; updateExisting - (boolean) if set to true , existing triggers will be updated; default: false ; deleteMissing - (boolean) if set to true , triggers not present in the imported data will be deleted from the database; default: false .
- **valueMaps** (object): Rules on how to import host or template value maps. Supported parameters: createMissing - (boolean) if set to true , new value maps will be created; default: false ; updateExisting - (boolean) if set to true , existing value maps will be updated; default: false ; deleteMissing - (boolean) if set to true , value maps not present in the imported data will be deleted from the database; default: false .

### Return value
(array) Returns an array with changes in configuration, that will be made.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/configuration/importcompare

<!-- method: connector.create -->
## connector.create

### Description
object connector.create(object/array connectors)
This method allows to create new connector objects.

### Parameters
(object/array) Connector objects to create.
Additionally to the standard connector properties , the method accepts the following parameters.

- **tags** (array): Connector tag filter .

### Return value
(object) Returns an object containing the IDs of the created connectors under the connectorids property.
The order of the returned IDs matches the order of the passed connectors.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/connector/create

<!-- method: connector.delete -->
## connector.delete

### Description
object connector.delete(array connectorids)
This method allows to delete connector entries.

### Parameters
(array) IDs of the connectors to delete.

### Return value
(object) Returns an object containing the IDs of the deleted connectors under the connectorids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/connector/delete

<!-- method: connector.get -->
## connector.get

### Description
integer/array connector.get(object parameters)
The method allows to retrieve connector objects according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **connectorids** (string/array): Return only connectors with the given IDs.
- **selectTags** (query): Return a tags property with connector tag filter . Supports count .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: connectorid , name , data_type , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/connector/get

<!-- method: connector.update -->
## connector.update

### Description
object connector.update(object/array connectors)
This method allows to update existing connectors.

### Parameters
(object/array) Connector properties to be updated.
The connectorid property must be defined for each connector, all other properties are optional.
Only the passed properties will be updated, all others will remain unchanged.
Additionally to the standard connector properties , the method accepts the following parameters.

- **tags** (array): Connector tag filter to replace the current tag filter.

### Return value
(object) Returns an object containing the IDs of the updated connectors under the connectorids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/connector/update

<!-- method: correlation.create -->
## correlation.create

### Description
object correlation.create(object/array correlations)
This method allows to create new correlations.

### Parameters
(object/array) Correlations to create.
Additionally to the standard correlation
properties , the method accepts the following
parameters.

- **operations** (array): Correlation operations to create for the correlation. Parameter behavior : - required
- **filter** (object): Correlation filter object for the correlation. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the created
correlations under the correlationids property. The order of the
returned IDs matches the order of the passed correlations.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/correlation/create

<!-- method: correlation.delete -->
## correlation.delete

### Description
object correlation.delete(array correlationids)
This method allows to delete correlations.

### Parameters
(array) IDs of the correlations to delete.

### Return value
(object) Returns an object containing the IDs of the deleted
correlations under the correlationids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/correlation/delete

<!-- method: correlation.get -->
## correlation.get

### Description
integer/array correlation.get(object parameters)
The method allows to retrieve correlations according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **correlationids** (string/array): Return only correlations with the given IDs.
- **selectFilter** (query): Return a filter property with the correlation conditions.
- **selectOperations** (query): Return an operations property with the correlation operations.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: correlationid , name , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/correlation/get

<!-- method: correlation.update -->
## correlation.update

### Description
object correlation.update(object/array correlations)
This method allows to update existing correlations.

### Parameters
(object/array) Correlation properties to be updated.
The correlationid property must be defined for each correlation, all
other properties are optional. Only the passed properties will be
updated, all others will remain unchanged.
Additionally to the standard correlation
properties , the method accepts the following
parameters.

- **filter** (object): Correlation filter object to replace the current filter.
- **operations** (array): Correlation operations to replace existing operations.

### Return value
(object) Returns an object containing the IDs of the updated
correlations under the correlationids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/correlation/update

<!-- method: dashboard.create -->
## dashboard.create

### Description
object dashboard.create(object/array dashboards)
This method allows to create new dashboards.

### Parameters
(object/array) Dashboards to create.
Additionally to the standard dashboard properties ,
the method accepts the following parameters.

- **pages** (array): Dashboard pages to be created for the dashboard. Dashboard pages will be ordered in the same order as specified. Parameter behavior : - required
- **users** (array): Dashboard user shares to be created on the dashboard.
- **userGroups** (array): Dashboard user group shares to be created on the dashboard.

### Return value
(object) Returns an object containing the IDs of the created
dashboards under the dashboardids property. The order of the returned
IDs matches the order of the passed dashboards.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dashboard/create

<!-- method: dashboard.delete -->
## dashboard.delete

### Description
object dashboard.delete(array dashboardids)
This method allows to delete dashboards.

### Parameters
(array) IDs of the dashboards to delete.

### Return value
(object) Returns an object containing the IDs of the deleted
dashboards under the dashboardids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dashboard/delete

<!-- method: dashboard.get -->
## dashboard.get

### Description
integer/array dashboard.get(object parameters)
The method allows to retrieve dashboards according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **dashboardids** (string/array): Return only dashboards with the given IDs.
- **selectPages** (query): Return a pages property with dashboard pages, correctly ordered.
- **selectUsers** (query): Return a users property with users that the dashboard is shared with.
- **selectUserGroups** (query): Return a userGroups property with user groups that the dashboard is shared with.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: dashboardid .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dashboard/get

<!-- method: dashboard.update -->
## dashboard.update

### Description
object dashboard.update(object/array dashboards)
This method allows to update existing dashboards.

### Parameters
(object/array) Dashboard properties to be updated.
The dashboardid property must be defined for each dashboard, all
other properties are optional. Only the passed properties will be
updated, all others will remain unchanged.
Additionally to the standard dashboard properties ,
the method accepts the following parameters.

- **pages** (array): Dashboard pages to replace the existing dashboard pages. Dashboard pages are updated by the dashboard_pageid property. New dashboard pages will be created for objects without dashboard_pageid property and the existing dashboard pages will be deleted if not reused. Dashboard pages will be ordered in the same order as specified. Only the specified properties of the dashboard pages will be updated.
- **users** (array): Dashboard user shares to replace the existing elements.
- **userGroups** (array): Dashboard user group shares to replace the existing elements.

### Return value
(object) Returns an object containing the IDs of the updated
dashboards under the dashboardids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dashboard/update

<!-- method: dashboard.widget_fields -->
## dashboard.widget_fields

### Description
This page contains navigation links for dashboard widget parameters
and possible property values for the respective dashboard widget field objects.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dashboard/widget_fields

<!-- method: dcheck.get -->
## dcheck.get

### Description
integer/array dcheck.get(object parameters)
The method allows to retrieve discovery checks according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **dcheckids** (string/array): Return only discovery checks with the given IDs.
- **druleids** (string/array): Return only discovery checks that belong to the given discovery rules.
- **dserviceids** (string/array): Return only discovery checks that have detected the given discovered services.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: dcheckid , druleid .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dcheck/get

<!-- method: dhost.get -->
## dhost.get

### Description
integer/array dhost.get(object parameters)
The method allows to retrieve discovered hosts according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **dhostids** (string/array): Return only discovered hosts with the given IDs.
- **druleids** (string/array): Return only discovered hosts that have been created by the given discovery rules.
- **dserviceids** (string/array): Return only discovered hosts that are running the given services.
- **selectDRules** (query): Return a drules property with an array of the discovery rules that detected the host.
- **selectDServices** (query): Return a dservices property with the discovered services running on the host. Supports count .
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectDServices - results will be sorted by dserviceid .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: dhostid , druleid .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dhost/get

<!-- method: discoveryrule.copy -->
## discoveryrule.copy

### Description
object discoveryrule.copy(object parameters)
This method allows to copy LLD rules with all of the prototypes to the
given hosts.

### Parameters
(object) Parameters defining the LLD rules to copy and the target
hosts.

- **discoveryids** (array): IDs of the LLD rules to be copied.
- **hostids** (array): IDs of the hosts to copy the LLD rules to.

### Return value
(boolean) Returns true if the copying was successful.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/discoveryrule/copy

<!-- method: discoveryrule.create -->
## discoveryrule.create

### Description
object discoveryrule.create(object/array lldRules)
This method allows to create new LLD rules.

### Parameters
(object/array) LLD rules to create.
Additionally to the standard LLD rule properties , the
method accepts the following parameters.

- **filter** (object): LLD rule filter for the LLD rule.
- **preprocessing** (array): LLD rule preprocessing options.
- **lld_macro_paths** (array): LLD rule lld_macro_path options.
- **overrides** (array): LLD rule overrides options.

### Return value
(object) Returns an object containing the IDs of the created LLD rules
under the itemids property. The order of the returned IDs matches the
order of the passed LLD rules.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/discoveryrule/create

<!-- method: discoveryrule.delete -->
## discoveryrule.delete

### Description
object discoveryrule.delete(array lldRuleIds)
This method allows to delete LLD rules.

### Parameters
(array) IDs of the LLD rules to delete.

### Return value
(object) Returns an object containing the IDs of the deleted LLD rules
under the ruleids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/discoveryrule/delete

<!-- method: discoveryrule.get -->
## discoveryrule.get

### Description
integer/array discoveryrule.get(object parameters)
The method allows to retrieve LLD rules according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **itemids** (string/array): Return only LLD rules with the given IDs.
- **groupids** (string/array): Return only LLD rules that belong to the hosts from the given groups.
- **hostids** (string/array): Return only LLD rules that belong to the given hosts.
- **inherited** (boolean): If set to true return only LLD rules inherited from a template.
- **interfaceids** (string/array): Return only LLD rules use the given host interfaces.
- **monitored** (boolean): If set to true return only enabled LLD rules that belong to monitored hosts.
- **templated** (boolean): If set to true return only LLD rules that belong to templates.
- **templateids** (string/array): Return only LLD rules that belong to the given templates.
- **selectFilter** (query): Return a filter property with data of the filter used by the LLD rule.
- **selectGraphs** (query): Returns a graphs property with graph prototypes that belong to the LLD rule. Supports count .
- **selectHostPrototypes** (query): Return a hostPrototypes property with host prototypes that belong to the LLD rule. Supports count .
- **selectHosts** (query): Return a hosts property with an array of hosts that the LLD rule belongs to.
- **selectItems** (query): Return an items property with item prototypes that belong to the LLD rule. Supports count .
- **selectTriggers** (query): Return a triggers property with trigger prototypes that belong to the LLD rule. Supports count .
- **selectLLDMacroPaths** (query): Return an lld_macro_paths property with a list of LLD macros and paths to values assigned to each corresponding macro.
- **selectPreprocessing** (query): Return a preprocessing property with LLD rule preprocessing options.
- **selectOverrides** (query): Return an lld_rule_overrides property with a list of override filters, conditions and operations that are performed on prototype objects.
- **filter** (object): Return only those results that exactly match the given filter. Accepts an array, where the keys are property names, and the values are either a single value or an array of values to match against. Supports additional filters: host - technical name of the host that the LLD rule belongs to.
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectItems , selectGraphs , selectTriggers .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: itemid , name , key_ , delay , type , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/discoveryrule/get

<!-- method: discoveryrule.update -->
## discoveryrule.update

### Description
object discoveryrule.update(object/array lldRules)
This method allows to update existing LLD rules.

### Parameters
(object/array) LLD rule properties to be updated.
The itemid property must be defined for each LLD rule, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard LLD rule properties , the
method accepts the following parameters.

- **filter** (object): LLD rule filter to replace the current filter.
- **preprocessing** (array): LLD rule preprocessing options to replace the existing preprocessing options. Parameter behavior : - read-only for inherited objects
- **lld_macro_paths** (array): LLD rule lld_macro_path options to replace the existing lld_macro_path options. Parameter behavior : - read-only for inherited objects
- **overrides** (array): LLD rule overrides options to replace the existing overrides options. Parameter behavior : - read-only for inherited objects

### Return value
(object) Returns an object containing the IDs of the updated LLD rules
under the itemids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/discoveryrule/update

<!-- method: drule.create -->
## drule.create

### Description
object drule.create(object/array discoveryRules)
This method allows to create new discovery rules.

### Parameters
(object/array) Discovery rules to create.
Additionally to the standard discovery rule
properties , the method accepts the following
parameters.

- **dchecks** (array): Discovery checks to create for the discovery rule. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the created
discovery rules under the druleids property. The order of the
returned IDs matches the order of the passed discovery rules.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/drule/create

<!-- method: drule.delete -->
## drule.delete

### Description
object drule.delete(array discoveryRuleIds)
This method allows to delete discovery rules.

### Parameters
(array) IDs of the discovery rules to delete.

### Return value
(object) Returns an object containing the IDs of the deleted discovery
rules under the druleids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/drule/delete

<!-- method: drule.get -->
## drule.get

### Description
integer/array drule.get(object parameters)
The method allows to retrieve discovery rules according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **dhostids** (string/array): Return only discovery rules that created the given discovered hosts.
- **druleids** (string/array): Return only discovery rules with the given IDs.
- **dserviceids** (string/array): Return only discovery rules that created the given discovered services.
- **selectDChecks** (query): Return a dchecks property with the discovery checks used by the discovery rule. Supports count .
- **selectDHosts** (query): Return a dhosts property with the discovered hosts created by the discovery rule. Supports count .
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectDChecks - results will be sorted by dcheckid ; selectDHosts - results will be sorted by dhostsid .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: druleid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/drule/get

<!-- method: drule.update -->
## drule.update

### Description
object drule.update(object/array discoveryRules)
This method allows to update existing discovery rules.

### Parameters
(object/array) Discovery rule properties to be updated.
The druleid property must be defined for each discovery rule, all
other properties are optional. Only the passed properties will be
updated, all others will remain unchanged.
Additionally to the standard discovery rule
properties , the method accepts the following
parameters.

- **dchecks** (array): Discovery checks to replace existing checks.

### Return value
(object) Returns an object containing the IDs of the updated discovery
rules under the druleids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/drule/update

<!-- method: dservice.get -->
## dservice.get

### Description
integer/array dservice.get(object parameters)
The method allows to retrieve discovered services according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **dserviceids** (string/array): Return only discovered services with the given IDs.
- **dhostids** (string/array): Return only discovered services that belong to the given discovered hosts.
- **dcheckids** (string/array): Return only discovered services that have been detected by the given discovery checks.
- **druleids** (string/array): Return only discovered services that have been detected by the given discovery rules.
- **selectDRules** (query): Return a drules property with an array of the discovery rules that detected the service.
- **selectDHosts** (query): Return a dhosts property with an array the discovered hosts that the service belongs to.
- **selectHosts** (query): Return a hosts property with the hosts with the same IP address and proxy as the service. Supports count .
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectHosts - result will be sorted by hostid .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: dserviceid , dhostid , ip .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/dservice/get

<!-- method: event.acknowledge -->
## event.acknowledge

### Description
object event.acknowledge(object/array parameters)
This method allows to update events. The following update actions can be
performed:
- Close event. If event is already resolved, this action will be
skipped.
- Acknowledge event. If event is already acknowledged, this action
will be skipped.
- Unacknowledge event. If event is not acknowledged, this action will be skipped.
- Add message.
- Change event severity. If event already has same severity, this
action will be skipped.
- Suppress event. If event is already suppressed, this action will be skipped.
- Unsuppress event. If event is not suppressed, this action will be skipped.

### Parameters
(object/array) Parameters containing the IDs of the events and update
operations that should be performed.

- **eventids** (string/object): IDs of the events to acknowledge. Parameter behavior : - required
- **action** (integer): Event update action(s). Possible bitmap values: 1 - close problem; 2 - acknowledge event; 4 - add message; 8 - change severity; 16 - unacknowledge event; 32 - suppress event; 64 - unsuppress event; 128 - change event rank to cause; 256 - change event rank to symptom. This is a bitmask field; any sum of possible bitmap values is acceptable (for example, 34 for acknowledge and suppress event). Parameter behavior : - required
- **cause_eventid** (string): Cause event ID. Parameter behavior : - required if action contains the "change event rank to symptom" bit
- **message** (string): Text of the message. Parameter behavior : - required if action contains the "add message" bit
- **severity** (integer): New severity for events. Possible values: 0 - not classified; 1 - information; 2 - warning; 3 - average; 4 - high; 5 - disaster. Parameter behavior : - required if action contains the "change severity" bit
- **suppress_until** (integer): Unix timestamp until which event must be suppressed. If set to "0", the suppression will be indefinite. Parameter behavior : - required if action contains the "suppress event" bit

### Return value
(object) Returns an object containing the IDs of the updated events
under the eventids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/event/acknowledge

<!-- method: event.get -->
## event.get

### Description
integer/array event.get(object parameters)
The method allows to retrieve events according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **eventids** (string/array): Return only events with the given IDs.
- **groupids** (string/array): Return only events created by objects that belong to the given host groups.
- **hostids** (string/array): Return only events created by objects that belong to the given hosts.
- **objectids** (string/array): Return only events created by the given objects.
- **source** (integer): Return only events with the given type. Refer to the event object page for a list of supported event types. Default: 0 - trigger events.
- **object** (integer): Return only events created by objects of the given type. Refer to the event object page for a list of supported object types. Default: 0 - trigger.
- **acknowledged** (boolean): If set to true return only acknowledged events.
- **suppressed** (boolean): true - return only suppressed events; false - return events in the normal state.
- **symptom** (boolean): true - return only symptom events; false - return only cause events.
- **severities** (integer/array): Return only events with given event severities. Applies only if object is trigger.
- **evaltype** (integer): Rules for tag searching. Possible values: 0 - (default) And/Or; 2 - Or.
- **tags** (array of objects): Return only events with given tags. Exact match by tag and case-insensitive search by value and operator. Format: [{"tag": "<tag>", "value": "<value>", "operator": "<operator>"}, ...] . An empty array returns all events. Possible operator types: 0 - (default) Like; 1 - Equal; 2 - Not like; 3 - Not equal 4 - Exists; 5 - Not exists.
- **eventid_from** (string): Return only events with IDs greater or equal to the given ID.
- **eventid_till** (string): Return only events with IDs less or equal to the given ID.
- **time_from** (timestamp): Return only events that have been created after or at the given time.
- **time_till** (timestamp): Return only events that have been created before or at the given time.
- **problem_time_from** (timestamp): Returns only events that were in the problem state starting with problem_time_from . Applies only if the source is trigger event and object is trigger. Mandatory if problem_time_till is specified.
- **problem_time_till** (timestamp): Returns only events that were in the problem state until problem_time_till . Applies only if the source is trigger event and object is trigger. Mandatory if problem_time_from is specified.
- **value** (integer/array): Return only events with the given values.
- **selectHosts** (query): Return a hosts property with hosts containing the object that created the event. Supported only for events generated by triggers, items or LLD rules.
- **selectRelatedObject** (query): Return a relatedObject property with the object that created the event. The type of object returned depends on the event type.
- **select_alerts** (query): Return an alerts property with alerts generated by the event. Alerts are sorted in reverse chronological order.
- **select_acknowledges** (query): Return an acknowledges property with event updates. Event updates are sorted in reverse chronological order. The event update object has the following properties: acknowledgeid - (string) acknowledgment's ID; userid - (string) ID of the user that updated the event; eventid - (string) ID of the updated event; clock - (timestamp) time when the event was updated; message - (string) text of the message; action - (integer) update action that was performed see event.acknowledge ; old_severity - (integer) event severity before this update action; new_severity - (integer) event severity after this update action; suppress_until - (timestamp) time till event will be suppressed; taskid - (string) ID of task if current event is undergoing a rank change; username - (string) username of the user that updated the event; name - (string) name of the user that updated the event; surname - (string) surname of the user that updated the event. Supports count .
- **selectTags** (query): Return a tags property with event tags.
- **selectSuppressionData** (query): Return a suppression_data property with the list of active maintenances and manual suppressions: maintenanceid - (string) ID of the maintenance; userid - (string) ID of user who suppressed the event; suppress_until - (integer) time until the event is suppressed.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: eventid , objectid , clock .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/event/get

<!-- method: graph.create -->
## graph.create

### Description
object graph.create(object/array graphs)
This method allows to create new graphs.

### Parameters
(object/array) Graphs to create.
Additionally to the standard graph properties , the
method accepts the following parameters.

- **gitems** (array): Graph items to be created for the graph. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the created graphs
under the graphids property. The order of the returned IDs matches the
order of the passed graphs.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/graph/create

<!-- method: graph.delete -->
## graph.delete

### Description
object graph.delete(array graphIds)
This method allows to delete graphs.

### Parameters
(array) IDs of the graphs to delete.

### Return value
(object) Returns an object containing the IDs of the deleted graphs
under the graphids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/graph/delete

<!-- method: graph.get -->
## graph.get

### Description
integer/array graph.get(object parameters)
The method allows to retrieve graphs according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **graphids** (string/array): Return only graphs with the given IDs.
- **groupids** (string/array): Return only graphs that belong to hosts or templates in the given host groups or template groups.
- **templateids** (string/array): Return only graph that belong to the given templates.
- **hostids** (string/array): Return only graphs that belong to the given hosts.
- **itemids** (string/array): Return only graphs that contain the given items.
- **templated** (boolean): If set to true return only graphs that belong to templates.
- **inherited** (boolean): If set to true return only graphs inherited from a template.
- **expandName** (flag): Expand macros in the graph name.
- **selectHostGroups** (query): Return a hostgroups property with the host groups that the graph belongs to.
- **selectTemplateGroups** (query): Return a templategroups property with the template groups that the graph belongs to.
- **selectTemplates** (query): Return a templates property with the templates that the graph belongs to.
- **selectHosts** (query): Return a hosts property with the hosts that the graph belongs to.
- **selectItems** (query): Return an items property with the items used in the graph.
- **selectGraphDiscovery** (query): Return a graphDiscovery property with the graph discovery object. The graph discovery objects links the graph to a graph prototype from which it was created. It has the following properties: graphid - (string) ID of the graph; parent_graphid - (string) ID of the graph prototype from which the graph has been created.
- **selectGraphItems** (query): Return a gitems property with the items used in the graph.
- **selectDiscoveryRule** (query): Return a discoveryRule property with the low-level discovery rule that created the graph.
- **filter** (object): Return only those results that exactly match the given filter. Accepts an array, where the keys are property names, and the values are either a single value or an array of values to match against. Supports additional filters: host - technical name of the host that the graph belongs to; hostid - ID of the host that the graph belongs to.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: graphid , name , graphtype .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)
- **selectGroups (deprecated)** (query): This parameter is deprecated, please use selectHostGroups or selectTemplateGroups instead. Return a groups property with the host groups and template groups that the graph belongs to.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/graph/get

<!-- method: graph.update -->
## graph.update

### Description
object graph.update(object/array graphs)
This method allows to update existing graphs.

### Parameters
(object/array) Graph properties to be updated.
The graphid property must be defined for each graph, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard graph properties the method
accepts the following parameters.

- **gitems** (array): Graph items to replace existing graph items. If a graph item has the gitemid property defined it will be updated, otherwise a new graph item will be created.

### Return value
(object) Returns an object containing the IDs of the updated graphs
under the graphids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/graph/update

<!-- method: graphitem.get -->
## graphitem.get

### Description
integer/array graphitem.get(object parameters)
The method allows to retrieve graph items according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **graphids** (string/array): Return only graph items that belong to the given graphs.
- **itemids** (string/array): Return only graph items with the given item IDs.
- **type** (integer): Return only graph items with the given type. Refer to the graph item object page for a list of supported graph item types.
- **selectGraphs** (query): Return a graphs property with an array of graphs that the item belongs to.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: gitemid .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **sortorder** (string/array)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/graphitem/get

<!-- method: graphprototype.create -->
## graphprototype.create

### Description
object graphprototype.create(object/array graphPrototypes)
This method allows to create new graph prototypes.

### Parameters
(object/array) Graph prototypes to create.
Additionally to the standard graph prototype
properties , the method accepts the following
parameters.

- **gitems** (array): Graph items to be created for the graph prototypes. Graph items can reference both items and item prototypes, but at least one item prototype must be present. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the created graph
prototypes under the graphids property. The order of the returned IDs
matches the order of the passed graph prototypes.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/graphprototype/create

<!-- method: graphprototype.delete -->
## graphprototype.delete

### Description
object graphprototype.delete(array graphPrototypeIds)
This method allows to delete graph prototypes.

### Parameters
(array) IDs of the graph prototypes to delete.

### Return value
(object) Returns an object containing the IDs of the deleted graph
prototypes under the graphids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/graphprototype/delete

<!-- method: graphprototype.get -->
## graphprototype.get

### Description
integer/array graphprototype.get(object parameters)
The method allows to retrieve graph prototypes according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **discoveryids** (string/array): Return only graph prototypes that belong to the given discovery rules.
- **graphids** (string/array): Return only graph prototypes with the given IDs.
- **groupids** (string/array): Return only graph prototypes that belong to hosts or templates in the given host groups or template groups.
- **hostids** (string/array): Return only graph prototypes that belong to the given hosts.
- **inherited** (boolean): If set to true return only graph prototypes inherited from a template.
- **itemids** (string/array): Return only graph prototypes that contain the given item prototypes.
- **templated** (boolean): If set to true return only graph prototypes that belong to templates.
- **templateids** (string/array): Return only graph prototypes that belong to the given templates.
- **selectDiscoveryRule** (query): Return a discoveryRule property with the LLD rule that the graph prototype belongs to.
- **selectGraphItems** (query): Return a gitems property with the graph items used in the graph prototype.
- **selectHostGroups** (query): Return a hostgroups property with the host groups that the graph prototype belongs to.
- **selectHosts** (query): Return a hosts property with the hosts that the graph prototype belongs to.
- **selectItems** (query): Return an items property with the items and item prototypes used in the graph prototype.
- **selectTemplateGroups** (query): Return a templategroups property with the template groups that the graph prototype belongs to.
- **selectTemplates** (query): Return a templates property with the templates that the graph prototype belongs to.
- **filter** (object): Return only those results that exactly match the given filter. Accepts an array, where the keys are property names, and the values are either a single value or an array of values to match against. Supports additional filters: host - technical name of the host that the graph prototype belongs to; hostid - ID of the host that the graph prototype belongs to.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: graphid , name , graphtype .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)
- **selectGroups (deprecated)** (query): This parameter is deprecated, please use selectHostGroups or selectTemplateGroups instead. Return a groups property with the host groups and template groups that the graph prototype belongs to.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/graphprototype/get

<!-- method: graphprototype.update -->
## graphprototype.update

### Description
object graphprototype.update(object/array graphPrototypes)
This method allows to update existing graph prototypes.

### Parameters
(object/array) Graph prototype properties to be updated.
The graphid property must be defined for each graph prototype, all
other properties are optional. Only the passed properties will be
updated, all others will remain unchanged.
Additionally to the standard graph prototype
properties , the method accepts the following
parameters.

- **gitems** (array): Graph items to replace existing graph items. If a graph item has the gitemid property defined it will be updated, otherwise a new graph item will be created.

### Return value
(object) Returns an object containing the IDs of the updated graph
prototypes under the graphids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/graphprototype/update

<!-- method: hanode.get -->
## hanode.get

### Description
integer/array hanode.get(object parameters)
The method allows to retrieve a list of High availability cluster nodes
according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **ha_nodeids** (string/array): Return only nodes with the given node IDs.
- **filter** (object): Return only those results that exactly match the given filter. Accepts an array, where the keys are property names, and the values are either a single value or an array of values to match against. Allows filtering by the node properties: name , address , status .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: name , lastaccess , status .
- **countOutput** (flag): These parameters being common for all get methods are described in detail in the reference commentary .
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **sortorder** (string/array)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hanode/get

<!-- method: history.clear -->
## history.clear

### Description
object history.clear(array itemids)
This method allows to clear item history.

### Parameters
(array) IDs of items to clear.

### Return value
(object) Returns an object containing the IDs of the cleared items
under the itemids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/history/clear

<!-- method: history.get -->
## history.get

### Description
integer/array history.get(object parameters)
The method allows to retrieve history data according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **history** (integer): History object types to return. Possible values: 0 - numeric float; 1 - character; 2 - log; 3 - (default) numeric unsigned; 4 - text.
- **hostids** (string/array): Return only history from the given hosts.
- **itemids** (string/array): Return only history from the given items.
- **time_from** (timestamp): Return only values that have been received after or at the given time.
- **time_till** (timestamp): Return only values that have been received before or at the given time.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: itemid , clock .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/history/get

<!-- method: host.create -->
## host.create

### Description
object host.create(object/array hosts)
This method allows to create new hosts.

### Parameters
(object/array) Hosts to create.
Additionally to the standard host properties , the method
accepts the following parameters.

- **groups** (object/array): Host groups to add the host to. The host groups must have the groupid property defined. Parameter behavior : - required
- **interfaces** (object/array): Interfaces to be created for the host.
- **tags** (object/array): Host tags .
- **templates** (object/array): Templates to be linked to the host. The templates must have the templateid property defined.
- **macros** (object/array): User macros to be created for the host.
- **inventory** (object): Host inventory properties.

### Return value
(object) Returns an object containing the IDs of the created hosts
under the hostids property. The order of the returned IDs matches the
order of the passed hosts.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/host/create

<!-- method: host.delete -->
## host.delete

### Description
object host.delete(array hosts)
This method allows to delete hosts.

### Parameters
(array) IDs of hosts to delete.

### Return value
(object) Returns an object containing the IDs of the deleted hosts
under the hostids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/host/delete

<!-- method: host.get -->
## host.get

### Description
integer/array host.get(object parameters)
The method allows to retrieve hosts according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **groupids** (string/array): Return only hosts that belong to the given groups.
- **dserviceids** (string/array): Return only hosts that are related to the given discovered services.
- **graphids** (string/array): Return only hosts that have the given graphs.
- **hostids** (string/array): Return only hosts with the given host IDs.
- **httptestids** (string/array): Return only hosts that have the given web checks.
- **interfaceids** (string/array): Return only hosts that use the given interfaces.
- **itemids** (string/array): Return only hosts that have the given items.
- **maintenanceids** (string/array): Return only hosts that are affected by the given maintenances.
- **monitored_hosts** (flag): Return only monitored hosts.
- **proxy_hosts** (flag): Return only proxies.
- **proxyids** (string/array): Return only hosts that are monitored by the given proxies.
- **templated_hosts** (flag): Return both hosts and templates.
- **templateids** (string/array): Return only hosts that are linked to the given templates.
- **triggerids** (string/array): Return only hosts that have the given triggers.
- **with_items** (flag): Return only hosts that have items. Overrides the with_monitored_items and with_simple_graph_items parameters.
- **with_item_prototypes** (flag): Return only hosts that have item prototypes. Overrides the with_simple_graph_item_prototypes parameter.
- **with_simple_graph_item_prototypes** (flag): Return only hosts that have item prototypes, which are enabled for creation and have numeric type of information.
- **with_graphs** (flag): Return only hosts that have graphs.
- **with_graph_prototypes** (flag): Return only hosts that have graph prototypes.
- **with_httptests** (flag): Return only hosts that have web checks. Overrides the with_monitored_httptests parameter.
- **with_monitored_httptests** (flag): Return only hosts that have enabled web checks.
- **with_monitored_items** (flag): Return only hosts that have enabled items. Overrides the with_simple_graph_items parameter.
- **with_monitored_triggers** (flag): Return only hosts that have enabled triggers. All of the items used in the trigger must also be enabled.
- **with_simple_graph_items** (flag): Return only hosts that have items with numeric type of information.
- **with_triggers** (flag): Return only hosts that have triggers. Overrides the with_monitored_triggers parameter.
- **withProblemsSuppressed** (boolean): Return hosts that have suppressed problems. Possible values: null - (default) all hosts; true - only hosts with suppressed problems; false - only hosts with unsuppressed problems.
- **evaltype** (integer): Rules for tag searching. Possible values: 0 - (default) And/Or; 2 - Or.
- **severities** (integer/array): Return hosts that have only problems with given severities. Applies only if problem object is trigger.
- **tags** (object/array): Return only hosts with given tags. Exact match by tag and case-sensitive or case-insensitive search by tag value depending on operator value. Format: [{"tag": "<tag>", "value": "<value>", "operator": "<operator>"}, ...] . An empty array returns all hosts. Possible operator values: 0 - (default) Contains; 1 - Equals; 2 - Not like; 3 - Not equal; 4 - Exists; 5 - Not exists.
- **inheritedTags** (boolean): Return hosts that have given tags also in all of their linked templates. Default: Possible values: true - linked templates must also have given tags ; false - (default) linked template tags are ignored.
- **selectDiscoveries** (query): Return a discoveries property with host low-level discovery rules. Supports count .
- **selectDiscoveryRule** (query): Return a discoveryRule property with the low-level discovery rule that created the host (from host prototype in VMware monitoring).
- **selectGraphs** (query): Return a graphs property with host graphs. Supports count .
- **selectHostDiscovery** (query): Return a hostDiscovery property with host discovery object data. The host discovery object links a discovered host to a host prototype or a host prototypes to an LLD rule and has the following properties: host - (string) host of the host prototype; hostid - (string) ID of the discovered host or host prototype; parent_hostid - (string) ID of the host prototype from which the host has been created; parent_itemid - (string) ID of the LLD rule that created the discovered host; lastcheck - (timestamp) time when the host was last discovered; ts_delete - (timestamp) time when a host that is no longer discovered will be deleted.
- **selectHostGroups** (query): Return a hostgroups property with host groups data that the host belongs to.
- **selectHttpTests** (query): Return an httpTests property with host web scenarios. Supports count .
- **selectInterfaces** (query): Return an interfaces property with host interfaces. Supports count .
- **selectInventory** (query): Return an inventory property with host inventory data.
- **selectItems** (query): Return an items property with host items. Supports count .
- **selectMacros** (query): Return a macros property with host macros.
- **selectParentTemplates** (query): Return a parentTemplates property with templates that the host is linked to. In addition to Template object fields, it contains link_type - (integer) the way that the template is linked to host. Possible values: 0 - (default) manually linked; 1 - automatically linked by LLD. Supports count .
- **selectDashboards** (query): Return a dashboards property. Supports count .
- **selectTags** (query): Return a tags property with host tags.
- **selectInheritedTags** (query): Return an inheritedTags property with tags that are on all templates which are linked to host.
- **selectTriggers** (query): Return a triggers property with host triggers. Supports count .
- **selectValueMaps** (query): Return a valuemaps property with host value maps.
- **filter** (object): Return only those results that exactly match the given filter. Accepts an array, where the keys are property names, and the values are either a single value or an array of values to match against. Allows filtering by interface properties. Doesn't work for text fields.
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectParentTemplates - results will be sorted by host ; selectInterfaces ; selectItems - sorted by name ; selectDiscoveries - sorted by name ; selectTriggers - sorted by description ; selectGraphs - sorted by name ; selectDashboards - sorted by name .
- **search** (object): Return results that match the given pattern (case-insensitive). Accepts an array, where the keys are property names, and the values are strings to search for. If no additional options are given, this will perform a LIKE "%…%" search. Allows searching by interface properties. Works only for string and text fields.
- **searchInventory** (object): Return only hosts that have inventory data matching the given wildcard search. This parameter is affected by the same additional parameters as search .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: hostid , host , name , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)
- **selectGroups (deprecated)** (query): This parameter is deprecated, please use selectHostGroups instead. Return a groups property with host groups data that the host belongs to.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/host/get

<!-- method: host.massadd -->
## host.massadd

### Description
object host.massadd(object parameters)
This method allows to simultaneously add multiple related objects to all
the given hosts.

### Parameters
(object) Parameters containing the IDs of the hosts to update and the
objects to add to all the hosts.
The method accepts the following parameters.

- **hosts** (object/array): Hosts to be updated. The hosts must have the hostid property defined. Parameter behavior : - required
- **groups** (object/array): Host groups to add to the given hosts. The host groups must have the groupid property defined.
- **interfaces** (object/array): Host interfaces to be created for the given hosts.
- **macros** (object/array): User macros to be created for the given hosts.
- **templates** (object/array): Templates to link to the given hosts. The templates must have the templateid property defined.

### Return value
(object) Returns an object containing the IDs of the updated hosts
under the hostids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/host/massadd

<!-- method: host.massremove -->
## host.massremove

### Description
object host.massremove(object parameters)
This method allows to remove related objects from multiple hosts.

### Parameters
(object) Parameters containing the IDs of the hosts to update and the
objects that should be removed.

- **hostids** (string/array): IDs of the hosts to be updated. Parameter behavior : - required
- **groupids** (string/array): Host groups to remove the given hosts from.
- **interfaces** (object/array): Host interfaces to remove from the given hosts. The host interface object must have the ip , dns and port properties defined.
- **macros** (string/array): User macros to delete from the given hosts.
- **templateids** (string/array): Templates to unlink from the given hosts.
- **templateids_clear** (string/array): Templates to unlink and clear from the given hosts.

### Return value
(object) Returns an object containing the IDs of the updated hosts
under the hostids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/host/massremove

<!-- method: host.massupdate -->
## host.massupdate

### Description
object host.massupdate(object parameters)
This method allows to simultaneously replace or remove related objects
and update properties on multiple hosts.

### Parameters
(object) Parameters containing the IDs of the hosts to update and the
properties that should be updated.
Additionally to the standard host properties , the method
accepts the following parameters.

- **hosts** (object/array): Hosts to be updated. The hosts must have the hostid property defined. Parameter behavior : - required
- **groups** (object/array): Host groups to replace the current host groups the hosts belong to. The host groups must have the groupid property defined.
- **interfaces** (object/array): Host interfaces to replace the current host interfaces on the given hosts.
- **inventory** (object): Host inventory properties. Host inventory mode cannot be updated using the inventory parameter, use inventory_mode instead.
- **macros** (object/array): User macros to replace the current user macros on the given hosts.
- **templates** (object/array): Templates to replace the currently linked templates on the given hosts. The templates must have the templateid property defined.
- **templates_clear** (object/array): Templates to unlink and clear from the given hosts. The templates must have the templateid property defined.

### Return value
(object) Returns an object containing the IDs of the updated hosts
under the hostids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/host/massupdate

<!-- method: host.update -->
## host.update

### Description
object host.update(object/array hosts)
This method allows to update existing hosts.

### Parameters
(object/array) Host properties to be updated.
The hostid property must be defined for each host, all other
properties are optional. Only the given properties will be updated, all
others will remain unchanged.
Note, however, that updating the host technical name will also update
the host's visible name (if not given or empty) by the host's technical
name value.
Additionally to the standard host properties , the method
accepts the following parameters.

- **groups** (object/array): Host groups to replace the current host groups the host belongs to. The host groups must have the groupid property defined. All host groups that are not listed in the request will be unlinked.
- **interfaces** (object/array): Host interfaces to replace the current host interfaces. All interfaces that are not listed in the request will be removed.
- **tags** (object/array): Host tags to replace the current host tags. All tags that are not listed in the request will be removed.
- **inventory** (object): Host inventory properties.
- **macros** (object/array): User macros to replace the current user macros. All macros that are not listed in the request will be removed.
- **templates** (object/array): Templates to replace the currently linked templates. All templates that are not listed in the request will be only unlinked. The templates must have the templateid property defined.
- **templates_clear** (object/array): Templates to unlink and clear from the host. The templates must have the templateid property defined.

### Return value
(object) Returns an object containing the IDs of the updated hosts
under the hostids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/host/update

<!-- method: hostgroup.create -->
## hostgroup.create

### Description
object hostgroup.create(object/array hostGroups)
This method allows to create new host groups.

### Parameters
(object/array) Host groups to create.
The method accepts host groups
with the standard host group properties .

### Return value
(object) Returns an object containing the IDs of the created host
groups under the groupids property. The order of the returned IDs
matches the order of the passed host groups.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostgroup/create

<!-- method: hostgroup.delete -->
## hostgroup.delete

### Description
object hostgroup.delete(array hostGroupIds)
This method allows to delete host groups.
A host group cannot be deleted if:
- it contains hosts that belong to this group only;
- it is marked as internal;
- it is used by a host prototype;
- it is used in a global script;
- it is used in a correlation condition.

### Parameters
(array) IDs of the host groups to delete.

### Return value
(object) Returns an object containing the IDs of the deleted host
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostgroup/delete

<!-- method: hostgroup.get -->
## hostgroup.get

### Description
integer/array hostgroup.get(object parameters)
The method allows to retrieve host groups according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **graphids** (string/array): Return only host groups that contain hosts with the given graphs.
- **groupids** (string/array): Return only host groups with the given host group IDs.
- **hostids** (string/array): Return only host groups that contain the given hosts.
- **maintenanceids** (string/array): Return only host groups that are affected by the given maintenances.
- **triggerids** (string/array): Return only host groups that contain hosts with the given triggers.
- **with_graphs** (flag): Return only host groups that contain hosts with graphs.
- **with_graph_prototypes** (flag): Return only host groups that contain hosts with graph prototypes.
- **with_hosts** (flag): Return only host groups that contain hosts.
- **with_httptests** (flag): Return only host groups that contain hosts with web checks. Overrides the with_monitored_httptests parameter.
- **with_items** (flag): Return only host groups that contain hosts with items. Overrides the with_monitored_items and with_simple_graph_items parameters.
- **with_item_prototypes** (flag): Return only host groups that contain hosts with item prototypes. Overrides the with_simple_graph_item_prototypes parameter.
- **with_simple_graph_item_prototypes** (flag): Return only host groups that contain hosts with item prototypes, which are enabled for creation and have numeric type of information.
- **with_monitored_httptests** (flag): Return only host groups that contain hosts with enabled web checks.
- **with_monitored_hosts** (flag): Return only host groups that contain monitored hosts.
- **with_monitored_items** (flag): Return only host groups that contain hosts with enabled items. Overrides the with_simple_graph_items parameter.
- **with_monitored_triggers** (flag): Return only host groups that contain hosts with enabled triggers. All of the items used in the trigger must also be enabled.
- **with_simple_graph_items** (flag): Return only host groups that contain hosts with numeric items.
- **with_triggers** (flag): Return only host groups that contain hosts with triggers. Overrides the with_monitored_triggers parameter.
- **selectDiscoveryRule** (query): Return a discoveryRule property with the LLD rule that created the host group.
- **selectGroupDiscovery** (query): Return a groupDiscovery property with the host group discovery object. The host group discovery object links a discovered host group to a host group prototype and has the following properties: groupid - (string) ID of the discovered host group; lastcheck - (timestamp) time when the host group was last discovered; name - (string) name of the host group prototype; parent_group_prototypeid - (string) ID of the host group prototype from which the host group has been created; ts_delete - (timestamp) time when a host group that is no longer discovered will be deleted.
- **selectHosts** (query): Return a hosts property with the hosts that belong to the host group. Supports count .
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectHosts - results will be sorted by host .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: groupid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)
- **monitored_hosts (deprecated)** (flag): This parameter is deprecated, please use with_monitored_hosts instead. Return only host groups that contain monitored hosts.
- **real_hosts (deprecated)** (flag): This parameter is deprecated, please use with_hosts instead. Return only host groups that contain hosts.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostgroup/get

<!-- method: hostgroup.massadd -->
## hostgroup.massadd

### Description
object hostgroup.massadd(object parameters)
This method allows to simultaneously add multiple related objects to all
the given host groups.

### Parameters
(object) Parameters containing the IDs of the host groups to update
and the objects to add to all the host groups.
The method accepts the following parameters.

- **groups** (object/array): Host groups to be updated. The host groups must have the groupid property defined. Parameter behavior : - required
- **hosts** (object/array): Hosts to add to all host groups. The hosts must have the hostid property defined.

### Return value
(object) Returns an object containing the IDs of the updated host
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostgroup/massadd

<!-- method: hostgroup.massremove -->
## hostgroup.massremove

### Description
object hostgroup.massremove(object parameters)
This method allows to remove related objects from multiple host groups.

### Parameters
(object) Parameters containing the IDs of the host groups to update
and the objects that should be removed.

- **groupids** (string/array): IDs of the host groups to be updated. Parameter behavior : - required
- **hostids** (string/array): Hosts to remove from all host groups.

### Return value
(object) Returns an object containing the IDs of the updated host
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostgroup/massremove

<!-- method: hostgroup.massupdate -->
## hostgroup.massupdate

### Description
object hostgroup.massupdate(object parameters)
This method allows to replace hosts and templates with the specified
ones in multiple host groups.

### Parameters
(object) Parameters containing the IDs of the host groups to update
and the objects that should be updated.

- **groups** (object/array): Host groups to be updated. The host groups must have the groupid property defined. Parameter behavior : - required
- **hosts** (object/array): Hosts to replace the current hosts on the given host groups. All other hosts, except the ones mentioned, will be excluded from host groups. Discovered hosts will not be affected. The hosts must have the hostid property defined. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the updated host
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostgroup/massupdate

<!-- method: hostgroup.propagate -->
## hostgroup.propagate

### Description
object hostgroup.propagate(object parameters)
This method allows to apply permissions and tag filters to all subgroups of a host group.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **groups** (object/array): Host groups to propagate. The host groups must have the groupid property defined. Parameter behavior : - required
- **permissions** (boolean): Set to "true" to propagate permissions. Parameter behavior : - required if tag_filters is not set
- **tag_filters** (boolean): Set to "true" to propagate tag filters. Parameter behavior : - required if permissions is not set

### Return value
(object) Returns an object containing the IDs of the propagated host
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostgroup/propagate

<!-- method: hostgroup.update -->
## hostgroup.update

### Description
object hostgroup.update(object/array hostGroups)
This method allows to update existing hosts groups.

### Parameters
(object/array) Host group properties to be
updated.
The groupid property must be defined for each host group, all other
properties are optional. Only the given properties will be updated, all
others will remain unchanged.

### Return value
(object) Returns an object containing the IDs of the updated host
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostgroup/update

<!-- method: hostinterface.create -->
## hostinterface.create

### Description
object hostinterface.create(object/array hostInterfaces)
This method allows to create new host interfaces.

### Parameters
(object/array) Host interfaces to create.
The method accepts host interfaces with the standard host interface properties .

### Return value
(object) Returns an object containing the IDs of the created host
interfaces under the interfaceids property. The order of the returned
IDs matches the order of the passed host interfaces.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/create

<!-- method: hostinterface.delete -->
## hostinterface.delete

### Description
object hostinterface.delete(array hostInterfaceIds)
This method allows to delete host interfaces.

### Parameters
(array) IDs of the host interfaces to delete.

### Return value
(object) Returns an object containing the IDs of the deleted host
interfaces under the interfaceids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/delete

<!-- method: hostinterface.get -->
## hostinterface.get

### Description
integer/array hostinterface.get(object parameters)
The method allows to retrieve host interfaces according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **hostids** (string/array): Return only host interfaces used by the given hosts.
- **interfaceids** (string/array): Return only host interfaces with the given IDs.
- **itemids** (string/array): Return only host interfaces used by the given items.
- **triggerids** (string/array): Return only host interfaces used by items in the given triggers.
- **selectItems** (query): Return an items property with the items that use the interface. Supports count .
- **selectHosts** (query): Return a hosts property with an array of hosts that use the interface.
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectItems .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: interfaceid , dns , ip .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/get

<!-- method: hostinterface.massadd -->
## hostinterface.massadd

### Description
object hostinterface.massadd(object parameters)
This method allows to simultaneously add host interfaces to multiple
hosts.

### Parameters
(object) Parameters containing the host interfaces to be created on
the given hosts.
The method accepts the following parameters.

- **interfaces** (object/array): Host interfaces to create on the given hosts. Parameter behavior : - required
- **hosts** (object/array): Hosts to be updated. The hosts must have the hostid property defined. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the created host
interfaces under the interfaceids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/massadd

<!-- method: hostinterface.massremove -->
## hostinterface.massremove

### Description
object hostinterface.massremove(object parameters)
This method allows to remove host interfaces from the given hosts.

### Parameters
(object) Parameters containing the IDs of the hosts to be updated and
the interfaces to be removed.

- **interfaces** (object/array): Host interfaces to remove from the given hosts. The host interface object must have the ip , dns and port properties defined. Parameter behavior : - required
- **hostids** (string/array): IDs of the hosts to be updated. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the deleted host
interfaces under the interfaceids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/massremove

<!-- method: hostinterface.replacehostinterfaces -->
## hostinterface.replacehostinterfaces

### Description
object hostinterface.replacehostinterfaces(object parameters)
This method allows to replace all host interfaces on a given host.

### Parameters
(object) Parameters containing the ID of the host to be updated and
the new host interfaces.

- **interfaces** (object/array): Host interfaces to replace the current host interfaces with. Parameter behavior : - required
- **hostid** (string): ID of the host to be updated. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the created host
interfaces under the interfaceids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/replacehostinterfaces

<!-- method: hostinterface.update -->
## hostinterface.update

### Description
object hostinterface.update(object/array hostInterfaces)
This method allows to update existing host interfaces.

### Parameters
(object/array) Host interface properties to
be updated.
The interfaceid property must be defined for each host interface, all
other properties are optional. Only the given properties will be
updated, all others will remain unchanged.

### Return value
(object) Returns an object containing the IDs of the updated host
interfaces under the interfaceids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostinterface/update

<!-- method: hostprototype.create -->
## hostprototype.create

### Description
object hostprototype.create(object/array hostPrototypes)
This method allows to create new host prototypes.

### Parameters
(object/array) Host prototypes to create.
Additionally to the standard host prototype
properties , the method accepts the following
parameters.

- **groupLinks** (array): Group links to be created for the host prototype. Parameter behavior : - required
- **ruleid** (string): ID of the LLD rule that the host prototype belongs to. Parameter behavior : - required
- **groupPrototypes** (array): Group prototypes to be created for the host prototype.
- **macros** (object/array): User macros to be created for the host prototype.
- **tags** (object/array): Host prototype tags .
- **interfaces** (object/array): Host prototype custom interfaces .
- **templates** (object/array): Templates to be linked to the host prototype. The templates must have the templateid property defined.

### Return value
(object) Returns an object containing the IDs of the created host
prototypes under the hostids property. The order of the returned IDs
matches the order of the passed host prototypes.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostprototype/create

<!-- method: hostprototype.delete -->
## hostprototype.delete

### Description
object hostprototype.delete(array hostPrototypeIds)
This method allows to delete host prototypes.

### Parameters
(array) IDs of the host prototypes to delete.

### Return value
(object) Returns an object containing the IDs of the deleted host
prototypes under the hostids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostprototype/delete

<!-- method: hostprototype.get -->
## hostprototype.get

### Description
integer/array hostprototype.get(object parameters)
The method allows to retrieve host prototypes according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **hostids** (string/array): Return only host prototypes with the given IDs.
- **discoveryids** (string/array): Return only host prototype that belong to the given LLD rules.
- **inherited** (boolean): If set to true return only items inherited from a template.
- **selectDiscoveryRule** (query): Return a discoveryRule property with the LLD rule that the host prototype belongs to.
- **selectInterfaces** (query): Return an interfaces property with host prototype custom interfaces.
- **selectGroupLinks** (query): Return a groupLinks property with the group links of the host prototype.
- **selectGroupPrototypes** (query): Return a groupPrototypes property with the group prototypes of the host prototype.
- **selectMacros** (query): Return a macros property with host prototype macros.
- **selectParentHost** (query): Return a parentHost property with the host that the host prototype belongs to.
- **selectTags** (query): Return a tags property with host prototype tags.
- **selectTemplates** (query): Return a templates property with the templates linked to the host prototype. Supports count .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: hostid , host , name , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostprototype/get

<!-- method: hostprototype.update -->
## hostprototype.update

### Description
object hostprototype.update(object/array hostPrototypes)
This method allows to update existing host prototypes.

### Parameters
(object/array) Host prototype properties to be updated.
The hostid property must be defined for each host prototype, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard host prototype
properties , the method accepts the following
parameters.

- **groupLinks** (array): Group links to replace the current group links on the host prototype. Parameter behavior : - read-only for inherited objects
- **groupPrototypes** (array): Group prototypes to replace the existing group prototypes on the host prototype. Parameter behavior : - read-only for inherited objects
- **macros** (object/array): User macros to replace the current user macros. All macros that are not listed in the request will be removed.
- **tags** (object/array): Host prototype tags to replace the current tags. All tags that are not listed in the request will be removed. Parameter behavior : - read-only for inherited objects
- **interfaces** (object/array): Host prototype custom interfaces to replace the current interfaces. Custom interface object should contain all its parameters. All interfaces that are not listed in the request will be removed. Parameter behavior : - supported if custom_interfaces of Host prototype object is set to "use host prototypes custom interfaces" - read-only for inherited objects
- **templates** (object/array): Templates to replace the currently linked templates. The templates must have the templateid property defined.

### Return value
(object) Returns an object containing the IDs of the updated host
prototypes under the hostids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/hostprototype/update

<!-- method: housekeeping.get -->
## housekeeping.get

### Description
object housekeeping.get(object parameters)
The method allows to retrieve housekeeping object according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports only one parameter.

- **output** (query): This parameter being common for all get methods described in the reference commentary .

### Return value
(object) Returns housekeeping object.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/housekeeping/get

<!-- method: housekeeping.update -->
## housekeeping.update

### Description
object housekeeping.update(object housekeeping)
This method allows to update existing housekeeping settings.

### Parameters
(object) Housekeeping properties to be updated.

### Return value
(array) Returns an array with the names of updated parameters.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/housekeeping/update

<!-- method: httptest.create -->
## httptest.create

### Description
object httptest.create(object/array webScenarios)
This method allows to create new web scenarios.

### Parameters
(object/array) Web scenarios to create.
Additionally to the standard web scenario
properties , the method accepts the following
parameters.

- **steps** (array): Web scenario steps . Parameter behavior : - required
- **tags** (array): Web scenario tags .

### Return value
(object) Returns an object containing the IDs of the created web
scenarios under the httptestids property. The order of the returned
IDs matches the order of the passed web scenarios.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/httptest/create

<!-- method: httptest.delete -->
## httptest.delete

### Description
object httptest.delete(array webScenarioIds)
This method allows to delete web scenarios.

### Parameters
(array) IDs of the web scenarios to delete.

### Return value
(object) Returns an object containing the IDs of the deleted web
scenarios under the httptestids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/httptest/delete

<!-- method: httptest.get -->
## httptest.get

### Description
integer/array httptest.get(object parameters)
The method allows to retrieve web scenarios according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **groupids** (string/array): Return only web scenarios that belong to the given host groups.
- **hostids** (string/array): Return only web scenarios that belong to the given hosts.
- **httptestids** (string/array): Return only web scenarios with the given IDs.
- **inherited** (boolean): If set to true return only web scenarios inherited from a template.
- **monitored** (boolean): If set to true return only enabled web scenarios that belong to monitored hosts.
- **templated** (boolean): If set to true return only web scenarios that belong to templates.
- **templateids** (string/array): Return only web scenarios that belong to the given templates.
- **expandName** (flag): Expand macros in the name of the web scenario.
- **expandStepName** (flag): Expand macros in the names of scenario steps.
- **evaltype** (integer): Rules for tag searching. Possible values: 0 - (default) And/Or; 2 - Or.
- **tags** (array of objects): Return only web scenarios with given tags. Exact match by tag and case-sensitive or case-insensitive search by tag value depending on operator value. Format: [{"tag": "<tag>", "value": "<value>", "operator": "<operator>"}, ...] . An empty array returns all web scenarios. Possible operator types: 0 - (default) Like; 1 - Equal; 2 - Not like; 3 - Not equal 4 - Exists; 5 - Not exists.
- **selectHosts** (query): Return the hosts that the web scenario belongs to as an array in the hosts property.
- **selectSteps** (query): Return web scenario steps in the steps property. Supports count .
- **selectTags** (query): Return web scenario tags in the tags property.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: httptestid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/httptest/get

<!-- method: httptest.update -->
## httptest.update

### Description
object httptest.update(object/array webScenarios)
This method allows to update existing web scenarios.

### Parameters
(object/array) Web scenario properties to be updated.
The httptestid property must be defined for each web scenario, all
other properties are optional. Only the passed properties will be
updated, all others will remain unchanged.
Additionally to the standard web scenario
properties , the method accepts the following
parameters.

- **steps** (array): Scenario steps to replace existing steps.
- **tags** (array): Web scenario tags .

### Return value
(object) Returns an object containing the IDs of the updated web
scenarios under the httptestid property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/httptest/update

<!-- method: iconmap.create -->
## iconmap.create

### Description
object iconmap.create(object/array iconMaps)
This method allows to create new icon maps.

### Parameters
(object/array) Icon maps to create.
Additionally to the standard icon map properties , the
method accepts the following parameters.

- **mappings** (array): Icon mappings to be created for the icon map. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the created icon maps
under the iconmapids property. The order of the returned IDs matches
the order of the passed icon maps.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/iconmap/create

<!-- method: iconmap.delete -->
## iconmap.delete

### Description
object iconmap.delete(array iconMapIds)
This method allows to delete icon maps.

### Parameters
(array) IDs of the icon maps to delete.

### Return value
(object) Returns an object containing the IDs of the deleted icon maps
under the iconmapids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/iconmap/delete

<!-- method: iconmap.get -->
## iconmap.get

### Description
integer/array iconmap.get(object parameters)
The method allows to retrieve icon maps according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **iconmapids** (string/array): Return only icon maps with the given IDs.
- **sysmapids** (string/array): Return only icon maps that are used in the given maps.
- **selectMappings** (query): Return a mappings property with the icon mappings used.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: iconmapid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/iconmap/get

<!-- method: iconmap.update -->
## iconmap.update

### Description
object iconmap.update(object/array iconMaps)
This method allows to update existing icon maps.

### Parameters
(object/array) Icon map properties to be updated.
The iconmapid property must be defined for each icon map, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard icon map properties , the
method accepts the following parameters.

- **mappings** (array): Icon mappings to replace the existing icon mappings.

### Return value
(object) Returns an object containing the IDs of the updated icon maps
under the iconmapids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/iconmap/update

<!-- method: image.create -->
## image.create

### Description
object image.create(object/array images)
This method allows to create new images.

### Parameters
(object/array) Images to create.
The method accepts images with the standard image properties .

### Return value
(object) Returns an object containing the IDs of the created images
under the imageids property. The order of the returned IDs matches the
order of the passed images.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/image/create

<!-- method: image.delete -->
## image.delete

### Description
object image.delete(array imageIds)
This method allows to delete images.

### Parameters
(array) IDs of the images to delete.

### Return value
(object) Returns an object containing the IDs of the deleted images
under the imageids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/image/delete

<!-- method: image.get -->
## image.get

### Description
integer/array image.get(object parameters)
The method allows to retrieve images according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **imageids** (string/array): Return only images with the given IDs.
- **sysmapids** (string/array): Return images that are used on the given maps.
- **select_image** (flag): Return an image property with the Base64 encoded image.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: imageid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/image/get

<!-- method: image.update -->
## image.update

### Description
object image.update(object/array images)
This method allows to update existing images.

### Parameters
(object/array) Image properties to be updated.
The imageid property must be defined for each image, all other properties are optional.
Only the passed properties will be updated, all others will remain unchanged.
The method accepts images with the standard image properties .

### Return value
(object) Returns an object containing the IDs of the updated images
under the imageids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/image/update

<!-- method: item.create -->
## item.create

### Description
object item.create(object/array items)
This method allows to create new items.

### Parameters
(object/array) Items to create.
Additionally to the standard item properties , the method
accepts the following parameters.

- **preprocessing** (array): Item preprocessing options.
- **tags** (array): Item tags .

### Return value
(object) Returns an object containing the IDs of the created items
under the itemids property. The order of the returned IDs matches the
order of the passed items.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/item/create

<!-- method: item.delete -->
## item.delete

### Description
object item.delete(array itemIds)
This method allows to delete items.

### Parameters
(array) IDs of the items to delete.

### Return value
(object) Returns an object containing the IDs of the deleted items
under the itemids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/item/delete

<!-- method: item.get -->
## item.get

### Description
integer/array item.get(object parameters)
The method allows to retrieve items according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **itemids** (string/array): Return only items with the given IDs.
- **groupids** (string/array): Return only items that belong to the hosts from the given groups.
- **templateids** (string/array): Return only items that belong to the given templates.
- **hostids** (string/array): Return only items that belong to the given hosts.
- **proxyids** (string/array): Return only items that are monitored by the given proxies.
- **interfaceids** (string/array): Return only items that use the given host interfaces.
- **graphids** (string/array): Return only items that are used in the given graphs.
- **triggerids** (string/array): Return only items that are used in the given triggers.
- **webitems** (flag): Include web items in the result.
- **inherited** (boolean): If set to true return only items inherited from a template.
- **templated** (boolean): If set to true return only items that belong to templates.
- **monitored** (boolean): If set to true return only enabled items that belong to monitored hosts.
- **group** (string): Return only items that belong to a group with the given name.
- **host** (string): Return only items that belong to a host with the given name.
- **evaltype** (integer): Rules for tag searching. Possible values: 0 - (default) And/Or; 2 - Or.
- **tags** (array of objects): Return only items with given tags. Exact match by tag and case-sensitive or case-insensitive search by tag value depending on operator value. Format: [{"tag": "<tag>", "value": "<value>", "operator": "<operator>"}, ...] . An empty array returns all items. Possible operator types: 0 - (default) Like; 1 - Equal; 2 - Not like; 3 - Not equal 4 - Exists; 5 - Not exists.
- **with_triggers** (boolean): If set to true return only items that are used in triggers.
- **selectHosts** (query): Return a hosts property with an array of hosts that the item belongs to.
- **selectInterfaces** (query): Return an interfaces property with an array of host interfaces used by the item.
- **selectTriggers** (query): Return a triggers property with the triggers that the item is used in. Supports count .
- **selectGraphs** (query): Return a graphs property with the graphs that contain the item. Supports count .
- **selectDiscoveryRule** (query): Return a discoveryRule property with the LLD rule that created the item.
- **selectItemDiscovery** (query): Return an itemDiscovery property with the item discovery object. The item discovery object links the item to an item prototype from which it was created. It has the following properties: itemdiscoveryid - (string) ID of the item discovery; itemid - (string) ID of the discovered item; parent_itemid - (string) ID of the item prototype from which the item has been created; key_ - (string) key of the item prototype; lastcheck - (timestamp) time when the item was last discovered; ts_delete - (timestamp) time when an item that is no longer discovered will be deleted.
- **selectPreprocessing** (query): Return a preprocessing property with item preprocessing options. It has the following properties: type - (string) The preprocessing option type: 1 - Custom multiplier; 2 - Right trim; 3 - Left trim; 4 - Trim; 5 - Regular expression; 6 - Boolean to decimal; 7 - Octal to decimal; 8 - Hexadecimal to decimal; 9 - Simple change; 10 - Change per second; 11 - XML XPath; 12 - JSONPath; 13 - In range; 14 - Matches regular expression; 15 - Does not match regular expression; 16 - Check for error in JSON; 17 - Check for error in XML; 18 - Check for error using regular expression; 19 - Discard unchanged; 20 - Discard unchanged with heartbeat; 21 - JavaScript; 22 - Prometheus pattern; 23 - Prometheus to JSON; 24 - CSV to JSON; 25 - Replace; 26 - Check for not supported value; 27 - XML to JSON; 28 - SNMP walk value; 29 - SNMP walk to JSON. params - (string) Additional parameters used by preprocessing option. Multiple parameters are separated by the newline (\n) character. error_handler - (string) Action type used in case of preprocessing step failure: 0 - Error message is set by Zabbix server; 1 - Discard value; 2 - Set custom value; 3 - Set custom error message. error_handler_params - (string) Error handler parameters.
- **selectTags** (query): Return the item tags in tags property.
- **selectValueMap** (query): Return a valuemap property with item value map.
- **filter** (object): Return only those results that exactly match the given filter. Accepts an array, where the keys are property names, and the values are either a single value or an array of values to match against. Supports additional filters: host - technical name of the host that the item belongs to.
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectGraphs - results will be sorted by name ; selectTriggers - results will be sorted by description .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: itemid , name , key_ , delay , history , trends , type , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/item/get

<!-- method: item.update -->
## item.update

### Description
object item.update(object/array items)
This method allows to update existing items.

### Parameters
(object/array) Item properties to be updated.
The itemid property must be defined for each item, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard item properties , the method
accepts the following parameters.

- **preprocessing** (array): Item preprocessing options to replace the current preprocessing options. Parameter behavior : - read-only for inherited objects or discovered objects
- **tags** (array): Item tags . Parameter behavior : - read-only for discovered objects

### Return value
(object) Returns an object containing the IDs of the updated items
under the itemids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/item/update

<!-- method: itemprototype.create -->
## itemprototype.create

### Description
object itemprototype.create(object/array itemPrototypes)
This method allows to create new item prototypes.

### Parameters
(object/array) Item prototype to create.
Additionally to the standard item prototype
properties , the method accepts the following
parameters.

- **ruleid** (string): ID of the LLD rule that the item belongs to. Parameter behavior : - required
- **preprocessing** (array): Item prototype preprocessing options.
- **tags** (array): Item prototype tags .

### Return value
(object) Returns an object containing the IDs of the created item
prototypes under the itemids property. The order of the returned IDs
matches the order of the passed item prototypes.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/itemprototype/create

<!-- method: itemprototype.delete -->
## itemprototype.delete

### Description
object itemprototype.delete(array itemPrototypeIds)
This method allows to delete item prototypes.

### Parameters
(array) IDs of the item prototypes to delete.

### Return value
(object) Returns an object containing the IDs of the deleted item
prototypes under the prototypeids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/itemprototype/delete

<!-- method: itemprototype.get -->
## itemprototype.get

### Description
integer/array itemprototype.get(object parameters)
The method allows to retrieve item prototypes according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **discoveryids** (string/array): Return only item prototypes that belong to the given LLD rules.
- **graphids** (string/array): Return only item prototypes that are used in the given graph prototypes.
- **hostids** (string/array): Return only item prototypes that belong to the given hosts.
- **inherited** (boolean): If set to true return only item prototypes inherited from a template.
- **itemids** (string/array): Return only item prototypes with the given IDs.
- **monitored** (boolean): If set to true return only enabled item prototypes that belong to monitored hosts.
- **templated** (boolean): If set to true return only item prototypes that belong to templates.
- **templateids** (string/array): Return only item prototypes that belong to the given templates.
- **triggerids** (string/array): Return only item prototypes that are used in the given trigger prototypes.
- **selectDiscoveryRule** (query): Return a discoveryRule property with the low-level discovery rule that the item prototype belongs to.
- **selectGraphs** (query): Return a graphs property with graph prototypes that the item prototype is used in. Supports count .
- **selectHosts** (query): Return a hosts property with an array of hosts that the item prototype belongs to.
- **selectTags** (query): Return the item prototype tags in tags property.
- **selectTriggers** (query): Return a triggers property with trigger prototypes that the item prototype is used in. Supports count .
- **selectPreprocessing** (query): Return a preprocessing property with item preprocessing options. It has the following properties: type - (string) The preprocessing option type: 1 - Custom multiplier; 2 - Right trim; 3 - Left trim; 4 - Trim; 5 - Regular expression; 6 - Boolean to decimal; 7 - Octal to decimal; 8 - Hexadecimal to decimal; 9 - Simple change; 10 - Change per second; 11 - XML XPath; 12 - JSONPath; 13 - In range; 14 - Matches regular expression; 15 - Does not match regular expression; 16 - Check for error in JSON; 17 - Check for error in XML; 18 - Check for error using regular expression; 19 - Discard unchanged; 20 - Discard unchanged with heartbeat; 21 - JavaScript; 22 - Prometheus pattern; 23 - Prometheus to JSON; 24 - CSV to JSON; 25 - Replace; 26 - Check for not supported value; 27 - XML to JSON; 28 - SNMP walk value; 29 - SNMP walk to JSON. params - (string) Additional parameters used by preprocessing option. Multiple parameters are separated by the newline (\n) character. error_handler - (string) Action type used in case of preprocessing step failure: 0 - Error message is set by Zabbix server; 1 - Discard value; 2 - Set custom value; 3 - Set custom error message. error_handler_params - (string) Error handler parameters.
- **selectValueMap** (query): Return a valuemap property with item prototype value map.
- **filter** (object): Return only those results that exactly match the given filter. Accepts an array, where the keys are property names, and the values are either a single value or an array of values to match against. Supports additional filters: host - technical name of the host that the item prototype belongs to.
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectGraphs - results will be sorted by name ; selectTriggers - results will be sorted by description .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: itemid , name , key_ , delay , type , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/itemprototype/get

<!-- method: itemprototype.update -->
## itemprototype.update

### Description
object itemprototype.update(object/array itemPrototypes)
This method allows to update existing item prototypes.

### Parameters
(object/array) Item prototype properties to be updated.
The itemid property must be defined for each item prototype, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard item prototype
properties , the method accepts the following
parameters.

- **preprocessing** (array): Item prototype preprocessing options to replace the current preprocessing options. Parameter behavior : - read-only for inherited objects
- **tags** (array): Item prototype tags .

### Return value
(object) Returns an object containing the IDs of the updated item
prototypes under the itemids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/itemprototype/update

<!-- method: maintenance.create -->
## maintenance.create

### Description
object maintenance.create(object/array maintenances)
This method allows to create new maintenances.

### Parameters
(object/array) Maintenances to create.
Additionally to the standard maintenance
properties , the method accepts the following
parameters.

- **groups** (object/array): Host groups that will undergo maintenance. The host groups must have the groupid property defined. Parameter behavior : - required if hosts is not set
- **hosts** (object/array): Hosts that will undergo maintenance. The hosts must have only the hostid property defined. Parameter behavior : - required if groups is not set
- **timeperiods** (object/array): Maintenance time periods . Parameter behavior : - required
- **tags** (object/array): Problem tags . Define what problems must be suppressed. If no tags are given, all active maintenance host problems will be suppressed. Parameter behavior : - supported if maintenance_type of Maintenance object is set to "with data collection"
- **groupids (deprecated)** (array): This parameter is deprecated, please use groups instead. IDs of the host groups that will undergo maintenance.
- **hostids (deprecated)** (array): This parameter is deprecated, please use hosts instead. IDs of the hosts that will undergo maintenance.

### Return value
(object) Returns an object containing the IDs of the created
maintenances under the maintenanceids property. The order of the
returned IDs matches the order of the passed maintenances.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/maintenance/create

<!-- method: maintenance.delete -->
## maintenance.delete

### Description
object maintenance.delete(array maintenanceIds)
This method allows to delete maintenance periods.

### Parameters
(array) IDs of the maintenance periods to delete.

### Return value
(object) Returns an object containing the IDs of the deleted
maintenance periods under the maintenanceids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/maintenance/delete

<!-- method: maintenance.get -->
## maintenance.get

### Description
integer/array maintenance.get(object parameters)
The method allows to retrieve maintenances according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **groupids** (string/array): Return only maintenances that are assigned to the given host groups.
- **hostids** (string/array): Return only maintenances that are assigned to the given hosts.
- **maintenanceids** (string/array): Return only maintenances with the given IDs.
- **selectHostGroups** (query): Return a hostgroups property with host groups assigned to the maintenance.
- **selectHosts** (query): Return a hosts property with hosts assigned to the maintenance.
- **selectTags** (query): Return a tags property with problem tags of the maintenance.
- **selectTimeperiods** (query): Return a timeperiods property with time periods of the maintenance.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: maintenanceid , name , maintenance_type .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)
- **selectGroups (deprecated)** (query): This parameter is deprecated, please use selectHostGroups instead. Return a groups property with host groups assigned to the maintenance.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/maintenance/get

<!-- method: maintenance.update -->
## maintenance.update

### Description
object maintenance.update(object/array maintenances)
This method allows to update existing maintenances.

### Parameters
(object/array) Maintenance properties to be updated.
The maintenanceid property must be defined for each maintenance, all
other properties are optional. Only the passed properties will be
updated, all others will remain unchanged.
Additionally to the standard maintenance
properties , the method accepts the following
parameters.

- **groups** (object/array): Host groups to replace the current groups. The host groups must have the groupid property defined. Parameter behavior : - required if hosts is not set
- **hosts** (object/array): Hosts to replace the current hosts. The hosts must have only the hostid property defined. Parameter behavior : - required if groups is not set
- **timeperiods** (object/array): Maintenance time periods to replace the current periods.
- **tags** (object/array): Problem tags to replace the current tags. Parameter behavior : - supported if maintenance_type of Maintenance object is set to "with data collection"
- **groupids (deprecated)** (array): This parameter is deprecated, please use groups instead. IDs of the host groups that will undergo maintenance.
- **hostids (deprecated)** (array): This parameter is deprecated, please use hosts instead. IDs of the hosts that will undergo maintenance.

### Return value
(object) Returns an object containing the IDs of the updated
maintenances under the maintenanceids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/maintenance/update

<!-- method: map.create -->
## map.create

### Description
object map.create(object/array maps)
This method allows to create new maps.

### Parameters
(object/array) Maps to create.
Additionally to the standard map properties , the method
accepts the following parameters.

- **links** (array): Map links to be created on the map.
- **selements** (array): Map elements to be created on the map.
- **urls** (array): Map URLs to be created on the map.
- **users** (array): Map user shares to be created on the map.
- **userGroups** (array): Map user group shares to be created on the map.
- **shapes** (array): Map shapes to be created on the map.
- **lines** (array): Map lines to be created on the map.

### Return value
(object) Returns an object containing the IDs of the created maps
under the sysmapids property. The order of the returned IDs matches
the order of the passed maps.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/map/create

<!-- method: map.delete -->
## map.delete

### Description
object map.delete(array mapIds)
This method allows to delete maps.

### Parameters
(array) IDs of the maps to delete.

### Return value
(object) Returns an object containing the IDs of the deleted maps
under the sysmapids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/map/delete

<!-- method: map.get -->
## map.get

### Description
integer/array map.get(object parameters)
The method allows to retrieve maps according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **sysmapids** (string/array): Returns only maps with the given IDs.
- **userids** (string/array): Returns only maps that belong to the given user IDs.
- **expandUrls** (flag): Adds global map URLs to the corresponding map elements and expands macros in all map element URLs.
- **selectIconMap** (query): Returns an iconmap property with the icon map used on the map.
- **selectLinks** (query): Returns a links property with the map links between elements.
- **selectSelements** (query): Returns a selements property with the map elements.
- **selectUrls** (query): Returns a urls property with the map URLs.
- **selectUsers** (query): Returns a users property with users that the map is shared with.
- **selectUserGroups** (query): Returns a userGroups property with user groups that the map is shared with.
- **selectShapes** (query): Returns a shapes property with the map shapes.
- **selectLines** (query): Returns a lines property with the map lines.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: name , width , height .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/map/get

<!-- method: map.update -->
## map.update

### Description
object map.update(object/array maps)
This method allows to update existing maps.

### Parameters
(object/array) Map properties to be updated.
The mapid property must be defined for each map, all other properties
are optional. Only the passed properties will be updated, all others
will remain unchanged.
Additionally to the standard map properties , the method
accepts the following parameters.

- **links** (array): Map links to replace the existing links.
- **selements** (array): Map elements to replace the existing elements.
- **urls** (array): Map URLs to replace the existing URLs.
- **users** (array): Map user shares to replace the existing elements.
- **userGroups** (array): Map user group shares to replace the existing elements.
- **shapes** (array): Map shapes to replace the existing shapes.
- **lines** (array): Map lines to replace the existing lines.

### Return value
(object) Returns an object containing the IDs of the updated maps
under the sysmapids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/map/update

<!-- method: mediatype.create -->
## mediatype.create

### Description
object mediatype.create(object/array mediaTypes)
This method allows to create new media types.

### Parameters
(object/array) Media types to create.
Additionally to the standard media type properties ,
the method accepts the following parameters.

- **parameters** (array): Script or webhook parameters to be created for the media type.
- **message_templates** (array): Message templates to be created for the media type.

### Return value
(object) Returns an object containing the IDs of the created media
types under the mediatypeids property. The order of the returned IDs
matches the order of the passed media types.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/mediatype/create

<!-- method: mediatype.delete -->
## mediatype.delete

### Description
object mediatype.delete(array mediaTypeIds)
This method allows to delete media types.

### Parameters
(array) IDs of the media types to delete.

### Return value
(object) Returns an object containing the IDs of the deleted media
types under the mediatypeids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/mediatype/delete

<!-- method: mediatype.get -->
## mediatype.get

### Description
integer/array mediatype.get(object parameters)
The method allows to retrieve media types according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **mediatypeids** (string/array): Return only media types with the given IDs.
- **mediaids** (string/array): Return only media types used by the given media .
- **userids** (string/array): Return only media types used by the given users.
- **selectMessageTemplates** (query): Return a message_templates property with an array of media type messages. Parameter behavior : - supported for Super admin type users (since Zabbix 6.4.19)
- **selectUsers** (query): Return a users property with the users that use the media type.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: mediatypeid .
- **filter** (object): Return only those results that exactly match the given filter. Accepts an object, where the keys are property names, and the values are either a single value or an array of values to match against. Supported properties for Super admin type users: all Media type object properties, except properties of text data type . Supported properties for Admin type users (since Zabbix 6.4.19): mediatypeid , name , type , status , maxattempts .
- **output** (query): Media type object properties to be returned. Since Zabbix 6.4.19, Admin type users may retrieve only the following Media type object properties: mediatypeid , name , type , status , maxattempts . For an example, see Retrieving media types as Admin . Default: extend .
- **search** (object): Return results that match the given pattern (case-insensitive). Accepts an object, where the keys are property names, and the values are strings to search for. If no additional options are given, this will perform a LIKE "%…%" search. Supported properties for Super admin type users: all Media type object properties of string and text data type . Supported properties for Admin type users (since Zabbix 6.4.19): name , description .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **limit** (integer)
- **preservekeys** (boolean)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/mediatype/get

<!-- method: mediatype.update -->
## mediatype.update

### Description
object mediatype.update(object/array mediaTypes)
This method allows to update existing media types.

### Parameters
(object/array) Media type properties to be updated.
The mediatypeid property must be defined for each media type, all
other properties are optional. Only the passed properties will be
updated, all others will remain unchanged.
Additionally to the standard media type properties ,
the method accepts the following parameters.

- **parameters** (array): Script or webhook parameters to replace the current parameters.
- **message_templates** (array): Message templates to replace the current message templates.

### Return value
(object) Returns an object containing the IDs of the updated media
types under the mediatypeids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/mediatype/update

<!-- method: module.create -->
## module.create

### Description
object module.create(object/array modules)
This method allows to install new frontend modules.

### Parameters
(object/array) Modules to create.
The method accepts modules with the standard module properties .

### Return value
(object) Returns an object containing the IDs of the installed modules under the moduleids property.
The order of the returned IDs matches the order of the passed modules.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/module/create

<!-- method: module.delete -->
## module.delete

### Description
object module.delete(array moduleids)
This method allows to uninstall modules.

### Parameters
(array) IDs of the modules to uninstall.

### Return value
(object) Returns an object containing the IDs of the uninstalled modules under the moduleids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/module/delete

<!-- method: module.get -->
## module.get

### Description
integer/array module.get(object parameters)
The method allows to retrieve modules according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **moduleids** (string/array): Return only modules with the given IDs.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: moduleid , relative_path .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the Reference commentary page.
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/module/get

<!-- method: module.update -->
## module.update

### Description
object module.update(object/array modules)
This method allows to update existing modules.

### Parameters
(object/array) Module properties to be updated.
The moduleid property must be defined for each module, all other properties are optional.
Only the specified properties will be updated.
The method accepts modules with the standard module properties .

### Return value
(object) Returns an object containing the IDs of the updated modules under the moduleids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/module/update

<!-- method: problem.get -->
## problem.get

### Description
integer/array problem.get(object parameters)
The method allows to retrieve problems according to the given
parameters.
This method is for retrieving unresolved problems. It is also possible,
if specified, to additionally retrieve recently resolved problems. The
period that determines how old is "recently" is defined in Administration → General .
Problems that were resolved prior to that period are not kept in the
problem table. To retrieve problems that were resolved further back in
the past, use the event.get method.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **eventids** (string/array): Return only problems with the given IDs.
- **groupids** (string/array): Return only problems created by objects that belong to the given host groups.
- **hostids** (string/array): Return only problems created by objects that belong to the given hosts.
- **objectids** (string/array): Return only problems created by the given objects.
- **source** (integer): Return only problems with the given type. Refer to the problem event object page for a list of supported event types. Default: 0 - problem created by a trigger.
- **object** (integer): Return only problems created by objects of the given type. Refer to the problem event object page for a list of supported object types. Default: 0 - trigger.
- **acknowledged** (boolean): true - return acknowledged problems only; false - unacknowledged only.
- **suppressed** (boolean): true - return only suppressed problems; false - return problems in the normal state.
- **symptom** (boolean): true - return only symptom problem events; false - return only cause problem events.
- **severities** (integer/array): Return only problems with given event severities. Applies only if object is trigger.
- **evaltype** (integer): Rules for tag searching. Possible values: 0 - (default) And/Or; 2 - Or.
- **tags** (array of objects): Return only problems with given tags. Exact match by tag and case-insensitive search by value and operator. Format: [{"tag": "<tag>", "value": "<value>", "operator": "<operator>"}, ...] . An empty array returns all problems. Possible operator types: 0 - (default) Like; 1 - Equal; 2 - Not like; 3 - Not equal 4 - Exists; 5 - Not exists.
- **recent** (boolean): true - return PROBLEM and recently RESOLVED problems (depends on Display OK triggers for N seconds) Default: false - UNRESOLVED problems only
- **eventid_from** (string): Return only problems with IDs greater or equal to the given ID.
- **eventid_till** (string): Return only problems with IDs less or equal to the given ID.
- **time_from** (timestamp): Return only problems that have been created after or at the given time.
- **time_till** (timestamp): Return only problems that have been created before or at the given time.
- **selectAcknowledges** (query): Return an acknowledges property with the problem updates. Problem updates are sorted in reverse chronological order. The problem update object has the following properties: acknowledgeid - (string) update's ID; userid - (string) ID of the user that updated the event; eventid - (string) ID of the updated event; clock - (timestamp) time when the event was updated; message - (string) text of the message; action - (integer) type of update action (see event.acknowledge ); old_severity - (integer) event severity before this update action; new_severity - (integer) event severity after this update action; suppress_until - (timestamp) time till event will be suppressed; taskid - (string) ID of task if current event is undergoing a rank change; Supports count .
- **selectTags** (query): Return a tags property with the problem tags. Output format: [{"tag": "<tag>", "value": "<value>"}, ...] .
- **selectSuppressionData** (query): Return a suppression_data property with the list of active maintenances and manual suppressions: maintenanceid - (string) ID of the maintenance; userid - (string) ID of user who suppressed the problem; suppress_until - (integer) time until the problem is suppressed.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: eventid .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/problem/get

<!-- method: proxy.create -->
## proxy.create

### Description
object proxy.create(object/array proxies)
This method allows to create new proxies.

### Parameters
(object/array) Proxies to create.
Additionally to the standard proxy properties , the method accepts the following parameters.

- **hosts** (array): Hosts to be monitored by the proxy. If a host is already monitored by a different proxy, it will be reassigned to the current proxy. The hosts must have the hostid property defined.
- **interface** (object): Host interface to be created for the passive proxy. Parameter behavior : - required if status of Proxy object is set to "passive proxy"

### Return value
(object) Returns an object containing the IDs of the created proxies under the proxyids property. The order of the
returned IDs matches the order of the passed proxies.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/proxy/create

<!-- method: proxy.delete -->
## proxy.delete

### Description
object proxy.delete(array proxies)
This method allows to delete proxies.

### Parameters
(array) IDs of proxies to delete.

### Return value
(object) Returns an object containing the IDs of the deleted proxies under the proxyids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/proxy/delete

<!-- method: proxy.get -->
## proxy.get

### Description
integer/array proxy.get(object parameters)
The method allows to retrieve proxies according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **proxyids** (string/array): Return only proxies with the given IDs.
- **selectHosts** (query): Return a hosts property with the hosts monitored by the proxy.
- **selectInterface** (query): Return an interface property with the proxy interface used by a passive proxy.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: hostid , host , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/proxy/get

<!-- method: proxy.update -->
## proxy.update

### Description
object proxy.update(object/array proxies)
This method allows to update existing proxies.

### Parameters
(object/array) Proxy properties to be updated.
The proxyid property must be defined for each proxy, all other properties are optional. Only the passed properties
will be updated, all others will remain unchanged.
Additionally to the standard proxy properties , the method accepts the following parameters.

- **hosts** (array): Hosts to be monitored by the proxy. If a host is already monitored by a different proxy, it will be reassigned to the current proxy. The hosts must have the hostid property defined.
- **interface** (object): Host interface to replace the existing interface for the passive proxy. Parameter behavior : - supported if status of Proxy object is set to "passive proxy"

### Return value
(object) Returns an object containing the IDs of the updated proxies under the proxyids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/proxy/update

<!-- method: regexp.create -->
## regexp.create

### Description
object regexp.create(object/array regularExpressions)
This method allows to create new global regular expressions.

### Parameters
(object/array) Regular expressions to create.
Additionally to the standard properties , the method accepts
the following parameters.

- **expressions** (array): Expressions options. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the created regular
expressions under the regexpids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/regexp/create

<!-- method: regexp.delete -->
## regexp.delete

### Description
object regexp.delete(array regexpids)
This method allows to delete global regular expressions.

### Parameters
(array) IDs of the regular expressions to delete.

### Return value
(object) Returns an object containing the IDs of the deleted regular
expressions under the regexpids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/regexp/delete

<!-- method: regexp.get -->
## regexp.get

### Description
integer/array regexp.get(object parameters)
The method allows to retrieve global regular expressions according to
the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **regexpids** (string/array): Return only regular expressions with the given IDs.
- **selectExpressions** (query): Return a expressions property.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: regexpid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/regexp/get

<!-- method: regexp.update -->
## regexp.update

### Description
object regexp.update(object/array regularExpressions)
This method allows to update existing global regular expressions.

### Parameters
(object/array) Regular expression properties to be updated.
The regexpid property must be defined for each object, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard properties ,
the method accepts the following parameters.

- **expressions** (array): Expressions options.

### Return value
(object) Returns an object containing the IDs of the updated regular
expressions under the regexpids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/regexp/update

<!-- method: report.create -->
## report.create

### Description
object report.create(object/array reports)
This method allows to create new scheduled reports.

### Parameters
(object/array) Scheduled reports to create.
Additionally to the standard scheduled report
properties , the method accepts the following parameters.

- **users** (object/array): Users to send the report to. Parameter behavior : - required if user_groups is not set
- **user_groups** (object/array): User groups to send the report to. Parameter behavior : - required if users is not set

### Return value
(object) Returns an object containing the IDs of the created scheduled
reports under the reportids property. The order of the returned IDs
matches the order of the passed scheduled reports.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/report/create

<!-- method: report.delete -->
## report.delete

### Description
object report.delete(array reportids)
This method allows to delete scheduled reports.

### Parameters
(array) IDs of the scheduled reports to delete.

### Return value
(object) Returns an object containing the IDs of the deleted scheduled
reports under the reportids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/report/delete

<!-- method: report.get -->
## report.get

### Description
integer/array report.get(object parameters)
The method allows to retrieve scheduled reports according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **reportids** (string/array): Return only scheduled reports with the given report IDs.
- **expired** (boolean): If set to true returns only expired scheduled reports, if false - only active scheduled reports.
- **selectUsers** (query): Return a users property the report is configured to be sent to.
- **selectUserGroups** (query): Return a user_groups property the report is configured to be sent to.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: reportid , name , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/report/get

<!-- method: report.update -->
## report.update

### Description
object report.update(object/array reports)
This method allows to update existing scheduled reports.

### Parameters
(object/array) Scheduled report properties to be updated.
The reportid property must be defined for each scheduled report, all
other properties are optional. Only the passed properties will be
updated, all others will remain unchanged.
Additionally to the standard scheduled report
properties the method accepts the following parameters.

- **users** (object/array): Users to replace the current users assigned to the scheduled report. Parameter behavior : - required if user_groups is not set
- **user_groups** (object/array): User groups to replace the current user groups assigned to the scheduled report. Parameter behavior : - required if users is not set

### Return value
(object) Returns an object containing the IDs of the updated scheduled
reports under the reportids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/report/update

<!-- method: role.create -->
## role.create

### Description
object role.create(object/array roles)
This method allows to create new roles.

### Parameters
(object/array) Roles to create.
Additionally to the standard role properties , the method
accepts the following parameters.

- **rules** (array): Role rules to be created for the role.

### Return value
(object) Returns an object containing the IDs of the created roles
under the roleids property. The order of the returned IDs matches the
order of the passed roles.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/role/create

<!-- method: role.delete -->
## role.delete

### Description
object role.delete(array roleids)
This method allows to delete roles.

### Parameters
(array) IDs of the roles to delete.

### Return value
(object) Returns an object containing the IDs of the deleted roles
under the roleids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/role/delete

<!-- method: role.get -->
## role.get

### Description
integer/array role.get(object parameters)
The method allows to retrieve roles according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **roleids** (string/array): Return only roles with the given IDs.
- **selectRules** (query): Return role rules in the rules property.
- **selectUsers** (query): Select users this role is assigned to.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: roleid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/role/get

<!-- method: role.update -->
## role.update

### Description
object role.update(object/array roles)
This method allows to update existing roles.

### Parameters
(object/array) Role properties to be updated.
The roleid property must be defined for each role, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard role properties the method
accepts the following parameters.

- **rules** (array): Access rules to update for the role.

### Return value
(object) Returns an object containing the IDs of the updated roles
under the roleids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/role/update

<!-- method: script.create -->
## script.create

### Description
object script.create(object/array scripts)
This method allows to create new scripts.

### Parameters
(object/array) Scripts to create.
The method accepts scripts with the standard script
properties .

### Return value
(object) Returns an object containing the IDs of the created scripts
under the scriptids property. The order of the returned IDs matches
the order of the passed scripts.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/script/create

<!-- method: script.delete -->
## script.delete

### Description
object script.delete(array scriptIds)
This method allows to delete scripts.

### Parameters
(array) IDs of the scripts to delete.

### Return value
(object) Returns an object containing the IDs of the deleted scripts
under the scriptids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/script/delete

<!-- method: script.execute -->
## script.execute

### Description
object script.execute(object parameters)
This method allows to run a script on a host or event. Except for URL type scripts. Those are not executable.

### Parameters
(object) Parameters containing the ID of the script to run and either
the ID of the host or the ID of the event.

- **scriptid** (string): ID of the script to run. Parameter behavior : - required
- **hostid** (string): ID of the host to run the script on. Parameter behavior : - required if eventid is not set
- **eventid** (string): ID of the event to run the script on. Parameter behavior : - required if hostid is not set

### Return value
(object) Returns the result of script execution.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/script/execute

<!-- method: script.get -->
## script.get

### Description
integer/array script.get(object parameters)
The method allows to retrieve scripts according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **groupids** (string/array): Return only scripts that can be run on the given host groups.
- **hostids** (string/array): Return only scripts that can be run on the given hosts.
- **scriptids** (string/array): Return only scripts with the given IDs.
- **usrgrpids** (string/array): Return only scripts that can be run by users in the given user groups.
- **selectHostGroups** (query): Return a hostgroups property with host groups that the script can be run on.
- **selectHosts** (query): Return a hosts property with hosts that the script can be run on.
- **selectActions** (query): Return a actions property with actions that the script is associated with.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: scriptid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)
- **selectGroups (deprecated)** (query): This parameter is deprecated, please use selectHostGroups instead. Return a groups property with host groups that the script can be run on.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/script/get

<!-- method: script.getscriptsbyevents -->
## script.getscriptsbyevents

### Description
object script.getscriptsbyevents(array eventIds)
This method allows to retrieve scripts available to the given events.

### Parameters
(string/array) IDs of events to return scripts for.

### Return value
(object) Returns an object with event IDs as properties and arrays of
available scripts as values.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/script/getscriptsbyevents

<!-- method: script.getscriptsbyhosts -->
## script.getscriptsbyhosts

### Description
object script.getscriptsbyhosts(array hostIds)
This method allows to retrieve scripts available on the given hosts.

### Parameters
(string/array) IDs of hosts to return scripts for.

### Return value
(object) Returns an object with host IDs as properties and arrays of
available scripts as values.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/script/getscriptsbyhosts

<!-- method: script.update -->
## script.update

### Description
object script.update(object/array scripts)
This method allows to update existing scripts.

### Parameters
(object/array) Script properties to be updated.
The scriptid property must be defined for each script, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged. An exception is type property change
from 5 (Webhook) to other: the parameters property will be cleaned.

### Return value
(object) Returns an object containing the IDs of the updated scripts
under the scriptids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/script/update

<!-- method: service.create -->
## service.create

### Description
object service.create(object/array services)
This method allows to create new services.

### Parameters
(object/array) services to create.
Additionally to the standard service properties , the
method accepts the following parameters.

- **children** (array): Child services to be linked to the service. The children must have the serviceid property defined.
- **parents** (array): Parent services to be linked to the service. The parents must have the serviceid property defined.
- **tags** (array): Service tags to be created for the service.
- **problem_tags** (array): Problem tags to be created for the service.
- **status_rules** (array): Status rules to be created for the service.

### Return value
(object) Returns an object containing the IDs of the created services
under the serviceids property. The order of the returned IDs matches
the order of the passed services.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/service/create

<!-- method: service.delete -->
## service.delete

### Description
object service.delete(array serviceIds)
This method allows to delete services.

### Parameters
(array) IDs of the services to delete.

### Return value
(object) Returns an object containing the IDs of the deleted services
under the serviceids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/service/delete

<!-- method: service.get -->
## service.get

### Description
integer/array service.get(object parameters)
The method allows to retrieve services according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **serviceids** (string/array): Return only services with the given IDs.
- **parentids** (string/array): Return only services that are linked to the given parent services.
- **deep_parentids** (flag): Return all direct and indirect child services. Used together with parentids .
- **childids** (string/array): Return only services that are linked to the given child services.
- **evaltype** (integer): Rules for tag searching. Possible values: 0 - (default) And/Or; 2 - Or.
- **tags** (object/array): Return only services with given tags. Exact match by tag and case-sensitive or case-insensitive search by tag value depending on operator value. Format: [{"tag": "<tag>", "value": "<value>", "operator": "<operator>"}, ...] . An empty array returns all services. Possible operator values: 0 - (default) Contains; 1 - Equals; 2 - Does not contain; 3 - Does not equal; 4 - Exists; 5 - Does not exist.
- **problem_tags** (object/array): Return only services with given problem tags. Exact match by tag and case-sensitive or case-insensitive search by tag value depending on operator value. Format: [{"tag": "<tag>", "value": "<value>", "operator": "<operator>"}, ...] . An empty array returns all services. Possible operator values: 0 - (default) Contains; 1 - Equals; 2 - Does not contain; 3 - Does not equal; 4 - Exists; 5 - Does not exist.
- **without_problem_tags** (flag): Return only services without problem tags.
- **slaids** (string/array): Return only services that are linked to the specific SLA(s).
- **selectChildren** (query): Return a children property with the child services. Supports count .
- **selectParents** (query): Return a parents property with the parent services. Supports count .
- **selectTags** (query): Return a tags property with service tags. Supports count .
- **selectProblemEvents** (query): Return a problem_events property with an array of problem event objects. The problem event object has the following properties: eventid - (string) Event ID; severity - (string) Current event severity; name - (string) Resolved event name. Supports count .
- **selectProblemTags** (query): Return a problem_tags property with problem tags. Supports count .
- **selectStatusRules** (query): Return a status_rules property with status rules. Supports count .
- **selectStatusTimeline** (object/array): Return a status_timeline property containing service state changes for given periods. Format [{"period_from": "<period_from>", "period_to": "<period_to>"}, ...] - period_from being a starting date (inclusive; integer timestamp) and period_to being an ending date (exclusive; integer timestamp) for the period you're interested in. Returns an array of entries containing a start_value property and an alarms array for the state changes within specified periods.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: serviceid , name , status , sortorder , created_at .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/service/get

<!-- method: service.update -->
## service.update

### Description
object service.update(object/array services)
This method allows to update existing services.

### Parameters
(object/array) service properties to be updated.
The serviceid property must be defined for each service, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard service properties , the
method accepts the following parameters.

- **children** (array): Child services to replace the current service children. The children must have the serviceid property defined.
- **parents** (array): Parent services to replace the current service parents. The parents must have the serviceid property defined.
- **tags** (array): Service tags to replace the current service tags.
- **problem_tags** (array): Problem tags to replace the current problem tags.
- **status_rules** (array): Status rules to replace the current status rules.

### Return value
(object) Returns an object containing the IDs of the updated services
under the serviceids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/service/update

<!-- method: settings.get -->
## settings.get

### Description
object settings.get(object parameters)
The method allows to retrieve settings object according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports only one parameter.

- **output** (query): This parameter being common for all get methods described in the reference commentary .

### Return value
(object) Returns settings object.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/get

<!-- method: settings.update -->
## settings.update

### Description
object settings.update(object settings)
This method allows to update existing common settings.

### Parameters
(object) Settings properties to be updated.

### Return value
(array) Returns an array with the names of updated parameters.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/settings/update

<!-- method: sla.create -->
## sla.create

### Description
object sla.create(object/array SLAs)
This method allows to create new SLA objects.

### Parameters
(object/array) SLA objects to create.
Additionally to the standard SLA properties , the
method accepts the following parameters.

- **service_tags** (array): SLA service tags to be created for the SLA. Parameter behavior : - required
- **schedule** (array): SLA schedule to be created for the SLA. Specifying an empty parameter will be interpreted as a 24x7 schedule. Default: 24x7 schedule.
- **excluded_downtimes** (array): SLA excluded downtimes to be created for the SLA.

### Return value
(object) Returns an object containing the IDs of the created SLAs
under the slaids property. The order of the returned IDs matches
the order of the passed SLAs.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/sla/create

<!-- method: sla.delete -->
## sla.delete

### Description
object sla.delete(array slaids)
This method allows to delete SLA entries.

### Parameters
(array) IDs of the SLAs to delete.

### Return value
(object) Returns an object containing the IDs of the deleted SLAs
under the slaids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/sla/delete

<!-- method: sla.get -->
## sla.get

### Description
integer/array sla.get(object parameters)
The method allows to retrieve SLA objects according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **slaids** (string/array): Return only SLAs with the given IDs.
- **serviceids** (string/array): Return only SLAs matching the specific services.
- **selectSchedule** (query): Return a schedule property with SLA schedules. Supports count .
- **selectExcludedDowntimes** (query): Return an excluded_downtimes property with SLA excluded downtimes. Supports count .
- **selectServiceTags** (query): Return a service_tags property with SLA service tags. Supports count .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: slaid , name , period , slo , effective_date , timezone , status , description .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/sla/get

<!-- method: sla.getsli -->
## sla.getsli

### Description
object sla.getsli(object parameters)
This method allows to calculate the Service Level Indicator (SLI) data for a Service Level Agreement (SLA).

### Parameters
(object) Parameters containing the SLA ID, reporting periods and, optionally,
the IDs of the services - to calculate the SLI for.
The following table demonstrates the arrangement of returned period slices based on combinations of parameters.

- **slaid** (string): ID of the SLA to return availability information for. Parameter behavior : - required
- **period_from** (timestamp): Starting date (inclusive) to report the SLI for. Possible values: timestamp.
- **period_to** (timestamp): Ending date (exclusive) to report the SLI for. Possible values: timestamp.
- **periods** (array): Preferred number of periods to report. Possible values: 1-100
- **serviceids** (string/array): IDs of services to return the SLI for.
- **period_from** (period_to)
- **-** (-): Return the last 20 periods.
- **-** (-): Return the last periods specified by the periods parameter.
- **-** (specified): Return the last 20 periods before the specified period_to date.
- **-** (specified): Return the last periods specified by the periods parameter before the specified period_to date.
- **specified** (-): Return the first 20 periods starting with the specified period_from date.
- **specified** (-): Return the first periods specified by the periods parameter starting with the specified period_from date.
- **specified** (specified): Return up to 100 periods within the specified date range.
- **specified** (specified): Return periods specified by the periods parameter within the specified date range.

### Return value
(object) Returns the results of the calculation.
The SLI data returned for each reported period and service consists of:

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/sla/getsli

<!-- method: sla.update -->
## sla.update

### Description
object sla.update(object/array slaids)
This method allows to update existing SLA entries.

### Parameters
(object/array) SLA properties to be updated.
The slaid property must be defined for each SLA, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard SLA properties , the
method accepts the following parameters.

- **service_tags** (array): SLA service tags to replace the current SLA service tags.
- **schedule** (array): SLA schedule to replace the current one. Specifying parameter as empty will be interpreted as a 24x7 schedule.
- **excluded_downtimes** (array): SLA excluded downtimes to replace the current ones.

### Return value
(object) Returns an object containing the IDs of the updated SLAs under the slaids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/sla/update

<!-- method: task.create -->
## task.create

### Description
object task.create(object/array tasks)
This method allows to create a new task (such as collect diagnostic data
or check items or low-level discovery rules without config reload).

### Parameters
(object/array) A task to create.
The method accepts tasks with the standard task properties .
Note that 'Execute now' tasks can be created only for the following
types of items/discovery rules:
- Zabbix agent
- SNMPv1/v2/v3 agent
- Simple check
- Internal check
- External check
- Database monitor
- HTTP agent
- IPMI agent
- SSH agent
- TELNET agent
- Calculated check
- JMX agent
- Dependent item
If item or discovery rule is of type "Dependent item", then top level master item must be of type:
- Zabbix agent
- SNMPv1/v2/v3 agent
- Simple check
- Internal check
- External check
- Database monitor
- HTTP agent
- IPMI agent
- SSH agent
- TELNET agent
- Calculated check
- JMX agent

### Return value
(object) Returns an object containing the IDs of the created tasks
under the taskids property. One task is created for each item and
low-level discovery rule. The order of the returned IDs matches the
order of the passed itemids .

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/task/create

<!-- method: task.get -->
## task.get

### Description
integer/array task.get(object parameters)
The method allows to retrieve tasks according to the given parameters.
Method returns details only about 'diagnostic information' tasks.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **taskids** (string/array): Return only tasks with the given IDs.
- **output** (query): These parameters being common for all get methods are described in detail in the reference commentary .
- **preservekeys** (boolean)

### Return value
(integer/array) Returns an array of objects.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/task/get

<!-- method: template.create -->
## template.create

### Description
object template.create(object/array templates)
This method allows to create new templates.

### Parameters
(object/array) Templates to create.
Additionally to the standard template properties , the
method accepts the following parameters.

- **groups** (object/array): Template groups to add the template to. The template groups must have the groupid property defined. Parameter behavior : - required
- **tags** (object/array): Template tags .
- **templates** (object/array): Templates to be linked to the template. The templates must have the templateid property defined.
- **macros** (object/array): User macros to be created for the template.

### Return value
(object) Returns an object containing the IDs of the created templates
under the templateids property. The order of the returned IDs matches
the order of the passed templates.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/template/create

<!-- method: template.delete -->
## template.delete

### Description
object template.delete(array templateIds)
This method allows to delete templates.
Deleting a template will cause deletion of all template entities (items,
triggers, graphs, etc.). To leave template entities with the hosts, but
delete the template itself, first unlink the template from required
hosts using one of these methods: template.update , template.massupdate , host.update , host.massupdate .

### Parameters
(array) IDs of the templates to delete.

### Return value
(object) Returns an object containing the IDs of the deleted templates
under the templateids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/template/delete

<!-- method: template.get -->
## template.get

### Description
integer/array template.get(object parameters)
The method allows to retrieve templates according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **templateids** (string/array): Return only templates with the given template IDs.
- **groupids** (string/array): Return only templates that belong to the given template groups.
- **parentTemplateids** (string/array): Return only templates that the given template is linked to.
- **hostids** (string/array): Return only templates that are linked to the given hosts/templates.
- **graphids** (string/array): Return only templates that contain the given graphs.
- **itemids** (string/array): Return only templates that contain the given items.
- **triggerids** (string/array): Return only templates that contain the given triggers.
- **with_items** (flag): Return only templates that have items.
- **with_triggers** (flag): Return only templates that have triggers.
- **with_graphs** (flag): Return only templates that have graphs.
- **with_httptests** (flag): Return only templates that have web scenarios.
- **evaltype** (integer): Rules for tag searching. Possible values: 0 - (default) And/Or; 2 - Or.
- **tags** (object/array): Return only templates with given tags. Exact match by tag and case-sensitive or case-insensitive search by tag value depending on operator value. Format: [{"tag": "<tag>", "value": "<value>", "operator": "<operator>"}, ...] . An empty array returns all templates. Possible operator values: 0 - (default) Contains; 1 - Equals; 2 - Not like; 3 - Not equal 4 - Exists; 5 - Not exists.
- **selectTags** (query): Return template tags in the tags property.
- **selectHosts** (query): Return the hosts that are linked to the template in the hosts property. Supports count .
- **selectTemplateGroups** (query): Return the template groups that the template belongs to in the templategroups property.
- **selectTemplates** (query): Return templates to which the given template is linked in the templates property. Supports count .
- **selectParentTemplates** (query): Return templates that are linked to the given template in the parentTemplates property. Supports count .
- **selectHttpTests** (query): Return the web scenarios from the template in the httpTests property. Supports count .
- **selectItems** (query): Return items from the template in the items property. Supports count .
- **selectDiscoveries** (query): Return low-level discoveries from the template in the discoveries property. Supports count .
- **selectTriggers** (query): Return triggers from the template in the triggers property. Supports count .
- **selectGraphs** (query): Return graphs from the template in the graphs property. Supports count .
- **selectMacros** (query): Return the macros from the template in the macros property..
- **selectDashboards** (query): Return dashboards from the template in the dashboards property. Supports count .
- **selectValueMaps** (query): Return a valuemaps property with template value maps.
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectTemplates - results will be sorted by name ; selectHosts - sorted by host ; selectParentTemplates - sorted by host ; selectItems - sorted by name ; selectDiscoveries - sorted by name ; selectTriggers - sorted by description ; selectGraphs - sorted by name ; selectDashboards - sorted by name .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: hostid , host , name , status .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)
- **selectGroups (deprecated)** (query): This parameter is deprecated, please use selectTemplateGroups instead. Return the template groups that the template belongs to in the groups property.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/template/get

<!-- method: template.massadd -->
## template.massadd

### Description
object template.massadd(object parameters)
This method allows to simultaneously add multiple related objects to the
given templates.

### Parameters
(object) Parameters containing the IDs of the templates to update and
the objects to add to the templates.
The method accepts the following parameters.

- **templates** (object/array): Templates to be updated. The templates must have the templateid property defined. Parameter behavior : - required
- **groups** (object/array): Template groups to add the given templates to. The template groups must have the groupid property defined.
- **macros** (object/array): User macros to be created for the given templates.
- **templates_link** (object/array): Templates to link to the given templates. The templates must have the templateid property defined.

### Return value
(object) Returns an object containing the IDs of the updated templates
under the templateids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/template/massadd

<!-- method: template.massremove -->
## template.massremove

### Description
object template.massremove(object parameters)
This method allows to remove related objects from multiple templates.

### Parameters
(object) Parameters containing the IDs of the templates to update and
the objects that should be removed.

- **templateids** (string/array): IDs of the templates to be updated. Parameter behavior : - required
- **groupids** (string/array): Template groups from which to remove the given templates.
- **macros** (string/array): User macros to delete from the given templates.
- **templateids_clear** (string/array): Templates to unlink and clear from the given templates (upstream).
- **templateids_link** (string/array): Templates to unlink from the given templates (upstream).

### Return value
(object) Returns an object containing the IDs of the updated templates
under the templateids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/template/massremove

<!-- method: template.massupdate -->
## template.massupdate

### Description
object template.massupdate(object parameters)
This method allows to simultaneously replace or remove related objects
and update properties on multiple templates.

### Parameters
(object) Parameters containing the IDs of the templates to update and the objects to replace for the templates.
The method accepts the following parameters.

- **templates** (object/array): Templates to be updated. The templates must have the templateid property defined. Parameter behavior : - required
- **groups** (object/array): Template groups to replace the current template groups the templates belong to. The template groups must have the groupid property defined.
- **macros** (object/array): User macros to replace all of the current user macros on the given templates.
- **templates_clear** (object/array): Templates to unlink and clear from the given templates. The templates must have the templateid property defined.
- **templates_link** (object/array): Templates to replace the currently linked templates. The templates must have the templateid property defined.

### Return value
(object) Returns an object containing the IDs of the updated templates
under the templateids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/template/massupdate

<!-- method: template.update -->
## template.update

### Description
object template.update(object/array templates)
This method allows to update existing templates.

### Parameters
(object/array) Template properties to be updated.
The templateid property must be defined for each template, all other
properties are optional. Only the given properties will be updated, all
others will remain unchanged.
Additionally to the standard template properties , the
method accepts the following parameters.

- **groups** (object/array): Template groups to replace the current template groups the templates belong to. The template groups must have the groupid property defined.
- **tags** (object/array): Template tags to replace the current template tags.
- **macros** (object/array): User macros to replace the current user macros on the given templates.
- **templates** (object/array): Templates to replace the currently linked templates. Templates that are not passed are only unlinked. The templates must have the templateid property defined.
- **templates_clear** (object/array): Templates to unlink and clear from the given templates. The templates must have the templateid property defined.

### Return value
(object) Returns an object containing the IDs of the updated templates
under the templateids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/template/update

<!-- method: templatedashboard.create -->
## templatedashboard.create

### Description
object templatedashboard.create(object/array templateDashboards)
This method allows to create new template dashboards.

### Parameters
(object/array) Template dashboards to create.
Additionally to the standard template dashboard
properties , the method accepts the following
parameters.

- **pages** (array): Template dashboard pages to be created for the dashboard. Dashboard pages will be ordered in the same order as specified. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the created template
dashboards under the dashboardids property. The order of the returned
IDs matches the order of the passed template dashboards.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templatedashboard/create

<!-- method: templatedashboard.delete -->
## templatedashboard.delete

### Description
object templatedashboard.delete(array templateDashboardIds)
This method allows to delete template dashboards.

### Parameters
(array) IDs of the template dashboards to delete.

### Return value
(object) Returns an object containing the IDs of the deleted template
dashboards under the dashboardids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templatedashboard/delete

<!-- method: templatedashboard.get -->
## templatedashboard.get

### Description
integer/array templatedashboard.get(object parameters)
The method allows to retrieve template dashboards according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **dashboardids** (string/array): Return only template dashboards with the given IDs.
- **templateids** (string/array): Return only template dashboards that belong to the given templates.
- **selectPages** (query): Return a pages property with template dashboard pages, correctly ordered.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: dashboardid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templatedashboard/get

<!-- method: templatedashboard.update -->
## templatedashboard.update

### Description
object templatedashboard.update(object/array templateDashboards)
This method allows to update existing template dashboards.

### Parameters
(object/array) Template dashboard properties to be updated.
The dashboardid property must be specified for each dashboard, all
other properties are optional. Only the specified properties will be
updated.
Additionally to the standard template dashboard
properties , the method accepts the following
parameters.

- **pages** (array): Template dashboard pages to replace the existing dashboard pages. Dashboard pages are updated by the dashboard_pageid property. New dashboard pages will be created for objects without dashboard_pageid property and the existing dashboard pages will be deleted if not reused. Dashboard pages will be ordered in the same order as specified. Only the specified properties of the dashboard pages will be updated. At least one dashboard page object is required for pages property.

### Return value
(object) Returns an object containing the IDs of the updated template
dashboards under the dashboardids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templatedashboard/update

<!-- method: templategroup.create -->
## templategroup.create

### Description
object templategroup.create(object/array templateGroups)
This method allows to create new template groups.

### Parameters
(object/array) Template groups to create. The method accepts template groups
with the standard template group properties .

### Return value
(object) Returns an object containing the IDs of the created template
groups under the groupids property. The order of the returned IDs
matches the order of the passed template groups.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templategroup/create

<!-- method: templategroup.delete -->
## templategroup.delete

### Description
object templategroup.delete(array templateGroupIds)
This method allows to delete template groups.
A template group can not be deleted if it contains templates that belong to this group only.

### Parameters
(array) IDs of the template groups to delete.

### Return value
(object) Returns an object containing the IDs of the deleted template
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templategroup/delete

<!-- method: templategroup.get -->
## templategroup.get

### Description
integer/array templategroup.get(object parameters)
The method allows to retrieve template groups according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **graphids** (string/array): Return only template groups that contain templates with the given graphs.
- **groupids** (string/array): Return only template groups with the given template group IDs.
- **templateids** (string/array): Return only template groups that contain the given templates.
- **triggerids** (string/array): Return only template groups that contain templates with the given triggers.
- **with_graphs** (flag): Return only template groups that contain templates with graphs.
- **with_graph_prototypes** (flag): Return only template groups that contain templates with graph prototypes.
- **with_httptests** (flag): Return only template groups that contain templates with web checks.
- **with_items** (flag): Return only template groups that contain templates with items. Overrides the with_simple_graph_items parameters.
- **with_item_prototypes** (flag): Return only template groups that contain templates with item prototypes. Overrides the with_simple_graph_item_prototypes parameter.
- **with_simple_graph_item_prototypes** (flag): Return only template groups that contain templates with item prototypes, which are enabled for creation and have numeric type of information.
- **with_simple_graph_items** (flag): Return only template groups that contain templates with numeric items.
- **with_templates** (flag): Return only template groups that contain templates.
- **with_triggers** (flag): Return only template groups that contain templates with triggers.
- **selectTemplates** (query): Return a templates property with the templates that belong to the template group. Supports count .
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectTemplates - results will be sorted by template .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: groupid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templategroup/get

<!-- method: templategroup.massadd -->
## templategroup.massadd

### Description
object templategroup.massadd(object parameters)
This method allows to simultaneously add multiple related objects to all
the given template groups.

### Parameters
(object) Parameters containing the IDs of the template groups to update
and the objects to add to all the template groups.
The method accepts the following parameters.

- **groups** (object/array): Template groups to be updated. The template groups must have the groupid property defined. Parameter behavior : - required
- **templates** (object/array): Templates to add to all template groups. The templates must have the templateid property defined. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the updated template
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templategroup/massadd

<!-- method: templategroup.massremove -->
## templategroup.massremove

### Description
object templategroup.massremove(object parameters)
This method allows to remove related objects from multiple template groups.

### Parameters
(object) Parameters containing the IDs of the template groups to update
and the objects that should be removed.

- **groupids** (string/array): IDs of the template groups to be updated. Parameter behavior : - required
- **templateids** (string/array): Templates to remove from all template groups. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the updated template
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templategroup/massremove

<!-- method: templategroup.massupdate -->
## templategroup.massupdate

### Description
object templategroup.massupdate(object parameters)
This method allows to replace templates with the specified
ones in multiple template groups.

### Parameters
(object) Parameters containing the IDs of the template groups to update
and the objects that should be updated.

- **groups** (object/array): Template groups to be updated. The template groups must have the groupid property defined. Parameter behavior : - required
- **templates** (object/array): Templates to replace the current template on the given template groups. All other template, except the ones mentioned, will be excluded from template groups. The templates must have the templateid property defined. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the updated template
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templategroup/massupdate

<!-- method: templategroup.propagate -->
## templategroup.propagate

### Description
object templategroup.propagate(object parameters)
This method allows to apply permissions to all template groups' subgroups.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **groups** (object/array): Template groups to propagate. The template groups must have the groupid property defined. Parameter behavior : - required
- **permissions** (boolean): Set true if need to propagate permissions. Parameter behavior : - required

### Return value
(object) Returns an object containing the IDs of the propagated template
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templategroup/propagate

<!-- method: templategroup.update -->
## templategroup.update

### Description
object templategroup.update(object/array templateGroups)
This method allows to update existing template groups.

### Parameters
(object/array) Template group properties to be
updated.
The groupid property must be defined for each template group, all other
properties are optional. Only the given properties will be updated, all
others will remain unchanged.

### Return value
(object) Returns an object containing the IDs of the updated template
groups under the groupids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/templategroup/update

<!-- method: token.create -->
## token.create

### Description
object token.create(object/array tokens)
This method allows to create new tokens.

### Parameters
(object/array) Tokens to create.
The method accepts tokens with the standard token properties .

### Return value
(object) Returns an object containing the IDs of the created tokens
under the tokenids property. The order of the returned IDs matches the
order of the passed tokens.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/token/create

<!-- method: token.delete -->
## token.delete

### Description
object token.delete(array tokenids)
This method allows to delete tokens.

### Parameters
(array) IDs of the tokens to delete.

### Return value
(object) Returns an object containing the IDs of the deleted tokens
under the tokenids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/token/delete

<!-- method: token.generate -->
## token.generate

### Description
object token.generate(array tokenids)
This method allows to generate tokens.

### Parameters
(array) IDs of the tokens to generate.

### Return value
(array) Returns an array of objects containing the ID of the generated
token under the tokenid property and generated authorization string
under token property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/token/generate

<!-- method: token.get -->
## token.get

### Description
integer/array token.get(object parameters)
The method allows to retrieve tokens according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **tokenids** (string/array): Return only tokens with the given IDs.
- **userids** (string/array): Return only tokens created for the given users.
- **token** (string): Return only tokens created for the given Auth token .
- **valid_at** (timestamp): Return only tokens, which are valid (not expired) at the given date and time.
- **expired_at** (timestamp): Return only tokens, which are expired (not valid) at the given date and time.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: tokenid , name , lastaccess , status , expires_at , created_at .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/token/get

<!-- method: token.update -->
## token.update

### Description
object token.update(object/array tokens)
This method allows to update existing tokens.

### Parameters
(object/array) Token properties to be updated.
The tokenid property must be defined for each token, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
The method accepts tokens with the standard token properties .

### Return value
(object) Returns an object containing the IDs of the updated tokens
under the tokenids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/token/update

<!-- method: trend.get -->
## trend.get

### Description
integer/array trend.get(object parameters)
The method allows to retrieve trend data according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **itemids** (string/array): Return only trends with the given item IDs.
- **time_from** (timestamp): Return only values that have been collected after or at the given time.
- **time_till** (timestamp): Return only values that have been collected before or at the given time.
- **countOutput** (boolean): Count the number of retrieved objects.
- **limit** (integer): Limit the amount of retrieved objects.
- **output** (query): Set Trend object properties to be returned.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/trend/get

<!-- method: trigger.create -->
## trigger.create

### Description
object trigger.create(object/array triggers)
This method allows to create new triggers.

### Parameters
(object/array) Triggers to create.
Additionally to the standard trigger properties the
method accepts the following parameters.

- **dependencies** (array): Triggers that the trigger is dependent on. The triggers must have the triggerid property defined.
- **tags** (array): Trigger tags.

### Return value
(object) Returns an object containing the IDs of the created triggers
under the triggerids property. The order of the returned IDs matches
the order of the passed triggers.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/trigger/create

<!-- method: trigger.delete -->
## trigger.delete

### Description
object trigger.delete(array triggerIds)
This method allows to delete triggers.

### Parameters
(array) IDs of the triggers to delete.

### Return value
(object) Returns an object containing the IDs of the deleted triggers
under the triggerids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/trigger/delete

<!-- method: trigger.get -->
## trigger.get

### Description
integer/array trigger.get(object parameters)
The method allows to retrieve triggers according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **triggerids** (string/array): Return only triggers with the given IDs.
- **groupids** (string/array): Return only triggers that belong to hosts or templates from the given host groups or template groups.
- **templateids** (string/array): Return only triggers that belong to the given templates.
- **hostids** (string/array): Return only triggers that belong to the given hosts.
- **itemids** (string/array): Return only triggers that contain the given items.
- **functions** (string/array): Return only triggers that use the given functions. Refer to the supported function page for a list of supported functions.
- **group** (string): Return only triggers that belong to hosts or templates from the host group or template group with the given name.
- **host** (string): Return only triggers that belong to host with the given technical name.
- **inherited** (boolean): If set to true return only triggers inherited from a template.
- **templated** (boolean): If set to true return only triggers that belong to templates.
- **dependent** (boolean): If set to true return only triggers that have dependencies. If set to false return only triggers that do not have dependencies.
- **monitored** (flag): Return only enabled triggers that belong to monitored hosts and contain only enabled items.
- **active** (flag): Return only enabled triggers that belong to monitored hosts.
- **maintenance** (boolean): If set to true return only enabled triggers that belong to hosts in maintenance.
- **withUnacknowledgedEvents** (flag): Return only triggers that have unacknowledged events.
- **withAcknowledgedEvents** (flag): Return only triggers with all events acknowledged.
- **withLastEventUnacknowledged** (flag): Return only triggers with the last event unacknowledged.
- **skipDependent** (flag): Skip triggers in a problem state that are dependent on other triggers. Note that the other triggers are ignored if disabled, have disabled items or disabled item hosts.
- **lastChangeSince** (timestamp): Return only triggers that have changed their state after the given time.
- **lastChangeTill** (timestamp): Return only triggers that have changed their state before the given time.
- **only_true** (flag): Return only triggers that have recently been in a problem state.
- **min_severity** (integer): Return only triggers with severity greater or equal than the given severity.
- **evaltype** (integer): Rules for tag searching. Possible values: 0 - (default) And/Or; 2 - Or.
- **tags** (array of objects): Return only triggers with given tags. Exact match by tag and case-sensitive or case-insensitive search by tag value depending on operator value. Format: [{"tag": "<tag>", "value": "<value>", "operator": "<operator>"}, ...] . An empty array returns all triggers. Possible operator types: 0 - (default) Like; 1 - Equal; 2 - Not like; 3 - Not equal 4 - Exists; 5 - Not exists.
- **expandComment** (flag): Expand macros in the trigger description.
- **expandDescription** (flag): Expand macros in the name of the trigger.
- **expandExpression** (flag): Expand functions and macros in the trigger expression.
- **selectHostGroups** (query): Return the host groups that the trigger belongs to in the hostgroups property.
- **selectHosts** (query): Return the hosts that the trigger belongs to in the hosts property.
- **selectItems** (query): Return items contained by the trigger in the items property.
- **selectFunctions** (query): Return functions used in the trigger in the functions property. The function objects represent the functions used in the trigger expression and has the following properties: functionid - (string) ID of the function; itemid - (string) ID of the item used in the function; function - (string) name of the function; parameter - (string) parameter passed to the function. Query parameter is replaced by $ symbol in returned string.
- **selectDependencies** (query): Return triggers that the trigger depends on in the dependencies property.
- **selectDiscoveryRule** (query): Return the low-level discovery rule that created the trigger.
- **selectLastEvent** (query): Return the last significant trigger event in the lastEvent property.
- **selectTags** (query): Return the trigger tags in tags property.
- **selectTemplateGroups** (query): Return the template groups that the trigger belongs to in the templategroups property.
- **selectTriggerDiscovery** (query): Return the trigger discovery object in the triggerDiscovery property. The trigger discovery objects link the trigger to a trigger prototype from which it was created. It has the following properties: parent_triggerid - (string) ID of the trigger prototype from which the trigger has been created.
- **filter** (object): Return only those results that exactly match the given filter. Accepts an array, where the keys are property names, and the values are either a single value or an array of values to match against. Supports additional filters: host - technical name of the host that the trigger belongs to; hostid - ID of the host that the trigger belongs to.
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectHosts - results will be sorted by host .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: triggerid , description , status , priority , lastchange , hostname .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)
- **selectGroups (deprecated)** (query): This parameter is deprecated, please use selectHostGroups or selectTemplateGroups instead. Return the host groups and template groups that the trigger belongs to in the groups property.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/trigger/get

<!-- method: trigger.update -->
## trigger.update

### Description
object trigger.update(object/array triggers)
This method allows to update existing triggers.

### Parameters
(object/array) Trigger properties to be updated.
The triggerid property must be defined for each trigger, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard trigger properties the
method accepts the following parameters.

- **dependencies** (array): Triggers that the trigger is dependent on. The triggers must have the triggerid property defined.
- **tags** (array): Trigger tags.

### Return value
(object) Returns an object containing the IDs of the updated triggers
under the triggerids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/trigger/update

<!-- method: triggerprototype.create -->
## triggerprototype.create

### Description
object triggerprototype.create(object/array triggerPrototypes)
This method allows to create new trigger prototypes.

### Parameters
(object/array) Trigger prototypes to create.
Additionally to the standard trigger prototype
properties the method accepts the following
parameters.

- **dependencies** (array): Triggers and trigger prototypes that the trigger prototype is dependent on. The triggers must have the triggerid property defined.
- **tags** (array): Trigger prototype tags .

### Return value
(object) Returns an object containing the IDs of the created trigger
prototypes under the triggerids property. The order of the returned
IDs matches the order of the passed trigger prototypes.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/triggerprototype/create

<!-- method: triggerprototype.delete -->
## triggerprototype.delete

### Description
object triggerprototype.delete(array triggerPrototypeIds)
This method allows to delete trigger prototypes.

### Parameters
(array) IDs of the trigger prototypes to delete.

### Return value
(object) Returns an object containing the IDs of the deleted trigger
prototypes under the triggerids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/triggerprototype/delete

<!-- method: triggerprototype.get -->
## triggerprototype.get

### Description
integer/array triggerprototype.get(object parameters)
The method allows to retrieve trigger prototypes according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **active** (flag): Return only enabled trigger prototypes that belong to monitored hosts.
- **discoveryids** (string/array): Return only trigger prototypes that belong to the given LLD rules.
- **functions** (string/array): Return only triggers that use the given functions. Refer to the Supported functions page for a list of supported functions.
- **group** (string): Return only trigger prototypes that belong to hosts or templates from the host groups or template groups with the given name.
- **groupids** (string/array): Return only trigger prototypes that belong to hosts or templates from the given host groups or template groups.
- **host** (string): Return only trigger prototypes that belong to hosts with the given name.
- **hostids** (string/array): Return only trigger prototypes that belong to the given hosts.
- **inherited** (boolean): If set to true return only trigger prototypes inherited from a template.
- **maintenance** (boolean): If set to true return only enabled trigger prototypes that belong to hosts in maintenance.
- **min_severity** (integer): Return only trigger prototypes with severity greater or equal than the given severity.
- **monitored** (flag): Return only enabled trigger prototypes that belong to monitored hosts and contain only enabled items.
- **templated** (boolean): If set to true return only trigger prototypes that belong to templates.
- **templateids** (string/array): Return only trigger prototypes that belong to the given templates.
- **triggerids** (string/array): Return only trigger prototypes with the given IDs.
- **expandExpression** (flag): Expand functions and macros in the trigger expression.
- **selectDependencies** (query): Return trigger prototypes and triggers that the trigger prototype depends on in the dependencies property.
- **selectDiscoveryRule** (query): Return the LLD rule that the trigger prototype belongs to.
- **selectFunctions** (query): Return functions used in the trigger prototype in the functions property. The function objects represent the functions used in the trigger expression and has the following properties: functionid - (string) ID of the function; itemid - (string) ID of the item used in the function; function - (string) name of the function; parameter - (string) parameter passed to the function. Query parameter is replaced by $ symbol in returned string.
- **selectHostGroups** (query): Return the host groups that the trigger prototype belongs to in the hostgroups property.
- **selectHosts** (query): Return the hosts that the trigger prototype belongs to in the hosts property.
- **selectItems** (query): Return items and item prototypes used the trigger prototype in the items property.
- **selectTags** (query): Return the trigger prototype tags in tags property.
- **selectTemplateGroups** (query): Return the template groups that the trigger prototype belongs to in the templategroups property.
- **filter** (object): Return only those results that exactly match the given filter. Accepts an array, where the keys are property names, and the values are either a single value or an array of values to match against. Supports additional filters: host - technical name of the host that the trigger prototype belongs to; hostid - ID of the host that the trigger prototype belongs to.
- **limitSelects** (integer): Limits the number of records returned by subselects. Applies to the following subselects: selectHosts - results will be sorted by host .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: triggerid , description , status , priority .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)
- **selectGroups (deprecated)** (query): This parameter is deprecated, please use selectHostGroups or selectTemplateGroups instead. Return the host groups and template groups that the trigger prototype belongs to in the groups property.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/triggerprototype/get

<!-- method: triggerprototype.update -->
## triggerprototype.update

### Description
object triggerprototype.update(object/array triggerPrototypes)
This method allows to update existing trigger prototypes.

### Parameters
(object/array) Trigger prototype properties to be updated.
The triggerid property must be defined for each trigger prototype, all
other properties are optional. Only the passed properties will be
updated, all others will remain unchanged.
Additionally to the standard trigger prototype
properties the method accepts the following
parameters.

- **dependencies** (array): Triggers and trigger prototypes that the trigger prototype is dependent on. The triggers must have the triggerid property defined.
- **tags** (array): Trigger prototype tags .

### Return value
(object) Returns an object containing the IDs of the updated trigger
prototypes under the triggerids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/triggerprototype/update

<!-- method: user.checkauthentication -->
## user.checkauthentication

### Description
object user.checkAuthentication
This method checks and prolongs the user session.

### Parameters
The method accepts the following parameters.

- **extend** (boolean): Whether to prolong the user session. Default value: "true". Setting the value to "false" allows to check the user session without prolonging it. Parameter behavior : - supported if sessionid is set
- **sessionid** (string): User authentication token . Parameter behavior : - required if token is not set
- **secret** (string): Random 32 characters string. Is generated on user login.
- **token** (string): User API token . Parameter behavior : - required if sessionid is not set

### Return value
(object) Returns an object containing information about the user.
Additionally to the standard user properties , the following information is returned.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/checkauthentication

<!-- method: user.create -->
## user.create

### Description
object user.create(object/array users)
This method allows to create new users.

### Parameters
(object/array) Users to create.
Additionally to the standard user properties , the method
accepts the following parameters.

- **usrgrps** (array): User groups to add the user to. The user groups must have the usrgrpid property defined.
- **medias** (array): User media to be created.

### Return value
(object) Returns an object containing the IDs of the created users
under the userids property. The order of the returned IDs matches the
order of the passed users.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/create

<!-- method: user.delete -->
## user.delete

### Description
object user.delete(array users)
This method allows to delete users.

### Parameters
(array) IDs of users to delete.

### Return value
(object) Returns an object containing the IDs of the deleted users
under the userids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/delete

<!-- method: user.get -->
## user.get

### Description
integer/array user.get(object parameters)
The method allows to retrieve users according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **mediaids** (string/array): Return only users that use the given media.
- **mediatypeids** (string/array): Return only users that use the given media types.
- **userids** (string/array): Return only users with the given IDs.
- **usrgrpids** (string/array): Return only users that belong to the given user groups.
- **getAccess** (flag): Adds additional information about user permissions. Adds the following properties for each user: gui_access - (integer) user's frontend authentication method. Refer to the gui_access property of the user group object for a list of possible values. debug_mode - (integer) indicates whether debug is enabled for the user. Possible values: 0 - debug disabled, 1 - debug enabled. users_status - (integer) indicates whether the user is disabled. Possible values: 0 - user enabled, 1 - user disabled.
- **selectMedias** (query): Return media used by the user in the medias property.
- **selectMediatypes** (query): Return media types used by the user in the mediatypes property.
- **selectUsrgrps** (query): Return user groups that the user belongs to in the usrgrps property.
- **selectRole** (query): Return user role in the role property.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: userid , username .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/get

<!-- method: user.login -->
## user.login

### Description
string/object user.login(object parameters)
This method allows to log in to the API and generate an authentication
token.

### Parameters
(object) Parameters containing the user name and password.
The method accepts the following parameters.

- **password** (string): User password. Parameter behavior : - required
- **username** (string): User name. Parameter behavior : - required
- **userData** (flag): Return information about the authenticated user.

### Return value
(string/object) If the userData parameter is used, returns an object
containing information about the authenticated user.
Additionally to the standard user properties , the
following information is returned:
If the userData parameter is not used, the method returns an
authentication token.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/login

<!-- method: user.logout -->
## user.logout

### Description
string/object user.logout(array)
This method allows to log out of the API and invalidates the current
authentication token.

### Parameters
(array) The method accepts an empty array.

### Return value
(boolean) Returns true if the user has been logged out successfully.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/logout

<!-- method: user.provision -->
## user.provision

### Description
object user.provision(object/array users)
This method allows to provision LDAP users.

### Parameters
(array) IDs of users to provision.

### Return value
(object) Returns an object containing the IDs of the provisioned users under the userids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/provision

<!-- method: user.unblock -->
## user.unblock

### Description
object user.unblock(array userids)
This method allows to unblock users.

### Parameters
(array) IDs of users to unblock.

### Return value
(object) Returns an object containing the IDs of the unblocked users
under the userids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/unblock

<!-- method: user.update -->
## user.update

### Description
object user.update(object/array users)
This method allows to update existing users.

### Parameters
(object/array) User properties to be updated.
The userid property must be defined for each user, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard user properties , the method
accepts the following parameters.

- **current_passwd** (string): User's current password. The value of this parameter can be an empty string if the user is linked to a user directory . Parameter behavior : - write-only - required if passwd of User object is set and user changes own user password
- **usrgrps** (array): User groups to replace existing user groups. The user groups must have the usrgrpid property defined.
- **medias** (array): User media to replace existing media.

### Return value
(object) Returns an object containing the IDs of the updated users
under the userids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/user/update

<!-- method: userdirectory.create -->
## userdirectory.create

### Description
object userdirectory.create(object/array userDirectory)
This method allows to create new user directories.

### Parameters
(object/array) User directories to create.
The method accepts user directories with the standard user directory properties .

### Return value
(object) Returns an object containing the IDs of the created user directories under the userdirectoryids property.
The order of the returned IDs matches the order of the passed user directories.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/userdirectory/create

<!-- method: userdirectory.delete -->
## userdirectory.delete

### Description
object userdirectory.delete(array userDirectoryIds)
This method allows to delete user directories. User directory cannot be deleted when it is directly used for at least one user group. Default LDAP user directory cannot be deleted when authentication.ldap_configured is set to 1 or when there are more user directories left.

### Parameters
(array) IDs of the user directories to delete.

### Return value
(object) Returns an object containing the IDs of the deleted user directories under the userdirectoryids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/userdirectory/delete

<!-- method: userdirectory.get -->
## userdirectory.get

### Description
integer/array userdirectory.get(object parameters)
The method allows to retrieve user directories according to the given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **userdirectoryids** (string/array): Return only user directories with the given IDs.
- **selectUsrgrps** (query): Return a usrgrps property with user groups associated with a user directory. Supports count .
- **selectProvisionMedia** (query): Return a provision_media property with media type mappings associated with a user directory.
- **selectProvisionGroups** (query): Return a provision_groups property with provisioning groups mappings associated with a user directory.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: name .
- **filter** (object): Return only those results that exactly match the given filter. Accepts an object, where the keys are property names, and the values are either a single value or an array of values. Supported keys: userdirectoryid , idp_type , provision_status .
- **search** (object): Return results that match the given pattern (case-insensitive). br> Accepts an object, where the keys are property names, and the values are strings to search for. If no additional options are given, this will perform a LIKE "%…%" search. Supported properties: name , description . User directory of type SAML will have an empty value for both name and description fields. Both fields can be changed with userdirectory.update operation.
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **excludeSearch** (boolean)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/userdirectory/get

<!-- method: userdirectory.test -->
## userdirectory.test

### Description
object userdirectory.test(array userDirectory)
This method allows to test user directory connection settings.

### Parameters
(object) User directory properties.
Since userdirectory.get API does not return bind_password field, userdirectoryid and/or bind_password should be supplied. Additionally to the standard user directory properties , the method accepts the following parameters.

- **test_username** (string): Username to test in user directory.
- **test_password** (string): Username associated password to test in user directory.

### Return value
(bool) Returns true on success.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/userdirectory/test

<!-- method: userdirectory.update -->
## userdirectory.update

### Description
object userdirectory.update(object/array userDirectory)
This method allows to update existing user directories.

### Parameters
(object/array) User directory properties to be updated.
The userdirectoryid property must be defined for each user directory, all other properties are optional.
Only the passed properties will be updated, all others will remain unchanged.

### Return value
(object) Returns an object containing the IDs of the updated user directories
under the userdirectoryids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/userdirectory/update

<!-- method: usergroup.create -->
## usergroup.create

### Description
object usergroup.create(object/array userGroups)
This method allows to create new user groups.

### Parameters
(object/array) User groups to create.
Additionally to the standard user group properties ,
the method accepts the following parameters.

- **hostgroup_rights** (object/array): Host group permissions to assign to the user group.
- **templategroup_rights** (object/array): Template group permissions to assign to the user group.
- **tag_filters** (array): Tag-based permissions to assign to the user group.
- **users** (object/array): Users to add to the user group. The user must have the userid property defined.
- **rights (deprecated)** (object/array): This parameter is deprecated, please use hostgroup_rights or templategroup_rights instead. Permissions to assign to the user group.

### Return value
(object) Returns an object containing the IDs of the created user
groups under the usrgrpids property. The order of the returned IDs
matches the order of the passed user groups.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/usergroup/create

<!-- method: usergroup.delete -->
## usergroup.delete

### Description
object usergroup.delete(array userGroupIds)
This method allows to delete user groups.

### Parameters
(array) IDs of the user groups to delete.

### Return value
(object) Returns an object containing the IDs of the deleted user
groups under the usrgrpids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/usergroup/delete

<!-- method: usergroup.get -->
## usergroup.get

### Description
integer/array usergroup.get(object parameters)
The method allows to retrieve user groups according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **status** (integer): Return only user groups with the given status. Refer to the user group page for a list of supported statuses.
- **userids** (string/array): Return only user groups that contain the given users.
- **usrgrpids** (string/array): Return only user groups with the given IDs.
- **selectTagFilters** (query): Return user group tag based permissions in the tag_filters property. It has the following properties: groupid - (string) ID of the host group; tag - (string) tag name; value - (string) tag value.
- **selectUsers** (query): Return the users from the user group in the users property.
- **selectHostGroupRights** (query): Return user group host group rights in the hostgroup_rights property. It has the following properties: permission - (integer) access level to the host group; id - (string) ID of the host group. Refer to the user group page for a list of access levels to host groups.
- **selectTemplateGroupRights** (query): Return user group template group rights in the templategroup_rights property. It has the following properties: permission - (integer) access level to the template group; id - (string) ID of the template group. Refer to the user group page for a list of access levels to template groups.
- **limitSelects** (integer): Limits the number of records returned by subselects.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: usrgrpid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)
- **selectRights (deprecated)** (query): This parameter is deprecated, please use selectHostGroupRights or selectTemplateGroupRights instead. Return user group rights in the rights property. It has the following properties: permission - (integer) access level to the host group; id - (string) ID of the host group. Refer to the user group page for a list of access levels to host groups.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/usergroup/get

<!-- method: usergroup.update -->
## usergroup.update

### Description
object usergroup.update(object/array userGroups)
This method allows to update existing user groups.

### Parameters
(object/array) User group properties to be updated.
The usrgrpid property must be defined for each user group, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.
Additionally to the standard user group properties ,
the method accepts the following parameters.

- **hostgroup_rights** (object/array): Host group permissions to replace the current permissions assigned to the user group.
- **templategroup_rights** (object/array): Template group permissions to replace the current permissions assigned to the user group.
- **tag_filters** (array): Tag-based permissions to replace the current permissions assigned to the user group.
- **users** (object/array): Users to replace the current users assigned to the user group. The user must have only the userid property defined.
- **rights (deprecated)** (object/array): This parameter is deprecated, please use hostgroup_rights or templategroup_rights instead. Permissions to assign to the user group.

### Return value
(object) Returns an object containing the IDs of the updated user
groups under the usrgrpids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/usergroup/update

<!-- method: usermacro.create -->
## usermacro.create

### Description
object usermacro.create(object/array hostMacros)
This method allows to create new host macros.

### Parameters
(object/array) Host macros to create.
The method accepts host macros with the standard host macro
properties .

### Return value
(object) Returns an object containing the IDs of the created host
macros under the hostmacroids property. The order of the returned IDs
matches the order of the passed host macros.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/usermacro/create

<!-- method: usermacro.createglobal -->
## usermacro.createglobal

### Description
object usermacro.createglobal(object/array globalMacros)
This method allows to create new global macros.

### Parameters
(object/array) Global macros to create.
The method accepts global macros with the standard global macro
properties .

### Return value
(object) Returns an object containing the IDs of the created global
macros under the globalmacroids property. The order of the returned
IDs matches the order of the passed global macros.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/usermacro/createglobal

<!-- method: usermacro.delete -->
## usermacro.delete

### Description
object usermacro.delete(array hostMacroIds)
This method allows to delete host macros.

### Parameters
(array) IDs of the host macros to delete.

### Return value
(object) Returns an object containing the IDs of the deleted host
macros under the hostmacroids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/usermacro/delete

<!-- method: usermacro.deleteglobal -->
## usermacro.deleteglobal

### Description
object usermacro.deleteglobal(array globalMacroIds)
This method allows to delete global macros.

### Parameters
(array) IDs of the global macros to delete.

### Return value
(object) Returns an object containing the IDs of the deleted global
macros under the globalmacroids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/usermacro/deleteglobal

<!-- method: usermacro.get -->
## usermacro.get

### Description
integer/array usermacro.get(object parameters)
The method allows to retrieve host and global macros according to the
given parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **globalmacro** (flag): Return global macros instead of host macros.
- **globalmacroids** (string/array): Return only global macros with the given IDs.
- **groupids** (string/array): Return only host macros that belong to hosts or templates from the given host groups or template groups.
- **hostids** (string/array): Return only macros that belong to the given hosts or templates.
- **hostmacroids** (string/array): Return only host macros with the given IDs.
- **inherited** (boolean): If set to true return only host prototype user macros inherited from a template.
- **selectHostGroups** (query): Return host groups that the host macro belongs to in the hostgroups property. Used only when retrieving host macros.
- **selectHosts** (query): Return hosts that the host macro belongs to in the hosts property. Used only when retrieving host macros.
- **selectTemplateGroups** (query): Return template groups that the template macro belongs to in the templategroups property. Used only when retrieving template macros.
- **selectTemplates** (query): Return templates that the host macro belongs to in the templates property. Used only when retrieving host macros.
- **sortfield** (string/array): Sort the result by the given properties. Possible values: macro .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary page.
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)
- **selectGroups (deprecated)** (query): This parameter is deprecated, please use selectHostGroups or selectTemplateGroups instead. Return host groups and template groups that the host macro belongs to in the groups property. Used only when retrieving host macros.

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/usermacro/get

<!-- method: usermacro.update -->
## usermacro.update

### Description
object usermacro.update(object/array hostMacros)
This method allows to update existing host macros.

### Parameters
(object/array) Host macro properties to be
updated.
The hostmacroid property must be defined for each host macro, all
other properties are optional. Only the passed properties will be
updated, all others will remain unchanged.

### Return value
(object) Returns an object containing the IDs of the updated host
macros under the hostmacroids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/usermacro/update

<!-- method: usermacro.updateglobal -->
## usermacro.updateglobal

### Description
object usermacro.updateglobal(object/array globalMacros)
This method allows to update existing global macros.

### Parameters
(object/array) Global macro properties to be
updated.
The globalmacroid property must be defined for each global macro, all
other properties are optional. Only the passed properties will be
updated, all others will remain unchanged.

### Return value
(object) Returns an object containing the IDs of the updated global
macros under the globalmacroids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/usermacro/updateglobal

<!-- method: valuemap.create -->
## valuemap.create

### Description
object valuemap.create(object/array valuemaps)
This method allows to create new value maps.

### Parameters
(object/array) Value maps to create.
The method accepts value maps with the standard value map
properties .

### Return value
(object) Returns an object containing the IDs of the created value
maps the valuemapids property. The order of the returned IDs matches
the order of the passed value maps.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/valuemap/create

<!-- method: valuemap.delete -->
## valuemap.delete

### Description
object valuemap.delete(array valuemapids)
This method allows to delete value maps.

### Parameters
(array) IDs of the value maps to delete.

### Return value
(object) Returns an object containing the IDs of the deleted value
maps under the valuemapids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/valuemap/delete

<!-- method: valuemap.get -->
## valuemap.get

### Description
integer/array valuemap.get(object parameters)
The method allows to retrieve value maps according to the given
parameters.

### Parameters
(object) Parameters defining the desired output.
The method supports the following parameters.

- **valuemapids** (string/array): Return only value maps with the given IDs.
- **selectMappings** (query): Return the value mappings for current value map in the mappings property. Supports count .
- **sortfield** (string/array): Sort the result by the given properties. Possible values: valuemapid , name .
- **countOutput** (boolean): These parameters being common for all get methods are described in detail in the reference commentary .
- **editable** (boolean)
- **excludeSearch** (boolean)
- **filter** (object)
- **limit** (integer)
- **output** (query)
- **preservekeys** (boolean)
- **search** (object)
- **searchByAny** (boolean)
- **searchWildcardsEnabled** (boolean)
- **sortorder** (string/array)
- **startSearch** (boolean)

### Return value
(integer/array) Returns either:
- an array of objects;
- the count of retrieved objects, if the countOutput parameter has
been used.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/valuemap/get

<!-- method: valuemap.update -->
## valuemap.update

### Description
object valuemap.update(object/array valuemaps)
This method allows to update existing value maps.

### Parameters
(object/array) Value map properties to be updated.
The valuemapid property must be defined for each value map, all other
properties are optional. Only the passed properties will be updated, all
others will remain unchanged.

### Return value
(object) Returns an object containing the IDs of the updated value
maps under the valuemapids property.

Source: https://www.zabbix.com/documentation/6.4/en/manual/api/reference/valuemap/update

