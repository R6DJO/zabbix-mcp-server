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
