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
