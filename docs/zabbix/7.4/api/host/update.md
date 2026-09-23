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
