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
