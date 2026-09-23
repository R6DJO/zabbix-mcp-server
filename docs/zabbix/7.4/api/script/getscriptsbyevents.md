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
