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
