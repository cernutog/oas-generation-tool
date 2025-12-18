# Full Remediation Log
Complete list of differences detected between Original and Current templates.

## $index.xlsm
### Sheet: General Description
- **Column 1** (2 edits):
  - '/fpad' -> '' **(x1 rows)**
  - '' -> '/fpad' **(x1 rows)**
- **Column 3** (2 edits):
  - 'Server base path' -> '' **(x1 rows)**
  - '' -> 'Server base path' **(x1 rows)**

### Sheet: Parameters
- **Column 2** (1 edits):
  - 'header' -> 'path' **(x1 rows)**
- **Column 7** (3 edits):
  - '' -> 'Yes' **(x2 rows)**
  - 'M' -> 'Yes' **(x1 rows)**

### Sheet: Paths
- **Column 1** (1 edits):
  - '/v1/transactions/assessments' -> '/vop/v1/payee-verifications' **(x1 rows)**
- **Column 2** (1 edits):
  - 'Transacyion Assessments' -> 'Vop Payee-verifications' **(x1 rows)**
- **Column 4** (2 edits):
  - 'Performs a simultaneous Account Assessment and Verification of Payee request for an account, identified by an IBAN. **(x1 rows)**
  - 'This operation creates a pre-validation risk assessment for a **(x1 rows)**
- **Column 6** (1 edits):
  - 'Create Transaction Assessment' -> 'Perform Verification Of Payee (VOP)' **(x1 rows)**
- **Column 7** (1 edits):
  - 'create-transaction-assessment' -> 'postVerificationOfPayeeRequests' **(x1 rows)**
- **Column 8** (1 edits):
  - 'x-sandbox-rule-type: SCRIPT_JS **(x1 rows)**
- **Column Unknown** (1 edits):
  - ADDED Row Key='v1_transactions_assessments.251111' **(x1 rows)**

### Sheet: Responses
- **Column 1** (2046 edits):
  - 'x-sandbox-request-name' -> 'value' **(x35 rows)**
  - 'x-sandbox-request-headers' -> 'value' **(x35 rows)**
  - 'senderBic' -> 'value' **(x35 rows)**
  - 'pri' -> 'value' **(x35 rows)**
  - 'value' -> 'x-sandbox-request-name' **(x35 rows)**
  - 'value' -> 'x-sandbox-request-headers' **(x35 rows)**
  - 'value' -> 'senderBic' **(x35 rows)**
  - 'value' -> 'pri' **(x35 rows)**
  - 'x-sandbox-request-name' -> 'x-sandbox-request-headers' **(x25 rows)**
  - 'x-sandbox-request-name' -> 'senderBic' **(x25 rows)**
  - 'x-sandbox-request-name' -> 'pri' **(x25 rows)**
  - 'x-sandbox-request-headers' -> 'x-sandbox-request-name' **(x25 rows)**
  - 'x-sandbox-request-headers' -> 'senderBic' **(x25 rows)**
  - 'x-sandbox-request-headers' -> 'pri' **(x25 rows)**
  - 'senderBic' -> 'x-sandbox-request-name' **(x25 rows)**
  - 'senderBic' -> 'x-sandbox-request-headers' **(x25 rows)**
  - 'senderBic' -> 'pri' **(x25 rows)**
  - 'pri' -> 'x-sandbox-request-name' **(x25 rows)**
  - 'pri' -> 'x-sandbox-request-headers' **(x25 rows)**
  - 'pri' -> 'senderBic' **(x25 rows)**
  - 'value' -> 'errors' **(x21 rows)**
  - 'value' -> 'dateTime' **(x21 rows)**
  - 'value' -> 'code' **(x21 rows)**
  - 'value' -> 'description' **(x21 rows)**
  - 'errors' -> 'value' **(x21 rows)**
  - 'dateTime' -> 'value' **(x21 rows)**
  - 'code' -> 'value' **(x21 rows)**
  - 'description' -> 'value' **(x21 rows)**
  - 'text/plain' -> 'application/json' **(x15 rows)**
  - 'application/json' -> 'text/plain' **(x15 rows)**
  - 'x-sandbox-request-name' -> 'errors' **(x15 rows)**
  - 'x-sandbox-request-name' -> 'dateTime' **(x15 rows)**
  - 'x-sandbox-request-name' -> 'code' **(x15 rows)**
  - 'x-sandbox-request-name' -> 'description' **(x15 rows)**
  - 'x-sandbox-request-headers' -> 'errors' **(x15 rows)**
  - 'x-sandbox-request-headers' -> 'dateTime' **(x15 rows)**
  - 'x-sandbox-request-headers' -> 'code' **(x15 rows)**
  - 'x-sandbox-request-headers' -> 'description' **(x15 rows)**
  - 'senderBic' -> 'errors' **(x15 rows)**
  - 'senderBic' -> 'dateTime' **(x15 rows)**
  - 'senderBic' -> 'code' **(x15 rows)**
  - 'senderBic' -> 'description' **(x15 rows)**
  - 'pri' -> 'errors' **(x15 rows)**
  - 'pri' -> 'dateTime' **(x15 rows)**
  - 'pri' -> 'code' **(x15 rows)**
  - 'pri' -> 'description' **(x15 rows)**
  - 'errors' -> 'x-sandbox-request-name' **(x15 rows)**
  - 'errors' -> 'x-sandbox-request-headers' **(x15 rows)**
  - 'errors' -> 'senderBic' **(x15 rows)**
  - 'errors' -> 'pri' **(x15 rows)**
  - 'dateTime' -> 'x-sandbox-request-name' **(x15 rows)**
  - 'dateTime' -> 'x-sandbox-request-headers' **(x15 rows)**
  - 'dateTime' -> 'senderBic' **(x15 rows)**
  - 'dateTime' -> 'pri' **(x15 rows)**
  - 'code' -> 'x-sandbox-request-name' **(x15 rows)**
  - 'code' -> 'x-sandbox-request-headers' **(x15 rows)**
  - 'code' -> 'senderBic' **(x15 rows)**
  - 'code' -> 'pri' **(x15 rows)**
  - 'description' -> 'x-sandbox-request-name' **(x15 rows)**
  - 'description' -> 'x-sandbox-request-headers' **(x15 rows)**
  - 'description' -> 'senderBic' **(x15 rows)**
  - 'description' -> 'pri' **(x15 rows)**
  - 'errors' -> 'dateTime' **(x9 rows)**
  - 'errors' -> 'code' **(x9 rows)**
  - 'errors' -> 'description' **(x9 rows)**
  - 'dateTime' -> 'errors' **(x9 rows)**
  - 'dateTime' -> 'code' **(x9 rows)**
  - 'dateTime' -> 'description' **(x9 rows)**
  - 'code' -> 'errors' **(x9 rows)**
  - 'code' -> 'dateTime' **(x9 rows)**
  - 'code' -> 'description' **(x9 rows)**
  - 'description' -> 'errors' **(x9 rows)**
  - 'description' -> 'dateTime' **(x9 rows)**
  - 'description' -> 'code' **(x9 rows)**
  - 'Unauthorized' -> 'value' **(x7 rows)**
  - 'Forbidden' -> 'value' **(x7 rows)**
  - 'value' -> 'Unauthorized' **(x7 rows)**
  - 'value' -> 'Forbidden' **(x7 rows)**
  - 'value' -> 'Forbidden (application managed)' **(x7 rows)**
  - 'value' -> 'Not Found' **(x7 rows)**
  - 'value' -> 'Conflict' **(x7 rows)**
  - 'value' -> 'Too many requests' **(x7 rows)**
  - 'value' -> 'Generic Error' **(x7 rows)**
  - 'value' -> 'Generic Error (application managed)' **(x7 rows)**
  - 'Forbidden (application managed)' -> 'value' **(x7 rows)**
  - 'Not Found' -> 'value' **(x7 rows)**
  - 'Conflict' -> 'value' **(x7 rows)**
  - 'Too many requests' -> 'value' **(x7 rows)**
  - 'Generic Error' -> 'value' **(x7 rows)**
  - 'Generic Error (application managed)' -> 'value' **(x7 rows)**
  - 'Unauthorized' -> 'x-sandbox-request-name' **(x5 rows)**
  - 'Unauthorized' -> 'x-sandbox-request-headers' **(x5 rows)**
  - 'Unauthorized' -> 'senderBic' **(x5 rows)**
  - 'Unauthorized' -> 'pri' **(x5 rows)**
  - 'Forbidden' -> 'x-sandbox-request-name' **(x5 rows)**
  - 'Forbidden' -> 'x-sandbox-request-headers' **(x5 rows)**
  - 'Forbidden' -> 'senderBic' **(x5 rows)**
  - 'Forbidden' -> 'pri' **(x5 rows)**
  - 'x-sandbox-request-name' -> 'Unauthorized' **(x5 rows)**
  - 'x-sandbox-request-name' -> 'Forbidden' **(x5 rows)**
  - 'x-sandbox-request-name' -> 'Forbidden (application managed)' **(x5 rows)**
  - 'x-sandbox-request-name' -> 'Not Found' **(x5 rows)**
  - 'x-sandbox-request-name' -> 'Conflict' **(x5 rows)**
  - 'x-sandbox-request-name' -> 'Too many requests' **(x5 rows)**
  - 'x-sandbox-request-name' -> 'Generic Error' **(x5 rows)**
  - 'x-sandbox-request-name' -> 'Generic Error (application managed)' **(x5 rows)**
  - 'x-sandbox-request-headers' -> 'Unauthorized' **(x5 rows)**
  - 'x-sandbox-request-headers' -> 'Forbidden' **(x5 rows)**
  - 'x-sandbox-request-headers' -> 'Forbidden (application managed)' **(x5 rows)**
  - 'x-sandbox-request-headers' -> 'Not Found' **(x5 rows)**
  - 'x-sandbox-request-headers' -> 'Conflict' **(x5 rows)**
  - 'x-sandbox-request-headers' -> 'Too many requests' **(x5 rows)**
  - 'x-sandbox-request-headers' -> 'Generic Error' **(x5 rows)**
  - 'x-sandbox-request-headers' -> 'Generic Error (application managed)' **(x5 rows)**
  - 'senderBic' -> 'Unauthorized' **(x5 rows)**
  - 'senderBic' -> 'Forbidden' **(x5 rows)**
  - 'senderBic' -> 'Forbidden (application managed)' **(x5 rows)**
  - 'senderBic' -> 'Not Found' **(x5 rows)**
  - 'senderBic' -> 'Conflict' **(x5 rows)**
  - 'senderBic' -> 'Too many requests' **(x5 rows)**
  - 'senderBic' -> 'Generic Error' **(x5 rows)**
  - 'senderBic' -> 'Generic Error (application managed)' **(x5 rows)**
  - 'pri' -> 'Unauthorized' **(x5 rows)**
  - 'pri' -> 'Forbidden' **(x5 rows)**
  - 'pri' -> 'Forbidden (application managed)' **(x5 rows)**
  - 'pri' -> 'Not Found' **(x5 rows)**
  - 'pri' -> 'Conflict' **(x5 rows)**
  - 'pri' -> 'Too many requests' **(x5 rows)**
  - 'pri' -> 'Generic Error' **(x5 rows)**
  - 'pri' -> 'Generic Error (application managed)' **(x5 rows)**
  - 'Forbidden (application managed)' -> 'x-sandbox-request-name' **(x5 rows)**
  - 'Forbidden (application managed)' -> 'x-sandbox-request-headers' **(x5 rows)**
  - 'Forbidden (application managed)' -> 'senderBic' **(x5 rows)**
  - 'Forbidden (application managed)' -> 'pri' **(x5 rows)**
  - 'Not Found' -> 'x-sandbox-request-name' **(x5 rows)**
  - 'Not Found' -> 'x-sandbox-request-headers' **(x5 rows)**
  - 'Not Found' -> 'senderBic' **(x5 rows)**
  - 'Not Found' -> 'pri' **(x5 rows)**
  - 'Conflict' -> 'x-sandbox-request-name' **(x5 rows)**
  - 'Conflict' -> 'x-sandbox-request-headers' **(x5 rows)**
  - 'Conflict' -> 'senderBic' **(x5 rows)**
  - 'Conflict' -> 'pri' **(x5 rows)**
  - 'Too many requests' -> 'x-sandbox-request-name' **(x5 rows)**
  - 'Too many requests' -> 'x-sandbox-request-headers' **(x5 rows)**
  - 'Too many requests' -> 'senderBic' **(x5 rows)**
  - 'Too many requests' -> 'pri' **(x5 rows)**
  - 'Generic Error' -> 'x-sandbox-request-name' **(x5 rows)**
  - 'Generic Error' -> 'x-sandbox-request-headers' **(x5 rows)**
  - 'Generic Error' -> 'senderBic' **(x5 rows)**
  - 'Generic Error' -> 'pri' **(x5 rows)**
  - 'Generic Error (application managed)' -> 'x-sandbox-request-name' **(x5 rows)**
  - 'Generic Error (application managed)' -> 'x-sandbox-request-headers' **(x5 rows)**
  - 'Generic Error (application managed)' -> 'senderBic' **(x5 rows)**
  - 'Generic Error (application managed)' -> 'pri' **(x5 rows)**
  - 'Unauthorized' -> 'errors' **(x3 rows)**
  - 'Unauthorized' -> 'dateTime' **(x3 rows)**
  - 'Unauthorized' -> 'code' **(x3 rows)**
  - 'Unauthorized' -> 'description' **(x3 rows)**
  - 'Forbidden' -> 'errors' **(x3 rows)**
  - 'Forbidden' -> 'dateTime' **(x3 rows)**
  - 'Forbidden' -> 'code' **(x3 rows)**
  - 'Forbidden' -> 'description' **(x3 rows)**
  - 'Forbidden (application managed)' -> 'errors' **(x3 rows)**
  - 'Forbidden (application managed)' -> 'dateTime' **(x3 rows)**
  - 'Forbidden (application managed)' -> 'code' **(x3 rows)**
  - 'Forbidden (application managed)' -> 'description' **(x3 rows)**
  - 'errors' -> 'Unauthorized' **(x3 rows)**
  - 'errors' -> 'Forbidden' **(x3 rows)**
  - 'errors' -> 'Forbidden (application managed)' **(x3 rows)**
  - 'errors' -> 'Not Found' **(x3 rows)**
  - 'errors' -> 'Conflict' **(x3 rows)**
  - 'errors' -> 'Too many requests' **(x3 rows)**
  - 'errors' -> 'Generic Error' **(x3 rows)**
  - 'errors' -> 'Generic Error (application managed)' **(x3 rows)**
  - 'dateTime' -> 'Unauthorized' **(x3 rows)**
  - 'dateTime' -> 'Forbidden' **(x3 rows)**
  - 'dateTime' -> 'Forbidden (application managed)' **(x3 rows)**
  - 'dateTime' -> 'Not Found' **(x3 rows)**
  - 'dateTime' -> 'Conflict' **(x3 rows)**
  - 'dateTime' -> 'Too many requests' **(x3 rows)**
  - 'dateTime' -> 'Generic Error' **(x3 rows)**
  - 'dateTime' -> 'Generic Error (application managed)' **(x3 rows)**
  - 'code' -> 'Unauthorized' **(x3 rows)**
  - 'code' -> 'Forbidden' **(x3 rows)**
  - 'code' -> 'Forbidden (application managed)' **(x3 rows)**
  - 'code' -> 'Not Found' **(x3 rows)**
  - 'code' -> 'Conflict' **(x3 rows)**
  - 'code' -> 'Too many requests' **(x3 rows)**
  - 'code' -> 'Generic Error' **(x3 rows)**
  - 'code' -> 'Generic Error (application managed)' **(x3 rows)**
  - 'description' -> 'Unauthorized' **(x3 rows)**
  - 'description' -> 'Forbidden' **(x3 rows)**
  - 'description' -> 'Forbidden (application managed)' **(x3 rows)**
  - 'description' -> 'Not Found' **(x3 rows)**
  - 'description' -> 'Conflict' **(x3 rows)**
  - 'description' -> 'Too many requests' **(x3 rows)**
  - 'description' -> 'Generic Error' **(x3 rows)**
  - 'description' -> 'Generic Error (application managed)' **(x3 rows)**
  - 'Not Found' -> 'errors' **(x3 rows)**
  - 'Not Found' -> 'dateTime' **(x3 rows)**
  - 'Not Found' -> 'code' **(x3 rows)**
  - 'Not Found' -> 'description' **(x3 rows)**
  - 'Conflict' -> 'errors' **(x3 rows)**
  - 'Conflict' -> 'dateTime' **(x3 rows)**
  - 'Conflict' -> 'code' **(x3 rows)**
  - 'Conflict' -> 'description' **(x3 rows)**
  - 'Too many requests' -> 'errors' **(x3 rows)**
  - 'Too many requests' -> 'dateTime' **(x3 rows)**
  - 'Too many requests' -> 'code' **(x3 rows)**
  - 'Too many requests' -> 'description' **(x3 rows)**
  - 'Generic Error' -> 'errors' **(x3 rows)**
  - 'Generic Error' -> 'dateTime' **(x3 rows)**
  - 'Generic Error' -> 'code' **(x3 rows)**
  - 'Generic Error' -> 'description' **(x3 rows)**
  - 'Generic Error (application managed)' -> 'errors' **(x3 rows)**
  - 'Generic Error (application managed)' -> 'dateTime' **(x3 rows)**
  - 'Generic Error (application managed)' -> 'code' **(x3 rows)**
  - 'Generic Error (application managed)' -> 'description' **(x3 rows)**
  - 'Unauthorized' -> 'Forbidden' **(x1 rows)**
  - 'Unauthorized' -> 'Forbidden (application managed)' **(x1 rows)**
  - 'Unauthorized' -> 'Not Found' **(x1 rows)**
  - 'Unauthorized' -> 'Conflict' **(x1 rows)**
  - 'Unauthorized' -> 'Too many requests' **(x1 rows)**
  - 'Unauthorized' -> 'Generic Error' **(x1 rows)**
  - 'Unauthorized' -> 'Generic Error (application managed)' **(x1 rows)**
  - 'Forbidden' -> 'Unauthorized' **(x1 rows)**
  - 'Forbidden' -> 'Forbidden (application managed)' **(x1 rows)**
  - 'Forbidden' -> 'Not Found' **(x1 rows)**
  - 'Forbidden' -> 'Conflict' **(x1 rows)**
  - 'Forbidden' -> 'Too many requests' **(x1 rows)**
  - 'Forbidden' -> 'Generic Error' **(x1 rows)**
  - 'Forbidden' -> 'Generic Error (application managed)' **(x1 rows)**
  - 'Forbidden (application managed)' -> 'Unauthorized' **(x1 rows)**
  - 'Forbidden (application managed)' -> 'Forbidden' **(x1 rows)**
  - 'Forbidden (application managed)' -> 'Not Found' **(x1 rows)**
  - 'Forbidden (application managed)' -> 'Conflict' **(x1 rows)**
  - 'Forbidden (application managed)' -> 'Too many requests' **(x1 rows)**
  - 'Forbidden (application managed)' -> 'Generic Error' **(x1 rows)**
  - 'Forbidden (application managed)' -> 'Generic Error (application managed)' **(x1 rows)**
  - 'Not Found' -> 'Unauthorized' **(x1 rows)**
  - 'Not Found' -> 'Forbidden' **(x1 rows)**
  - 'Not Found' -> 'Forbidden (application managed)' **(x1 rows)**
  - 'Not Found' -> 'Conflict' **(x1 rows)**
  - 'Not Found' -> 'Too many requests' **(x1 rows)**
  - 'Not Found' -> 'Generic Error' **(x1 rows)**
  - 'Not Found' -> 'Generic Error (application managed)' **(x1 rows)**
  - 'Conflict' -> 'Unauthorized' **(x1 rows)**
  - 'Conflict' -> 'Forbidden' **(x1 rows)**
  - 'Conflict' -> 'Forbidden (application managed)' **(x1 rows)**
  - 'Conflict' -> 'Not Found' **(x1 rows)**
  - 'Conflict' -> 'Too many requests' **(x1 rows)**
  - 'Conflict' -> 'Generic Error' **(x1 rows)**
  - 'Conflict' -> 'Generic Error (application managed)' **(x1 rows)**
  - 'Too many requests' -> 'Unauthorized' **(x1 rows)**
  - 'Too many requests' -> 'Forbidden' **(x1 rows)**
  - 'Too many requests' -> 'Forbidden (application managed)' **(x1 rows)**
  - 'Too many requests' -> 'Not Found' **(x1 rows)**
  - 'Too many requests' -> 'Conflict' **(x1 rows)**
  - 'Too many requests' -> 'Generic Error' **(x1 rows)**
  - 'Too many requests' -> 'Generic Error (application managed)' **(x1 rows)**
  - 'Generic Error' -> 'Unauthorized' **(x1 rows)**
  - 'Generic Error' -> 'Forbidden' **(x1 rows)**
  - 'Generic Error' -> 'Forbidden (application managed)' **(x1 rows)**
  - 'Generic Error' -> 'Not Found' **(x1 rows)**
  - 'Generic Error' -> 'Conflict' **(x1 rows)**
  - 'Generic Error' -> 'Too many requests' **(x1 rows)**
  - 'Generic Error' -> 'Generic Error (application managed)' **(x1 rows)**
  - 'Generic Error (application managed)' -> 'Unauthorized' **(x1 rows)**
  - 'Generic Error (application managed)' -> 'Forbidden' **(x1 rows)**
  - 'Generic Error (application managed)' -> 'Forbidden (application managed)' **(x1 rows)**
  - 'Generic Error (application managed)' -> 'Not Found' **(x1 rows)**
  - 'Generic Error (application managed)' -> 'Conflict' **(x1 rows)**
  - 'Generic Error (application managed)' -> 'Too many requests' **(x1 rows)**
  - 'Generic Error (application managed)' -> 'Generic Error' **(x1 rows)**
- **Column 2** (2020 edits):
  - 'x-sandbox-request-headers' -> 'errors' **(x90 rows)**
  - 'errors' -> 'x-sandbox-request-headers' **(x90 rows)**
  - 'text/plain' -> 'x-sandbox-request-headers' **(x50 rows)**
  - 'x-sandbox-request-headers' -> 'text/plain' **(x50 rows)**
  - 'text/plain' -> 'errors' **(x45 rows)**
  - 'errors' -> 'text/plain' **(x45 rows)**
  - 'Forbidden' -> 'x-sandbox-request-headers' **(x30 rows)**
  - 'x-sandbox-request-headers' -> 'Forbidden' **(x30 rows)**
  - 'x-sandbox-request-headers' -> 'application/json' **(x30 rows)**
  - 'x-sandbox-request-headers' -> 'Forbidden (application managed)' **(x30 rows)**
  - 'x-sandbox-request-headers' -> 'value' **(x30 rows)**
  - 'x-sandbox-request-headers' -> 'Conflict' **(x30 rows)**
  - 'x-sandbox-request-headers' -> 'Generic Error' **(x30 rows)**
  - 'x-sandbox-request-headers' -> 'Generic Error (application managed)' **(x30 rows)**
  - 'application/json' -> 'x-sandbox-request-headers' **(x30 rows)**
  - 'Forbidden (application managed)' -> 'x-sandbox-request-headers' **(x30 rows)**
  - 'value' -> 'x-sandbox-request-headers' **(x30 rows)**
  - 'Conflict' -> 'x-sandbox-request-headers' **(x30 rows)**
  - 'Generic Error' -> 'x-sandbox-request-headers' **(x30 rows)**
  - 'Generic Error (application managed)' -> 'x-sandbox-request-headers' **(x30 rows)**
  - 'Forbidden' -> 'errors' **(x27 rows)**
  - 'application/json' -> 'errors' **(x27 rows)**
  - 'Forbidden (application managed)' -> 'errors' **(x27 rows)**
  - 'value' -> 'errors' **(x27 rows)**
  - 'errors' -> 'Forbidden' **(x27 rows)**
  - 'errors' -> 'application/json' **(x27 rows)**
  - 'errors' -> 'Forbidden (application managed)' **(x27 rows)**
  - 'errors' -> 'value' **(x27 rows)**
  - 'errors' -> 'Conflict' **(x27 rows)**
  - 'errors' -> 'Generic Error' **(x27 rows)**
  - 'errors' -> 'Generic Error (application managed)' **(x27 rows)**
  - 'Conflict' -> 'errors' **(x27 rows)**
  - 'Generic Error' -> 'errors' **(x27 rows)**
  - 'Generic Error (application managed)' -> 'errors' **(x27 rows)**
  - 'text/plain' -> 'Forbidden' **(x15 rows)**
  - 'text/plain' -> 'application/json' **(x15 rows)**
  - 'text/plain' -> 'Forbidden (application managed)' **(x15 rows)**
  - 'text/plain' -> 'value' **(x15 rows)**
  - 'text/plain' -> 'Conflict' **(x15 rows)**
  - 'text/plain' -> 'Generic Error' **(x15 rows)**
  - 'text/plain' -> 'Generic Error (application managed)' **(x15 rows)**
  - 'Forbidden' -> 'text/plain' **(x15 rows)**
  - 'application/json' -> 'text/plain' **(x15 rows)**
  - 'Forbidden (application managed)' -> 'text/plain' **(x15 rows)**
  - 'value' -> 'text/plain' **(x15 rows)**
  - 'Conflict' -> 'text/plain' **(x15 rows)**
  - 'Generic Error' -> 'text/plain' **(x15 rows)**
  - 'Generic Error (application managed)' -> 'text/plain' **(x15 rows)**
  - 'x-sandbox-request-headers' -> 'Not Found' **(x10 rows)**
  - 'x-sandbox-request-headers' -> 'Too many requests' **(x10 rows)**
  - 'Not Found' -> 'x-sandbox-request-headers' **(x10 rows)**
  - 'Too many requests' -> 'x-sandbox-request-headers' **(x10 rows)**
  - 'Forbidden' -> 'application/json' **(x9 rows)**
  - 'Forbidden' -> 'Forbidden (application managed)' **(x9 rows)**
  - 'Forbidden' -> 'value' **(x9 rows)**
  - 'Forbidden' -> 'Conflict' **(x9 rows)**
  - 'Forbidden' -> 'Generic Error' **(x9 rows)**
  - 'Forbidden' -> 'Generic Error (application managed)' **(x9 rows)**
  - 'application/json' -> 'Forbidden' **(x9 rows)**
  - 'application/json' -> 'Forbidden (application managed)' **(x9 rows)**
  - 'application/json' -> 'value' **(x9 rows)**
  - 'application/json' -> 'Conflict' **(x9 rows)**
  - 'application/json' -> 'Generic Error' **(x9 rows)**
  - 'application/json' -> 'Generic Error (application managed)' **(x9 rows)**
  - 'Forbidden (application managed)' -> 'Forbidden' **(x9 rows)**
  - 'Forbidden (application managed)' -> 'application/json' **(x9 rows)**
  - 'Forbidden (application managed)' -> 'value' **(x9 rows)**
  - 'Forbidden (application managed)' -> 'Conflict' **(x9 rows)**
  - 'Forbidden (application managed)' -> 'Generic Error' **(x9 rows)**
  - 'Forbidden (application managed)' -> 'Generic Error (application managed)' **(x9 rows)**
  - 'value' -> 'Forbidden' **(x9 rows)**
  - 'value' -> 'application/json' **(x9 rows)**
  - 'value' -> 'Forbidden (application managed)' **(x9 rows)**
  - 'value' -> 'Conflict' **(x9 rows)**
  - 'value' -> 'Generic Error' **(x9 rows)**
  - 'value' -> 'Generic Error (application managed)' **(x9 rows)**
  - 'errors' -> 'Not Found' **(x9 rows)**
  - 'errors' -> 'Too many requests' **(x9 rows)**
  - 'Not Found' -> 'errors' **(x9 rows)**
  - 'Conflict' -> 'Forbidden' **(x9 rows)**
  - 'Conflict' -> 'application/json' **(x9 rows)**
  - 'Conflict' -> 'Forbidden (application managed)' **(x9 rows)**
  - 'Conflict' -> 'value' **(x9 rows)**
  - 'Conflict' -> 'Generic Error' **(x9 rows)**
  - 'Conflict' -> 'Generic Error (application managed)' **(x9 rows)**
  - 'Too many requests' -> 'errors' **(x9 rows)**
  - 'Generic Error' -> 'Forbidden' **(x9 rows)**
  - 'Generic Error' -> 'application/json' **(x9 rows)**
  - 'Generic Error' -> 'Forbidden (application managed)' **(x9 rows)**
  - 'Generic Error' -> 'value' **(x9 rows)**
  - 'Generic Error' -> 'Conflict' **(x9 rows)**
  - 'Generic Error' -> 'Generic Error (application managed)' **(x9 rows)**
  - 'Generic Error (application managed)' -> 'Forbidden' **(x9 rows)**
  - 'Generic Error (application managed)' -> 'application/json' **(x9 rows)**
  - 'Generic Error (application managed)' -> 'Forbidden (application managed)' **(x9 rows)**
  - 'Generic Error (application managed)' -> 'value' **(x9 rows)**
  - 'Generic Error (application managed)' -> 'Conflict' **(x9 rows)**
  - 'Generic Error (application managed)' -> 'Generic Error' **(x9 rows)**
  - 'ErrorResponse_403' -> 'ErrorResponse_500' **(x5 rows)**
  - 'ErrorResponse_500' -> 'ErrorResponse_403' **(x5 rows)**
  - 'text/plain' -> 'Not Found' **(x5 rows)**
  - 'text/plain' -> 'Too many requests' **(x5 rows)**
  - 'Not Found' -> 'text/plain' **(x5 rows)**
  - 'Too many requests' -> 'text/plain' **(x5 rows)**
  - 'ErrorResponse_401' -> 'ErrorResponse_403' **(x3 rows)**
  - 'ErrorResponse_401' -> 'ErrorResponse_500' **(x3 rows)**
  - 'ErrorResponse_403' -> 'ErrorResponse_401' **(x3 rows)**
  - 'ErrorResponse_403' -> 'ErrorResponse_404' **(x3 rows)**
  - 'ErrorResponse_403' -> 'ErrorResponse_409' **(x3 rows)**
  - 'ErrorResponse_403' -> 'ErrorResponse_429' **(x3 rows)**
  - 'ErrorResponse_404' -> 'ErrorResponse_403' **(x3 rows)**
  - 'ErrorResponse_404' -> 'ErrorResponse_500' **(x3 rows)**
  - 'ErrorResponse_409' -> 'ErrorResponse_403' **(x3 rows)**
  - 'ErrorResponse_409' -> 'ErrorResponse_500' **(x3 rows)**
  - 'ErrorResponse_429' -> 'ErrorResponse_403' **(x3 rows)**
  - 'ErrorResponse_429' -> 'ErrorResponse_500' **(x3 rows)**
  - 'ErrorResponse_500' -> 'ErrorResponse_401' **(x3 rows)**
  - 'ErrorResponse_500' -> 'ErrorResponse_404' **(x3 rows)**
  - 'ErrorResponse_500' -> 'ErrorResponse_409' **(x3 rows)**
  - 'ErrorResponse_500' -> 'ErrorResponse_429' **(x3 rows)**
  - 'Forbidden' -> 'Not Found' **(x3 rows)**
  - 'Forbidden' -> 'Too many requests' **(x3 rows)**
  - 'application/json' -> 'Not Found' **(x3 rows)**
  - 'application/json' -> 'Too many requests' **(x3 rows)**
  - 'Forbidden (application managed)' -> 'Not Found' **(x3 rows)**
  - 'Forbidden (application managed)' -> 'Too many requests' **(x3 rows)**
  - 'value' -> 'Not Found' **(x3 rows)**
  - 'value' -> 'Too many requests' **(x3 rows)**
  - 'Not Found' -> 'Forbidden' **(x3 rows)**
  - 'Not Found' -> 'application/json' **(x3 rows)**
  - 'Not Found' -> 'Forbidden (application managed)' **(x3 rows)**
  - 'Not Found' -> 'value' **(x3 rows)**
  - 'Not Found' -> 'Conflict' **(x3 rows)**
  - 'Not Found' -> 'Generic Error' **(x3 rows)**
  - 'Not Found' -> 'Generic Error (application managed)' **(x3 rows)**
  - 'Conflict' -> 'Not Found' **(x3 rows)**
  - 'Conflict' -> 'Too many requests' **(x3 rows)**
  - 'Too many requests' -> 'Forbidden' **(x3 rows)**
  - 'Too many requests' -> 'application/json' **(x3 rows)**
  - 'Too many requests' -> 'Forbidden (application managed)' **(x3 rows)**
  - 'Too many requests' -> 'value' **(x3 rows)**
  - 'Too many requests' -> 'Conflict' **(x3 rows)**
  - 'Too many requests' -> 'Generic Error' **(x3 rows)**
  - 'Too many requests' -> 'Generic Error (application managed)' **(x3 rows)**
  - 'Generic Error' -> 'Not Found' **(x3 rows)**
  - 'Generic Error' -> 'Too many requests' **(x3 rows)**
  - 'Generic Error (application managed)' -> 'Not Found' **(x3 rows)**
  - 'Generic Error (application managed)' -> 'Too many requests' **(x3 rows)**
  - 'ErrorResponse_401' -> 'ErrorResponse_404' **(x2 rows)**
  - 'ErrorResponse_401' -> 'ErrorResponse_409' **(x2 rows)**
  - 'ErrorResponse_401' -> 'ErrorResponse_429' **(x2 rows)**
  - 'ErrorResponse_404' -> 'ErrorResponse_401' **(x2 rows)**
  - 'ErrorResponse_404' -> 'ErrorResponse_409' **(x2 rows)**
  - 'ErrorResponse_404' -> 'ErrorResponse_429' **(x2 rows)**
  - 'ErrorResponse_409' -> 'ErrorResponse_401' **(x2 rows)**
  - 'ErrorResponse_409' -> 'ErrorResponse_404' **(x2 rows)**
  - 'ErrorResponse_409' -> 'ErrorResponse_429' **(x2 rows)**
  - 'ErrorResponse_429' -> 'ErrorResponse_401' **(x2 rows)**
  - 'ErrorResponse_429' -> 'ErrorResponse_404' **(x2 rows)**
  - 'ErrorResponse_429' -> 'ErrorResponse_409' **(x2 rows)**
  - 'Not Found' -> 'Too many requests' **(x1 rows)**
  - 'Too many requests' -> 'Not Found' **(x1 rows)**
- **Column 3** (30 edits):
  - 'Error message' -> '' **(x15 rows)**
  - '' -> 'Error message' **(x15 rows)**
- **Column 4** (1190 edits):
  - '' -> 'string' **(x448 rows)**
  - 'string' -> '' **(x448 rows)**
  - 'string' -> 'array' **(x84 rows)**
  - 'array' -> 'string' **(x84 rows)**
  - '' -> 'array' **(x48 rows)**
  - 'array' -> '' **(x48 rows)**
  - 'string' -> 'schema' **(x15 rows)**
  - 'schema' -> 'string' **(x15 rows)**
- **Column 6** (30 edits):
  - '' -> 'ErrorResponse' **(x15 rows)**
  - 'ErrorResponse' -> '' **(x15 rows)**
- **Column 14** (1754 edits):
  - '' -> 'OK' **(x95 rows)**
  - '' -> 'FPADITMM' **(x95 rows)**
  - '' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x95 rows)**
  - 'OK' -> '' **(x95 rows)**
  - 'FPADITMM' -> '' **(x95 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> '' **(x95 rows)**
  - '' -> '2023-07-20T14:15:22Z' **(x57 rows)**
  - '2023-07-20T14:15:22Z' -> '' **(x57 rows)**
  - 'OK' -> 'FPADITMM' **(x25 rows)**
  - 'OK' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x25 rows)**
  - 'FPADITMM' -> 'OK' **(x25 rows)**
  - 'FPADITMM' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x25 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'OK' **(x25 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'FPADITMM' **(x25 rows)**
  - '' -> 'Forbidden' **(x19 rows)**
  - '' -> 'E403' **(x19 rows)**
  - '' -> 'The provided sender BIC is not authorized to perform this action.' **(x19 rows)**
  - '' -> 'Not Found' **(x19 rows)**
  - '' -> 'E409' **(x19 rows)**
  - '' -> 'The same PRI has already been sent.' **(x19 rows)**
  - '' -> 'Too many requests' **(x19 rows)**
  - '' -> 'Internal Server Error' **(x19 rows)**
  - '' -> 'E500' **(x19 rows)**
  - '' -> 'Application error.' **(x19 rows)**
  - 'Forbidden' -> '' **(x19 rows)**
  - 'E403' -> '' **(x19 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> '' **(x19 rows)**
  - 'Not Found' -> '' **(x19 rows)**
  - 'E409' -> '' **(x19 rows)**
  - 'The same PRI has already been sent.' -> '' **(x19 rows)**
  - 'Too many requests' -> '' **(x19 rows)**
  - 'Internal Server Error' -> '' **(x19 rows)**
  - 'E500' -> '' **(x19 rows)**
  - 'Application error.' -> '' **(x19 rows)**
  - 'OK' -> '2023-07-20T14:15:22Z' **(x15 rows)**
  - 'FPADITMM' -> '2023-07-20T14:15:22Z' **(x15 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> '2023-07-20T14:15:22Z' **(x15 rows)**
  - '2023-07-20T14:15:22Z' -> 'OK' **(x15 rows)**
  - '2023-07-20T14:15:22Z' -> 'FPADITMM' **(x15 rows)**
  - '2023-07-20T14:15:22Z' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x15 rows)**
  - 'OK' -> 'Forbidden' **(x5 rows)**
  - 'OK' -> 'E403' **(x5 rows)**
  - 'OK' -> 'The provided sender BIC is not authorized to perform this action.' **(x5 rows)**
  - 'OK' -> 'Not Found' **(x5 rows)**
  - 'OK' -> 'E409' **(x5 rows)**
  - 'OK' -> 'The same PRI has already been sent.' **(x5 rows)**
  - 'OK' -> 'Too many requests' **(x5 rows)**
  - 'OK' -> 'Internal Server Error' **(x5 rows)**
  - 'OK' -> 'E500' **(x5 rows)**
  - 'OK' -> 'Application error.' **(x5 rows)**
  - 'FPADITMM' -> 'Forbidden' **(x5 rows)**
  - 'FPADITMM' -> 'E403' **(x5 rows)**
  - 'FPADITMM' -> 'The provided sender BIC is not authorized to perform this action.' **(x5 rows)**
  - 'FPADITMM' -> 'Not Found' **(x5 rows)**
  - 'FPADITMM' -> 'E409' **(x5 rows)**
  - 'FPADITMM' -> 'The same PRI has already been sent.' **(x5 rows)**
  - 'FPADITMM' -> 'Too many requests' **(x5 rows)**
  - 'FPADITMM' -> 'Internal Server Error' **(x5 rows)**
  - 'FPADITMM' -> 'E500' **(x5 rows)**
  - 'FPADITMM' -> 'Application error.' **(x5 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'Forbidden' **(x5 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'E403' **(x5 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'The provided sender BIC is not authorized to perform this action.' **(x5 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'Not Found' **(x5 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'E409' **(x5 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'The same PRI has already been sent.' **(x5 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'Too many requests' **(x5 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'Internal Server Error' **(x5 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'E500' **(x5 rows)**
  - 'a206e009-ef37-4040-924d-db758b29b401' -> 'Application error.' **(x5 rows)**
  - 'Forbidden' -> 'OK' **(x5 rows)**
  - 'Forbidden' -> 'FPADITMM' **(x5 rows)**
  - 'Forbidden' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x5 rows)**
  - 'E403' -> 'OK' **(x5 rows)**
  - 'E403' -> 'FPADITMM' **(x5 rows)**
  - 'E403' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x5 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'OK' **(x5 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'FPADITMM' **(x5 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x5 rows)**
  - 'Not Found' -> 'OK' **(x5 rows)**
  - 'Not Found' -> 'FPADITMM' **(x5 rows)**
  - 'Not Found' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x5 rows)**
  - 'E409' -> 'OK' **(x5 rows)**
  - 'E409' -> 'FPADITMM' **(x5 rows)**
  - 'E409' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x5 rows)**
  - 'The same PRI has already been sent.' -> 'OK' **(x5 rows)**
  - 'The same PRI has already been sent.' -> 'FPADITMM' **(x5 rows)**
  - 'The same PRI has already been sent.' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x5 rows)**
  - 'Too many requests' -> 'OK' **(x5 rows)**
  - 'Too many requests' -> 'FPADITMM' **(x5 rows)**
  - 'Too many requests' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x5 rows)**
  - 'Internal Server Error' -> 'OK' **(x5 rows)**
  - 'Internal Server Error' -> 'FPADITMM' **(x5 rows)**
  - 'Internal Server Error' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x5 rows)**
  - 'E500' -> 'OK' **(x5 rows)**
  - 'E500' -> 'FPADITMM' **(x5 rows)**
  - 'E500' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x5 rows)**
  - 'Application error.' -> 'OK' **(x5 rows)**
  - 'Application error.' -> 'FPADITMM' **(x5 rows)**
  - 'Application error.' -> 'a206e009-ef37-4040-924d-db758b29b401' **(x5 rows)**
  - 'Forbidden' -> '2023-07-20T14:15:22Z' **(x3 rows)**
  - '2023-07-20T14:15:22Z' -> 'Forbidden' **(x3 rows)**
  - '2023-07-20T14:15:22Z' -> 'E403' **(x3 rows)**
  - '2023-07-20T14:15:22Z' -> 'The provided sender BIC is not authorized to perform this action.' **(x3 rows)**
  - '2023-07-20T14:15:22Z' -> 'Not Found' **(x3 rows)**
  - '2023-07-20T14:15:22Z' -> 'E409' **(x3 rows)**
  - '2023-07-20T14:15:22Z' -> 'The same PRI has already been sent.' **(x3 rows)**
  - '2023-07-20T14:15:22Z' -> 'Too many requests' **(x3 rows)**
  - '2023-07-20T14:15:22Z' -> 'Internal Server Error' **(x3 rows)**
  - '2023-07-20T14:15:22Z' -> 'E500' **(x3 rows)**
  - '2023-07-20T14:15:22Z' -> 'Application error.' **(x3 rows)**
  - 'E403' -> '2023-07-20T14:15:22Z' **(x3 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> '2023-07-20T14:15:22Z' **(x3 rows)**
  - 'Not Found' -> '2023-07-20T14:15:22Z' **(x3 rows)**
  - 'E409' -> '2023-07-20T14:15:22Z' **(x3 rows)**
  - 'The same PRI has already been sent.' -> '2023-07-20T14:15:22Z' **(x3 rows)**
  - 'Too many requests' -> '2023-07-20T14:15:22Z' **(x3 rows)**
  - 'Internal Server Error' -> '2023-07-20T14:15:22Z' **(x3 rows)**
  - 'E500' -> '2023-07-20T14:15:22Z' **(x3 rows)**
  - 'Application error.' -> '2023-07-20T14:15:22Z' **(x3 rows)**
  - 'Forbidden' -> 'E403' **(x1 rows)**
  - 'Forbidden' -> 'The provided sender BIC is not authorized to perform this action.' **(x1 rows)**
  - 'Forbidden' -> 'Not Found' **(x1 rows)**
  - 'Forbidden' -> 'E409' **(x1 rows)**
  - 'Forbidden' -> 'The same PRI has already been sent.' **(x1 rows)**
  - 'Forbidden' -> 'Too many requests' **(x1 rows)**
  - 'Forbidden' -> 'Internal Server Error' **(x1 rows)**
  - 'Forbidden' -> 'E500' **(x1 rows)**
  - 'Forbidden' -> 'Application error.' **(x1 rows)**
  - 'E403' -> 'Forbidden' **(x1 rows)**
  - 'E403' -> 'The provided sender BIC is not authorized to perform this action.' **(x1 rows)**
  - 'E403' -> 'Not Found' **(x1 rows)**
  - 'E403' -> 'E409' **(x1 rows)**
  - 'E403' -> 'The same PRI has already been sent.' **(x1 rows)**
  - 'E403' -> 'Too many requests' **(x1 rows)**
  - 'E403' -> 'Internal Server Error' **(x1 rows)**
  - 'E403' -> 'E500' **(x1 rows)**
  - 'E403' -> 'Application error.' **(x1 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'Forbidden' **(x1 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'E403' **(x1 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'Not Found' **(x1 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'E409' **(x1 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'The same PRI has already been sent.' **(x1 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'Too many requests' **(x1 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'Internal Server Error' **(x1 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'E500' **(x1 rows)**
  - 'The provided sender BIC is not authorized to perform this action.' -> 'Application error.' **(x1 rows)**
  - 'Not Found' -> 'Forbidden' **(x1 rows)**
  - 'Not Found' -> 'E403' **(x1 rows)**
  - 'Not Found' -> 'The provided sender BIC is not authorized to perform this action.' **(x1 rows)**
  - 'Not Found' -> 'E409' **(x1 rows)**
  - 'Not Found' -> 'The same PRI has already been sent.' **(x1 rows)**
  - 'Not Found' -> 'Too many requests' **(x1 rows)**
  - 'Not Found' -> 'Internal Server Error' **(x1 rows)**
  - 'Not Found' -> 'E500' **(x1 rows)**
  - 'Not Found' -> 'Application error.' **(x1 rows)**
  - 'E409' -> 'Forbidden' **(x1 rows)**
  - 'E409' -> 'E403' **(x1 rows)**
  - 'E409' -> 'The provided sender BIC is not authorized to perform this action.' **(x1 rows)**
  - 'E409' -> 'Not Found' **(x1 rows)**
  - 'E409' -> 'The same PRI has already been sent.' **(x1 rows)**
  - 'E409' -> 'Too many requests' **(x1 rows)**
  - 'E409' -> 'Internal Server Error' **(x1 rows)**
  - 'E409' -> 'E500' **(x1 rows)**
  - 'E409' -> 'Application error.' **(x1 rows)**
  - 'The same PRI has already been sent.' -> 'Forbidden' **(x1 rows)**
  - 'The same PRI has already been sent.' -> 'E403' **(x1 rows)**
  - 'The same PRI has already been sent.' -> 'The provided sender BIC is not authorized to perform this action.' **(x1 rows)**
  - 'The same PRI has already been sent.' -> 'Not Found' **(x1 rows)**
  - 'The same PRI has already been sent.' -> 'E409' **(x1 rows)**
  - 'The same PRI has already been sent.' -> 'Too many requests' **(x1 rows)**
  - 'The same PRI has already been sent.' -> 'Internal Server Error' **(x1 rows)**
  - 'The same PRI has already been sent.' -> 'E500' **(x1 rows)**
  - 'The same PRI has already been sent.' -> 'Application error.' **(x1 rows)**
  - 'Too many requests' -> 'Forbidden' **(x1 rows)**
  - 'Too many requests' -> 'E403' **(x1 rows)**
  - 'Too many requests' -> 'The provided sender BIC is not authorized to perform this action.' **(x1 rows)**
  - 'Too many requests' -> 'Not Found' **(x1 rows)**
  - 'Too many requests' -> 'E409' **(x1 rows)**
  - 'Too many requests' -> 'The same PRI has already been sent.' **(x1 rows)**
  - 'Too many requests' -> 'Internal Server Error' **(x1 rows)**
  - 'Too many requests' -> 'E500' **(x1 rows)**
  - 'Too many requests' -> 'Application error.' **(x1 rows)**
  - 'Internal Server Error' -> 'Forbidden' **(x1 rows)**
  - 'Internal Server Error' -> 'E403' **(x1 rows)**
  - 'Internal Server Error' -> 'The provided sender BIC is not authorized to perform this action.' **(x1 rows)**
  - 'Internal Server Error' -> 'Not Found' **(x1 rows)**
  - 'Internal Server Error' -> 'E409' **(x1 rows)**
  - 'Internal Server Error' -> 'The same PRI has already been sent.' **(x1 rows)**
  - 'Internal Server Error' -> 'Too many requests' **(x1 rows)**
  - 'Internal Server Error' -> 'E500' **(x1 rows)**
  - 'Internal Server Error' -> 'Application error.' **(x1 rows)**
  - 'E500' -> 'Forbidden' **(x1 rows)**
  - 'E500' -> 'E403' **(x1 rows)**
  - 'E500' -> 'The provided sender BIC is not authorized to perform this action.' **(x1 rows)**
  - 'E500' -> 'Not Found' **(x1 rows)**
  - 'E500' -> 'E409' **(x1 rows)**
  - 'E500' -> 'The same PRI has already been sent.' **(x1 rows)**
  - 'E500' -> 'Too many requests' **(x1 rows)**
  - 'E500' -> 'Internal Server Error' **(x1 rows)**
  - 'E500' -> 'Application error.' **(x1 rows)**
  - 'Application error.' -> 'Forbidden' **(x1 rows)**
  - 'Application error.' -> 'E403' **(x1 rows)**
  - 'Application error.' -> 'The provided sender BIC is not authorized to perform this action.' **(x1 rows)**
  - 'Application error.' -> 'Not Found' **(x1 rows)**
  - 'Application error.' -> 'E409' **(x1 rows)**
  - 'Application error.' -> 'The same PRI has already been sent.' **(x1 rows)**
  - 'Application error.' -> 'Too many requests' **(x1 rows)**
  - 'Application error.' -> 'Internal Server Error' **(x1 rows)**
  - 'Application error.' -> 'E500' **(x1 rows)**

### Sheet: Schemas
- **Column 2** (31 edits):
  - 'BIC of the Agent managing the Creditor's Account present in the **(x2 rows)**
  - 'IBAN identifies the Creditor's Account present in the potential **(x2 rows)**
  - 'BIC of the Agent managing the Debtor's Account present in the **(x2 rows)**
  - '' -> 'Standard amount.' **(x1 rows)**
  - 'Structure of a transaction assessment request, with all data of a **(x1 rows)**
  - 'Business Identifier Code (BIC) in 8 or 11 characters format' -> 'Business Identifier Code (BIC) in 8 or 11 characters format.' **(x1 rows)**
  - 'Structure describing FPAD error response, with a mandatory array of  errors, each one with code, description and the timestamp of when it occurred.' -> 'Structure describing FPAD error response, with a mandatory array of **(x1 rows)**
  - 'Usage Rule: the use of either ‘schemeNameCode’ or ‘schemeNameProprietary’ is mandatory when the ‘identification code’ is used. **(x1 rows)**
  - 'Separation of the two kinds of identification into distinct structures ensures that the two sets of attributes are mutually exclusive. **(x1 rows)**
  - 'The RiskInfoArray is an array where each item represents an assessed **(x1 rows)**
  - 'Separation of the two kinds of responses in different structures allows constraints on code identification results and name inclusion. **(x1 rows)**
  - 'Category Purpose of the potential transaction that has to be **(x1 rows)**
  - 'BIC of the Agent managing the Creditor's Account present in the transaction.\r\nIf a 8 characters BIC is assigned as value, all transactions having a creditorBic starting with the same 8 characters will be considered.' -> 'BIC of the Agent managing the Creditor's Account present in the transaction._x000D_ **(x1 rows)**
  - 'Name associated with the Creditor's Account present in the **(x1 rows)**
  - 'Name associated with the Creditor's Account present in the transaction.\r\n All transactions starting with the value assigned will be considered.' -> 'Name associated with the Creditor's Account present in the transaction._x000D_ **(x1 rows)**
  - 'BIC of the Agent managing the Debtor's Account present in the transaction.\r\nIf a 8 characters BIC is assigned as value, all transactions having a debtorBic starting with the same 8 characters will be considered.' -> 'BIC of the Agent managing the Debtor's Account present in the transaction._x000D_ **(x1 rows)**
  - 'Name associated with the Debtor's Account present in the **(x1 rows)**
  - 'Name associated with the Debtor's Account present in the transaction.\r\nAll transactions starting with the value assigned will be considered.' -> 'Name associated with the Debtor's Account present in the transaction._x000D_ **(x1 rows)**
  - 'Maximum value admitted as General Risk Indicator (model **(x1 rows)**
  - 'Maximum reference date and time. It cannot exceed 3 days from *minReferenceDateTime*.\r\nReference Date Time must be intended as *settlementDate* for SCT and *acceptanceDateTime* for SCTInst.' -> 'Maximum reference date and time. It cannot exceed 3 days from *minReferenceDateTime*._x000D_ **(x1 rows)**
  - 'Minimum value admitted as General Risk Indicator (model **(x1 rows)**
  - 'Minimum reference date and time.\r\nReference Date Time must be intended as *settlementDate* for SCT and *acceptanceDateTime* for SCTInst.' -> 'Minimum reference date and time._x000D_ **(x1 rows)**
  - 'Unique identification of an organisation, as assigned by an institution, using an identification scheme. **(x1 rows)**
  - 'Reference date and time of the potential transaction that has to be assessed.\r\nIt must me intended as *settlementDate* for SCT and *acceptanceDateTime* for SCTInst services.' -> 'Reference date and time of the potential transaction that has to be assessed._x000D_ **(x1 rows)**
  - 'Reference date and time of the transaction.\r\nIt must be intended as *settlementDate* for SCT and *acceptanceDtateTime* for SCTInst transactions.' -> 'Reference date and time of the transaction._x000D_ **(x1 rows)**
  - 'This attribute refers to: **(x1 rows)**
  - 'Identifier of the transaction, unique for the Debtor''s Agent.' -> 'Identifier of the transaction, unique for the Debtor's Agent.' **(x1 rows)**
  - 'Additional information about AT-C001 sent by the Requester AT-C007, **(x1 rows)**
- **Column 3** (7 edits):
  - 'object' -> 'schema' **(x4 rows)**
  - '' -> 'string' **(x2 rows)**
  - 'String' -> 'string' **(x1 rows)**
- **Column 4** (6 edits):
  - 'schema' -> 'VopBulkIdentification' **(x1 rows)**
  - 'schema' -> 'HateoasBlock' **(x1 rows)**
  - 'schema' -> 'ShortMessage' **(x1 rows)**
  - 'schema' -> 'GenericOrganisationIdentification' **(x1 rows)**
  - 'schema' -> 'Ria' **(x1 rows)**
  - 'schema' -> 'Max140Text' **(x1 rows)**
- **Column 5** (11 edits):
  - '' -> 'Max35Text' **(x2 rows)**
  - 'iban' -> 'Iban' **(x1 rows)**
  - 'VopBulkIdentification' -> '' **(x1 rows)**
  - '' -> 'Max256Text' **(x1 rows)**
  - 'HateoasBlock' -> '' **(x1 rows)**
  - 'ShortMessage' -> '' **(x1 rows)**
  - 'GenericOrganisationIdentification' -> '' **(x1 rows)**
  - 'Ria' -> '' **(x1 rows)**
  - '' -> 'OrganisationIdentificationCode' **(x1 rows)**
  - 'Max140Text' -> '' **(x1 rows)**
- **Column 7** (5 edits):
  - 'M' -> 'Yes' **(x3 rows)**
  - '' -> 'No' **(x1 rows)**
  - 'M' -> 'No' **(x1 rows)**
- **Column 11** (1 edits):
  - '[A-Z0-9]{18}[0-9]{2}$' -> '^[A-Z0-9]{18}[0-9]{2}$' **(x1 rows)**
- **Column 12** (4 edits):
  - 'FORMAT_ERROR, CLIENT_INVALID, CLIENT_INCONSISTENT, TIMESTAMP_INVALID' -> 'FORMAT_ERROR,CLIENT_INVALID,CLIENT_INCONSISTENT,TIMESTAMP_INVALID' **(x1 rows)**
  - 'BANK, CBID, CHID, CINC, COID, CUST, DUNS, EMPL, GS1G, SREN, SRET, TXID, BDID, BOID' -> 'BANK,CBID,CHID,CINC,COID,CUST,DUNS,EMPL,GS1G,SREN,SRET,TXID,BDID,BOID' **(x1 rows)**
  - 'SCT, SCTInst' -> 'SCT,SCTInst' **(x1 rows)**
  - '' -> 'INFO,WARNING,ERROR' **(x1 rows)**
- **Column 13** (5 edits):
  - '{rel: next **(x1 rows)**
  - '{instructingAgentBic: FPADITMM **(x1 rows)**
  - '{messageType: WARNING **(x1 rows)**
  - '{serviceType: SCT **(x1 rows)**
  - Timestamp update (Standardized) **(x1 rows)**
- **Column Unknown** (14 edits):
  - ADDED Row Key='dateTime | errors' **(x1 rows)**
  - ADDED Row Key='identification | PartyType' **(x1 rows)**
  - ADDED Row Key='modelOutcome | RiskInfoArray' **(x1 rows)**
  - ADDED Row Key='name | PartyType' **(x1 rows)**
  - ADDED Row Key='transactionId | AssessmentTransactionData' **(x1 rows)**
  - REMOVED Row Key='InvestigationTransaction | AssessmentTransactionData' **(x1 rows)**
  - REMOVED Row Key='allOf | identification' **(x1 rows)**
  - REMOVED Row Key='allOf | issuer' **(x1 rows)**
  - REMOVED Row Key='allOf | schemeNameCode' **(x1 rows)**
  - REMOVED Row Key='allOf | schemeNameProprietary' **(x1 rows)**
  - REMOVED Row Key='dateTime | PartType+B23' **(x1 rows)**
  - REMOVED Row Key='identification | PartType' **(x1 rows)**
  - REMOVED Row Key='modelOutCome | RiskInfoArray' **(x1 rows)**
  - REMOVED Row Key='name | PartType' **(x1 rows)**

## account_assessment.251111.xlsm
### Sheet: 201
- **Column 2** (2 edits):
  - 'CREATED' -> 'Created' **(x1 rows)**
  - '' -> 'application/json' **(x1 rows)**

### Sheet: 400
- **Column 1** (30 edits):
  - 'Bad Request' -> 'value' **(x1 rows)**
  - 'Bad Request' -> 'errors' **(x1 rows)**
  - 'Bad Request' -> 'dateTime' **(x1 rows)**
  - 'Bad Request' -> 'code' **(x1 rows)**
  - 'Bad Request' -> 'description' **(x1 rows)**
  - 'value' -> 'Bad Request' **(x1 rows)**
  - 'value' -> 'errors' **(x1 rows)**
  - 'value' -> 'dateTime' **(x1 rows)**
  - 'value' -> 'code' **(x1 rows)**
  - 'value' -> 'description' **(x1 rows)**
  - 'errors' -> 'Bad Request' **(x1 rows)**
  - 'errors' -> 'value' **(x1 rows)**
  - 'errors' -> 'dateTime' **(x1 rows)**
  - 'errors' -> 'code' **(x1 rows)**
  - 'errors' -> 'description' **(x1 rows)**
  - 'dateTime' -> 'Bad Request' **(x1 rows)**
  - 'dateTime' -> 'value' **(x1 rows)**
  - 'dateTime' -> 'errors' **(x1 rows)**
  - 'dateTime' -> 'code' **(x1 rows)**
  - 'dateTime' -> 'description' **(x1 rows)**
  - 'code' -> 'Bad Request' **(x1 rows)**
  - 'code' -> 'value' **(x1 rows)**
  - 'code' -> 'errors' **(x1 rows)**
  - 'code' -> 'dateTime' **(x1 rows)**
  - 'code' -> 'description' **(x1 rows)**
  - 'description' -> 'Bad Request' **(x1 rows)**
  - 'description' -> 'value' **(x1 rows)**
  - 'description' -> 'errors' **(x1 rows)**
  - 'description' -> 'dateTime' **(x1 rows)**
  - 'description' -> 'code' **(x1 rows)**
- **Column 2** (24 edits):
  - 'application/json' -> 'errors[0]' **(x3 rows)**
  - 'Bad Request' -> 'errors[0]' **(x3 rows)**
  - 'value' -> 'errors[0]' **(x3 rows)**
  - 'errors[0]' -> 'application/json' **(x3 rows)**
  - 'errors[0]' -> 'Bad Request' **(x3 rows)**
  - 'errors[0]' -> 'value' **(x3 rows)**
  - 'application/json' -> 'Bad Request' **(x1 rows)**
  - 'application/json' -> 'value' **(x1 rows)**
  - 'Bad Request' -> 'application/json' **(x1 rows)**
  - 'Bad Request' -> 'value' **(x1 rows)**
  - 'value' -> 'application/json' **(x1 rows)**
  - 'value' -> 'Bad Request' **(x1 rows)**
- **Column 4** (22 edits):
  - '' -> 'string' **(x6 rows)**
  - 'string' -> '' **(x6 rows)**
  - 'array' -> 'string' **(x3 rows)**
  - 'string' -> 'array' **(x3 rows)**
  - '' -> 'array' **(x2 rows)**
  - 'array' -> '' **(x2 rows)**
- **Column 14** (24 edits):
  - '' -> '2019-08-24T14:15:22Z' **(x3 rows)**
  - '' -> 'E400' **(x3 rows)**
  - '' -> 'Field 'status' is required.' **(x3 rows)**
  - '2019-08-24T14:15:22Z' -> '' **(x3 rows)**
  - 'E400' -> '' **(x3 rows)**
  - 'Field 'status' is required.' -> '' **(x3 rows)**
  - '2019-08-24T14:15:22Z' -> 'E400' **(x1 rows)**
  - '2019-08-24T14:15:22Z' -> 'Field 'status' is required.' **(x1 rows)**
  - 'E400' -> '2019-08-24T14:15:22Z' **(x1 rows)**
  - 'E400' -> 'Field 'status' is required.' **(x1 rows)**
  - 'Field 'status' is required.' -> '2019-08-24T14:15:22Z' **(x1 rows)**
  - 'Field 'status' is required.' -> 'E400' **(x1 rows)**

### Sheet: Body Example
- **Column 1** (2 edits):
  - '{ **(x2 rows)**

## account_assessment_vop.251111.xlsm
### Sheet: 201
- **Column 1** (6 edits):
  - 'fri' -> 'pri' **(x1 rows)**
  - 'fri' -> 'X-Response-Timestamp' **(x1 rows)**
  - 'pri' -> 'fri' **(x1 rows)**
  - 'pri' -> 'X-Response-Timestamp' **(x1 rows)**
  - 'X-Response-Timestamp' -> 'fri' **(x1 rows)**
  - 'X-Response-Timestamp' -> 'pri' **(x1 rows)**
- **Column 3** (7 edits):
  - '' -> 'Created' **(x1 rows)**
  - '' -> 'Participant Request Identifier used also as Requesting PSP’s reference number of the VOP Request **(T054)**.' **(x1 rows)**
  - '' -> 'Time stamp of provided by the responding PSP **(T061)**.' **(x1 rows)**
  - 'Participant Request Identifier used also as Requesting PSP’s reference number of the VOP Request **(T054)**.' -> 'Created' **(x1 rows)**
  - 'Participant Request Identifier used also as Requesting PSP’s reference number of the VOP Request **(T054)**.' -> 'Time stamp of provided by the responding PSP **(T061)**.' **(x1 rows)**
  - 'Time stamp of provided by the responding PSP **(T061)**.' -> 'Created' **(x1 rows)**
  - 'Time stamp of provided by the responding PSP **(T061)**.' -> 'Participant Request Identifier used also as Requesting PSP’s reference number of the VOP Request **(T054)**.' **(x1 rows)**
- **Column 4** (4 edits):
  - 'header' -> 'string' **(x2 rows)**
  - 'string' -> 'header' **(x2 rows)**
- **Column 6** (6 edits):
  - 'FpadResponseIdentifier' -> 'pri' **(x1 rows)**
  - 'FpadResponseIdentifier' -> '' **(x1 rows)**
  - 'pri' -> 'FpadResponseIdentifier' **(x1 rows)**
  - 'pri' -> '' **(x1 rows)**
  - '' -> 'FpadResponseIdentifier' **(x1 rows)**
  - '' -> 'pri' **(x1 rows)**
- **Column 7** (4 edits):
  - '' -> 'date-format' **(x2 rows)**
  - 'date-format' -> '' **(x2 rows)**
- **Column 8** (4 edits):
  - '' -> 'M' **(x2 rows)**
  - 'M' -> '' **(x2 rows)**
- **Column 14** (4 edits):
  - '' -> '2024-08-12T15:19:22.678Z' **(x2 rows)**
  - '2024-08-12T15:19:22.678Z' -> '' **(x2 rows)**

### Sheet: 400
- **Column 1** (2 edits):
  - 'fri' -> 'X-Response-Timestamp' **(x1 rows)**
  - 'X-Response-Timestamp' -> 'fri' **(x1 rows)**
- **Column 4** (2 edits):
  - 'header' -> 'string' **(x1 rows)**
  - 'string' -> 'header' **(x1 rows)**
- **Column 6** (2 edits):
  - 'FpadResponseIdentifier' -> '' **(x1 rows)**
  - '' -> 'FpadResponseIdentifier' **(x1 rows)**
- **Column 7** (2 edits):
  - '' -> 'date-format' **(x1 rows)**
  - 'date-format' -> '' **(x1 rows)**
- **Column 8** (2 edits):
  - '' -> 'M' **(x1 rows)**
  - 'M' -> '' **(x1 rows)**
- **Column 14** (2 edits):
  - '' -> '2024-08-12T15:19:22.678Z' **(x1 rows)**
  - '2024-08-12T15:19:22.678Z' -> '' **(x1 rows)**

### Sheet: Body Example
- **Column 1** (2 edits):
  - '{ **(x2 rows)**

## account_assessment_vop_bulk.251111.xlsm
### Sheet: 201
- **Column 1** (2 edits):
  - 'fri' -> 'pri' **(x1 rows)**
  - 'pri' -> 'fri' **(x1 rows)**
- **Column 3** (3 edits):
  - '' -> 'Created' **(x1 rows)**
  - '' -> 'Participant Request Identifier used also as Requesting PSP’s reference number of the VOP Request **(T054)**.' **(x1 rows)**
  - 'Participant Request Identifier used also as Requesting PSP’s reference number of the VOP Request **(T054)**.' -> 'Created' **(x1 rows)**
- **Column 6** (2 edits):
  - 'FpadResponseIdentifier' -> 'pri' **(x1 rows)**
  - 'pri' -> 'FpadResponseIdentifier' **(x1 rows)**

### Sheet: 409
- **Column 1** (1 edits):
  - '' -> 'Conflict' **(x1 rows)**

## v1_eds_local-file.251111.xlsm
### Sheet: 400
- **Column 4** (1 edits):
  - 'schema' -> 'header' **(x1 rows)**

### Sheet: 401
- **Column 1** (1 edits):
  - 'application/json' -> 'Unauthorized' **(x1 rows)**

### Sheet: 403
- **Column 1** (1 edits):
  - 'application/json' -> 'Forbidden' **(x1 rows)**

### Sheet: 409
- **Column 1** (1 edits):
  - 'application/json' -> 'Conflict' **(x1 rows)**

### Sheet: 429
- **Column 1** (1 edits):
  - 'application/json' -> 'Too many requests' **(x1 rows)**

### Sheet: 500
- **Column 1** (1 edits):
  - 'application/json' -> 'Generic Error' **(x1 rows)**

## v1_risk-info_feedbacks.251111.xlsm
### Sheet: 201
- **Column 3** (1 edits):
  - '' -> 'Created' **(x1 rows)**
- **Column 4** (1 edits):
  - 'headers' -> 'header' **(x1 rows)**

### Sheet: 400
- **Column 4** (1 edits):
  - 'schema' -> 'header' **(x1 rows)**

### Sheet: 401
- **Column 1** (1 edits):
  - 'application/json' -> 'Unauthorized' **(x1 rows)**

### Sheet: 403
- **Column 1** (1 edits):
  - 'application/json' -> 'Forbidden' **(x1 rows)**

### Sheet: 409
- **Column 1** (1 edits):
  - 'application/json' -> 'Conflict' **(x1 rows)**

### Sheet: 429
- **Column 1** (1 edits):
  - 'application/json' -> 'Too many requests' **(x1 rows)**

### Sheet: 500
- **Column 1** (1 edits):
  - 'application/json' -> 'Generic Error' **(x1 rows)**

### Sheet: Body Example
- **Column 1** (2 edits):
  - '{ **(x2 rows)**

## v1_transactions_assessments.251111.xlsm
### Sheet: 201
- **Column 3** (1 edits):
  - '' -> 'Created' **(x1 rows)**

### Sheet: 400
- **Column 4** (1 edits):
  - 'schema' -> 'header' **(x1 rows)**

### Sheet: 401
- **Column 1** (1 edits):
  - 'application/json' -> 'Unauthorized' **(x1 rows)**

### Sheet: 403
- **Column 1** (1 edits):
  - 'application/json' -> 'Forbidden' **(x1 rows)**

### Sheet: 409
- **Column 1** (1 edits):
  - 'application/json' -> 'Conflict' **(x1 rows)**

### Sheet: 429
- **Column 1** (1 edits):
  - 'application/json' -> 'Too many requests' **(x1 rows)**

### Sheet: 500
- **Column 1** (1 edits):
  - 'application/json' -> 'Generic Error' **(x1 rows)**

## v1_transactions_investigations.251111.xlsm
### Sheet: 400
- **Column 4** (1 edits):
  - 'schema' -> 'header' **(x1 rows)**

### Sheet: 401
- **Column 1** (1 edits):
  - 'application/json' -> 'Unauthorized' **(x1 rows)**

### Sheet: 403
- **Column 1** (1 edits):
  - 'application/json' -> 'Forbidden' **(x1 rows)**

### Sheet: 409
- **Column 1** (1 edits):
  - 'application/json' -> 'Conflict' **(x1 rows)**

### Sheet: 429
- **Column 1** (1 edits):
  - 'application/json' -> 'Too many requests' **(x1 rows)**

### Sheet: 500
- **Column 1** (1 edits):
  - 'application/json' -> 'Generic Error' **(x1 rows)**

## v1_transactions_investigations_reports.251111.xlsm
### Sheet: 202
- **Column 4** (1 edits):
  - 'headers' -> 'header' **(x1 rows)**

### Sheet: 400
- **Column 4** (1 edits):
  - 'schema' -> 'header' **(x1 rows)**

### Sheet: 401
- **Column 1** (1 edits):
  - 'application/json' -> 'Unauthorized' **(x1 rows)**

### Sheet: 403
- **Column 1** (1 edits):
  - 'application/json' -> 'Forbidden' **(x1 rows)**

### Sheet: 409
- **Column 1** (1 edits):
  - 'application/json' -> 'Conflict' **(x1 rows)**

### Sheet: 429
- **Column 1** (1 edits):
  - 'application/json' -> 'Too many requests' **(x1 rows)**

### Sheet: 500
- **Column 1** (1 edits):
  - 'application/json' -> 'Generic Error' **(x1 rows)**

### Sheet: Body Example
- **Column 1** (2 edits):
  - '{ **(x2 rows)**

## v1_transactions_investigations_reports_{reportId}.251111.xlsm
### Sheet: 400
- **Column 4** (1 edits):
  - 'schema' -> 'header' **(x1 rows)**

### Sheet: 401
- **Column 1** (1 edits):
  - 'application/json' -> 'Unauthorized' **(x1 rows)**

### Sheet: 403
- **Column 1** (1 edits):
  - 'application/json' -> 'Forbidden' **(x1 rows)**

### Sheet: 404
- **Column 1** (1 edits):
  - 'application/json' -> 'Not Found' **(x1 rows)**

### Sheet: 409
- **Column 1** (1 edits):
  - 'application/json' -> 'Conflict' **(x1 rows)**

### Sheet: 429
- **Column 1** (1 edits):
  - 'application/json' -> 'Too many requests' **(x1 rows)**

### Sheet: 500
- **Column 1** (1 edits):
  - 'application/json' -> 'Generic Error' **(x1 rows)**

## v1_transactions_investigations_{fuid}.251111.xlsm
### Sheet: 200
- **Column Unknown** (1 edits):
  - ADDED Row Key='headers' **(x1 rows)**

### Sheet: 400
- **Column 4** (1 edits):
  - 'schema' -> 'header' **(x1 rows)**

### Sheet: 401
- **Column 1** (1 edits):
  - 'application/json' -> 'Unauthorized' **(x1 rows)**

### Sheet: 403
- **Column 1** (1 edits):
  - 'application/json' -> 'Forbidden' **(x1 rows)**

### Sheet: 404
- **Column 1** (1 edits):
  - 'application/json' -> 'Not Found' **(x1 rows)**

### Sheet: 409
- **Column 1** (1 edits):
  - 'application/json' -> 'Conflict' **(x1 rows)**

### Sheet: 429
- **Column 1** (1 edits):
  - 'application/json' -> 'Too many requests' **(x1 rows)**

### Sheet: 500
- **Column 1** (1 edits):
  - 'application/json' -> 'Generic Error' **(x1 rows)**

## vop_v1_payee_verifications.251111.xlsm
### Sheet: 200
- **Column 1** (2 edits):
  - 'X-Request-ID' -> 'X-Response-Timestamp' **(x1 rows)**
  - 'X-Response-Timestamp' -> 'X-Request-ID' **(x1 rows)**
- **Column 7** (2 edits):
  - 'uuid' -> 'date-time' **(x1 rows)**
  - 'date-time' -> 'uuid' **(x1 rows)**
- **Column 14** (2 edits):
  - 'a206e009-ef37-4040-924d-db758b29b200' -> '2024-08-12T15:19:22.678Z' **(x1 rows)**
  - '2024-08-12T15:19:22.678Z' -> 'a206e009-ef37-4040-924d-db758b29b200' **(x1 rows)**

### Sheet: 400
- **Column 1** (2 edits):
  - 'X-Request-ID' -> 'X-Response-Timestamp' **(x1 rows)**
  - 'X-Response-Timestamp' -> 'X-Request-ID' **(x1 rows)**
- **Column 4** (2 edits):
  - 'string' -> 'header' **(x2 rows)**
- **Column 7** (2 edits):
  - 'uuid' -> 'date-time' **(x1 rows)**
  - 'date-time' -> 'uuid' **(x1 rows)**
- **Column 14** (2 edits):
  - '' -> '2024-08-12T15:19:22.678Z' **(x1 rows)**
  - '2024-08-12T15:19:22.678Z' -> '' **(x1 rows)**

### Sheet: 401
- **Column 1** (3 edits):
  - 'X-Request-ID' -> 'Unauthorized' **(x1 rows)**
  - 'X-Request-ID' -> 'X-Response-Timestamp' **(x1 rows)**
  - 'X-Response-Timestamp' -> 'Unauthorized' **(x1 rows)**
- **Column 4** (2 edits):
  - 'string' -> 'response' **(x2 rows)**
- **Column 7** (2 edits):
  - 'uuid' -> 'date-time' **(x1 rows)**
  - 'date-time' -> 'uuid' **(x1 rows)**
- **Column 14** (2 edits):
  - '' -> '2024-08-12T15:19:22.678Z' **(x1 rows)**
  - '2024-08-12T15:19:22.678Z' -> '' **(x1 rows)**

### Sheet: 500
- **Column 1** (3 edits):
  - 'X-Request-ID' -> 'Generic Error' **(x1 rows)**
  - 'X-Request-ID' -> 'X-Response-Timestamp' **(x1 rows)**
  - 'X-Response-Timestamp' -> 'Generic Error' **(x1 rows)**
- **Column 4** (2 edits):
  - 'string' -> 'response' **(x2 rows)**
- **Column 7** (2 edits):
  - 'uuid' -> 'date-time' **(x1 rows)**
  - 'date-time' -> 'uuid' **(x1 rows)**
- **Column 14** (2 edits):
  - '' -> '2024-08-12T15:19:22.678Z' **(x1 rows)**
  - '2024-08-12T15:19:22.678Z' -> '' **(x1 rows)**

### Sheet: Body Example
- **Column 1** (2 edits):
  - '{ **(x2 rows)**
