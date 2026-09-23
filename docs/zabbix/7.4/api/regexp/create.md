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
