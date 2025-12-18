# Change Request Summary
This document summarizes the systematic updates required to align the templates.

## File: `$index.xlsm`
### Sheet: **General Description**
- **Column 1** (2 changes):
    - '/fpad' -> '' (x1)
    - '' -> '/fpad' (x1)
- **Column 3** (2 changes):
    - 'Server base path' -> '' (x1)
    - '' -> 'Server base path' (x1)

### Sheet: **Parameters**
- **Column 2** (1 changes):
    - 'header' -> 'path' (x1)
- **Column 7** (3 changes):
    - '' -> 'Yes' (x2)
    - 'M' -> 'Yes' (x1)

### Sheet: **Paths**
- **Column 1** (1 changes):
    - '/v1/transactions/assessments' -> '/vop/v1/payee-verifications' (x1)
- **Column 2** (1 changes):
    - 'Transacyion Assessments' -> 'Vop Payee-verifications' (x1)
- **Column 4** (2 changes):
    - 'Performs a simultaneous Account Assessment and Verification of Payee request for an account, identified by an IBAN. (x1)
    - 'This operation creates a pre-validation risk assessment for a (x1)
- **Column 6** (1 changes):
    - 'Create Transaction Assessment' -> 'Perform Verification Of Payee (VOP)' (x1)
- **Column 7** (1 changes):
    - 'create-transaction-assessment' -> 'postVerificationOfPayeeRequests' (x1)
- **Column 8** (1 changes):
    - 'x-sandbox-rule-type: SCRIPT_JS (x1)
- **Column ??** (1 changes):
    - ADDED Row Key='v1_transactions_assessments.251111' (x1)

### Sheet: **Responses**
- **Column 1** (2046 changes):
    - 'x-sandbox-request-name' -> 'value' (x35)
    - 'x-sandbox-request-headers' -> 'value' (x35)
    - 'senderBic' -> 'value' (x35)
    - 'pri' -> 'value' (x35)
    - 'value' -> 'x-sandbox-request-name' (x35)
    - ... and 269 other variations.
- **Column 2** (2020 changes):
    - 'x-sandbox-request-headers' -> 'errors' (x90)
    - 'errors' -> 'x-sandbox-request-headers' (x90)
    - 'text/plain' -> 'x-sandbox-request-headers' (x50)
    - 'x-sandbox-request-headers' -> 'text/plain' (x50)
    - 'text/plain' -> 'errors' (x45)
    - ... and 157 other variations.
- **Column 3** (30 changes):
    - 'Error message' -> '' (x15)
    - '' -> 'Error message' (x15)
- **Column 4** (1190 changes):
    - '' -> 'string' (x448)
    - 'string' -> '' (x448)
    - 'string' -> 'array' (x84)
    - 'array' -> 'string' (x84)
    - '' -> 'array' (x48)
    - ... and 3 other variations.
- **Column 6** (30 changes):
    - '' -> 'ErrorResponse' (x15)
    - 'ErrorResponse' -> '' (x15)
- **Column 14** (1754 changes):
    - '' -> 'OK' (x95)
    - '' -> 'FPADITMM' (x95)
    - '' -> 'a206e009-ef37-4040-924d-db758b29b401' (x95)
    - 'OK' -> '' (x95)
    - 'FPADITMM' -> '' (x95)
    - ... and 205 other variations.

### Sheet: **Schemas**
- **Column 2** (31 changes):
    - 'BIC of the Agent managing the Creditor's Account present in the (x2)
    - 'IBAN identifies the Creditor's Account present in the potential (x2)
    - 'BIC of the Agent managing the Debtor's Account present in the (x2)
    - '' -> 'Standard amount.' (x1)
    - 'Structure of a transaction assessment request, with all data of a (x1)
    - ... and 23 other variations.
- **Column 3** (7 changes):
    - 'object' -> 'schema' (x4)
    - '' -> 'string' (x2)
    - 'String' -> 'string' (x1)
- **Column 4** (6 changes):
    - 'schema' -> 'VopBulkIdentification' (x1)
    - 'schema' -> 'HateoasBlock' (x1)
    - 'schema' -> 'ShortMessage' (x1)
    - 'schema' -> 'GenericOrganisationIdentification' (x1)
    - 'schema' -> 'Ria' (x1)
    - ... and 1 other variations.
- **Column 5** (11 changes):
    - '' -> 'Max35Text' (x2)
    - 'iban' -> 'Iban' (x1)
    - 'VopBulkIdentification' -> '' (x1)
    - '' -> 'Max256Text' (x1)
    - 'HateoasBlock' -> '' (x1)
    - ... and 5 other variations.
- **Column 7** (5 changes):
    - 'M' -> 'Yes' (x3)
    - '' -> 'No' (x1)
    - 'M' -> 'No' (x1)
- **Column 11** (1 changes):
    - '[A-Z0-9]{18}[0-9]{2}$' -> '^[A-Z0-9]{18}[0-9]{2}$' (x1)
- **Column 12** (4 changes):
    - 'FORMAT_ERROR, CLIENT_INVALID, CLIENT_INCONSISTENT, TIMESTAMP_INVALID' -> 'FORMAT_ERROR,CLIENT_INVALID,CLIENT_INCONSISTENT,TIMESTAMP_INVALID' (x1)
    - 'BANK, CBID, CHID, CINC, COID, CUST, DUNS, EMPL, GS1G, SREN, SRET, TXID, BDID, BOID' -> 'BANK,CBID,CHID,CINC,COID,CUST,DUNS,EMPL,GS1G,SREN,SRET,TXID,BDID,BOID' (x1)
    - 'SCT, SCTInst' -> 'SCT,SCTInst' (x1)
    - '' -> 'INFO,WARNING,ERROR' (x1)
- **Column 13** (5 changes):
    - '{rel: next (x1)
    - '{instructingAgentBic: FPADITMM (x1)
    - '{messageType: WARNING (x1)
    - '{serviceType: SCT (x1)
    - '2024-08-12T15:19:22.678Z' -> '2024-08-12 15:19:22.678000+00:00' (x1)
- **Column ??** (14 changes):
    - ADDED Row Key='dateTime | errors' (x1)
    - ADDED Row Key='identification | PartyType' (x1)
    - ADDED Row Key='modelOutcome | RiskInfoArray' (x1)
    - ADDED Row Key='name | PartyType' (x1)
    - ADDED Row Key='transactionId | AssessmentTransactionData' (x1)
    - ... and 9 other variations.

---
## File: `account_assessment.251111.xlsm`
### Sheet: **201**
- **Column 2** (2 changes):
    - 'CREATED' -> 'Created' (x1)
    - '' -> 'application/json' (x1)

### Sheet: **400**
- **Column 1** (30 changes):
    - 'Bad Request' -> 'value' (x1)
    - 'Bad Request' -> 'errors' (x1)
    - 'Bad Request' -> 'dateTime' (x1)
    - 'Bad Request' -> 'code' (x1)
    - 'Bad Request' -> 'description' (x1)
    - ... and 25 other variations.
- **Column 2** (24 changes):
    - 'application/json' -> 'errors[0]' (x3)
    - 'Bad Request' -> 'errors[0]' (x3)
    - 'value' -> 'errors[0]' (x3)
    - 'errors[0]' -> 'application/json' (x3)
    - 'errors[0]' -> 'Bad Request' (x3)
    - ... and 7 other variations.
- **Column 4** (22 changes):
    - '' -> 'string' (x6)
    - 'string' -> '' (x6)
    - 'array' -> 'string' (x3)
    - 'string' -> 'array' (x3)
    - '' -> 'array' (x2)
    - ... and 1 other variations.
- **Column 14** (24 changes):
    - '' -> '2019-08-24T14:15:22Z' (x3)
    - '' -> 'E400' (x3)
    - '' -> 'Field 'status' is required.' (x3)
    - '2019-08-24T14:15:22Z' -> '' (x3)
    - 'E400' -> '' (x3)
    - ... and 7 other variations.

### Sheet: **Body Example**
- **Column 1** (2 changes):
    - '{ (x2)

---
## File: `account_assessment_vop.251111.xlsm`
### Sheet: **201**
- **Column 1** (6 changes):
    - 'fri' -> 'pri' (x1)
    - 'fri' -> 'X-Response-Timestamp' (x1)
    - 'pri' -> 'fri' (x1)
    - 'pri' -> 'X-Response-Timestamp' (x1)
    - 'X-Response-Timestamp' -> 'fri' (x1)
    - ... and 1 other variations.
- **Column 3** (7 changes):
    - '' -> 'Created' (x1)
    - '' -> 'Participant Request Identifier used also as Requesting PSP’s reference number of the VOP Request **(T054)**.' (x1)
    - '' -> 'Time stamp of provided by the responding PSP **(T061)**.' (x1)
    - 'Participant Request Identifier used also as Requesting PSP’s reference number of the VOP Request **(T054)**.' -> 'Created' (x1)
    - 'Participant Request Identifier used also as Requesting PSP’s reference number of the VOP Request **(T054)**.' -> 'Time stamp of provided by the responding PSP **(T061)**.' (x1)
    - ... and 2 other variations.
- **Column 4** (4 changes):
    - 'header' -> 'string' (x2)
    - 'string' -> 'header' (x2)
- **Column 6** (6 changes):
    - 'FpadResponseIdentifier' -> 'pri' (x1)
    - 'FpadResponseIdentifier' -> '' (x1)
    - 'pri' -> 'FpadResponseIdentifier' (x1)
    - 'pri' -> '' (x1)
    - '' -> 'FpadResponseIdentifier' (x1)
    - ... and 1 other variations.
- **Column 7** (4 changes):
    - '' -> 'date-format' (x2)
    - 'date-format' -> '' (x2)
- **Column 8** (4 changes):
    - '' -> 'M' (x2)
    - 'M' -> '' (x2)
- **Column 14** (4 changes):
    - '' -> '2024-08-12T15:19:22.678Z' (x2)
    - '2024-08-12T15:19:22.678Z' -> '' (x2)

### Sheet: **400**
- **Column 1** (2 changes):
    - 'fri' -> 'X-Response-Timestamp' (x1)
    - 'X-Response-Timestamp' -> 'fri' (x1)
- **Column 4** (2 changes):
    - 'header' -> 'string' (x1)
    - 'string' -> 'header' (x1)
- **Column 6** (2 changes):
    - 'FpadResponseIdentifier' -> '' (x1)
    - '' -> 'FpadResponseIdentifier' (x1)
- **Column 7** (2 changes):
    - '' -> 'date-format' (x1)
    - 'date-format' -> '' (x1)
- **Column 8** (2 changes):
    - '' -> 'M' (x1)
    - 'M' -> '' (x1)
- **Column 14** (2 changes):
    - '' -> '2024-08-12T15:19:22.678Z' (x1)
    - '2024-08-12T15:19:22.678Z' -> '' (x1)

### Sheet: **Body Example**
- **Column 1** (2 changes):
    - '{ (x2)

---
## File: `account_assessment_vop_bulk.251111.xlsm`
### Sheet: **201**
- **Column 1** (2 changes):
    - 'fri' -> 'pri' (x1)
    - 'pri' -> 'fri' (x1)
- **Column 3** (3 changes):
    - '' -> 'Created' (x1)
    - '' -> 'Participant Request Identifier used also as Requesting PSP’s reference number of the VOP Request **(T054)**.' (x1)
    - 'Participant Request Identifier used also as Requesting PSP’s reference number of the VOP Request **(T054)**.' -> 'Created' (x1)
- **Column 6** (2 changes):
    - 'FpadResponseIdentifier' -> 'pri' (x1)
    - 'pri' -> 'FpadResponseIdentifier' (x1)

### Sheet: **409**
- **Column 1** (1 changes):
    - '' -> 'Conflict' (x1)

---
## File: `v1_eds_local-file.251111.xlsm`
### Sheet: **400**
- **Column 4** (1 changes):
    - 'schema' -> 'header' (x1)

### Sheet: **401**
- **Column 1** (1 changes):
    - 'application/json' -> 'Unauthorized' (x1)

### Sheet: **403**
- **Column 1** (1 changes):
    - 'application/json' -> 'Forbidden' (x1)

### Sheet: **409**
- **Column 1** (1 changes):
    - 'application/json' -> 'Conflict' (x1)

### Sheet: **429**
- **Column 1** (1 changes):
    - 'application/json' -> 'Too many requests' (x1)

### Sheet: **500**
- **Column 1** (1 changes):
    - 'application/json' -> 'Generic Error' (x1)

---
## File: `v1_risk-info_feedbacks.251111.xlsm`
### Sheet: **201**
- **Column 3** (1 changes):
    - '' -> 'Created' (x1)
- **Column 4** (1 changes):
    - 'headers' -> 'header' (x1)

### Sheet: **400**
- **Column 4** (1 changes):
    - 'schema' -> 'header' (x1)

### Sheet: **401**
- **Column 1** (1 changes):
    - 'application/json' -> 'Unauthorized' (x1)

### Sheet: **403**
- **Column 1** (1 changes):
    - 'application/json' -> 'Forbidden' (x1)

### Sheet: **409**
- **Column 1** (1 changes):
    - 'application/json' -> 'Conflict' (x1)

### Sheet: **429**
- **Column 1** (1 changes):
    - 'application/json' -> 'Too many requests' (x1)

### Sheet: **500**
- **Column 1** (1 changes):
    - 'application/json' -> 'Generic Error' (x1)

### Sheet: **Body Example**
- **Column 1** (2 changes):
    - '{ (x2)

---
## File: `v1_transactions_assessments.251111.xlsm`
### Sheet: **201**
- **Column 3** (1 changes):
    - '' -> 'Created' (x1)

### Sheet: **400**
- **Column 4** (1 changes):
    - 'schema' -> 'header' (x1)

### Sheet: **401**
- **Column 1** (1 changes):
    - 'application/json' -> 'Unauthorized' (x1)

### Sheet: **403**
- **Column 1** (1 changes):
    - 'application/json' -> 'Forbidden' (x1)

### Sheet: **409**
- **Column 1** (1 changes):
    - 'application/json' -> 'Conflict' (x1)

### Sheet: **429**
- **Column 1** (1 changes):
    - 'application/json' -> 'Too many requests' (x1)

### Sheet: **500**
- **Column 1** (1 changes):
    - 'application/json' -> 'Generic Error' (x1)

---
## File: `v1_transactions_investigations.251111.xlsm`
### Sheet: **400**
- **Column 4** (1 changes):
    - 'schema' -> 'header' (x1)

### Sheet: **401**
- **Column 1** (1 changes):
    - 'application/json' -> 'Unauthorized' (x1)

### Sheet: **403**
- **Column 1** (1 changes):
    - 'application/json' -> 'Forbidden' (x1)

### Sheet: **409**
- **Column 1** (1 changes):
    - 'application/json' -> 'Conflict' (x1)

### Sheet: **429**
- **Column 1** (1 changes):
    - 'application/json' -> 'Too many requests' (x1)

### Sheet: **500**
- **Column 1** (1 changes):
    - 'application/json' -> 'Generic Error' (x1)

---
## File: `v1_transactions_investigations_reports.251111.xlsm`
### Sheet: **202**
- **Column 4** (1 changes):
    - 'headers' -> 'header' (x1)

### Sheet: **400**
- **Column 4** (1 changes):
    - 'schema' -> 'header' (x1)

### Sheet: **401**
- **Column 1** (1 changes):
    - 'application/json' -> 'Unauthorized' (x1)

### Sheet: **403**
- **Column 1** (1 changes):
    - 'application/json' -> 'Forbidden' (x1)

### Sheet: **409**
- **Column 1** (1 changes):
    - 'application/json' -> 'Conflict' (x1)

### Sheet: **429**
- **Column 1** (1 changes):
    - 'application/json' -> 'Too many requests' (x1)

### Sheet: **500**
- **Column 1** (1 changes):
    - 'application/json' -> 'Generic Error' (x1)

### Sheet: **Body Example**
- **Column 1** (2 changes):
    - '{ (x2)

---
## File: `v1_transactions_investigations_reports_{reportId}.251111.xlsm`
### Sheet: **400**
- **Column 4** (1 changes):
    - 'schema' -> 'header' (x1)

### Sheet: **401**
- **Column 1** (1 changes):
    - 'application/json' -> 'Unauthorized' (x1)

### Sheet: **403**
- **Column 1** (1 changes):
    - 'application/json' -> 'Forbidden' (x1)

### Sheet: **404**
- **Column 1** (1 changes):
    - 'application/json' -> 'Not Found' (x1)

### Sheet: **409**
- **Column 1** (1 changes):
    - 'application/json' -> 'Conflict' (x1)

### Sheet: **429**
- **Column 1** (1 changes):
    - 'application/json' -> 'Too many requests' (x1)

### Sheet: **500**
- **Column 1** (1 changes):
    - 'application/json' -> 'Generic Error' (x1)

---
## File: `v1_transactions_investigations_{fuid}.251111.xlsm`
### Sheet: **200**
- **Column ??** (1 changes):
    - ADDED Row Key='headers' (x1)

### Sheet: **400**
- **Column 4** (1 changes):
    - 'schema' -> 'header' (x1)

### Sheet: **401**
- **Column 1** (1 changes):
    - 'application/json' -> 'Unauthorized' (x1)

### Sheet: **403**
- **Column 1** (1 changes):
    - 'application/json' -> 'Forbidden' (x1)

### Sheet: **404**
- **Column 1** (1 changes):
    - 'application/json' -> 'Not Found' (x1)

### Sheet: **409**
- **Column 1** (1 changes):
    - 'application/json' -> 'Conflict' (x1)

### Sheet: **429**
- **Column 1** (1 changes):
    - 'application/json' -> 'Too many requests' (x1)

### Sheet: **500**
- **Column 1** (1 changes):
    - 'application/json' -> 'Generic Error' (x1)

---
## File: `vop_v1_payee_verifications.251111.xlsm`
### Sheet: **200**
- **Column 1** (2 changes):
    - 'X-Request-ID' -> 'X-Response-Timestamp' (x1)
    - 'X-Response-Timestamp' -> 'X-Request-ID' (x1)
- **Column 7** (2 changes):
    - 'uuid' -> 'date-time' (x1)
    - 'date-time' -> 'uuid' (x1)
- **Column 14** (2 changes):
    - 'a206e009-ef37-4040-924d-db758b29b200' -> '2024-08-12T15:19:22.678Z' (x1)
    - '2024-08-12T15:19:22.678Z' -> 'a206e009-ef37-4040-924d-db758b29b200' (x1)

### Sheet: **400**
- **Column 1** (2 changes):
    - 'X-Request-ID' -> 'X-Response-Timestamp' (x1)
    - 'X-Response-Timestamp' -> 'X-Request-ID' (x1)
- **Column 4** (2 changes):
    - 'string' -> 'header' (x2)
- **Column 7** (2 changes):
    - 'uuid' -> 'date-time' (x1)
    - 'date-time' -> 'uuid' (x1)
- **Column 14** (2 changes):
    - '' -> '2024-08-12T15:19:22.678Z' (x1)
    - '2024-08-12T15:19:22.678Z' -> '' (x1)

### Sheet: **401**
- **Column 1** (3 changes):
    - 'X-Request-ID' -> 'Unauthorized' (x1)
    - 'X-Request-ID' -> 'X-Response-Timestamp' (x1)
    - 'X-Response-Timestamp' -> 'Unauthorized' (x1)
- **Column 4** (2 changes):
    - 'string' -> 'response' (x2)
- **Column 7** (2 changes):
    - 'uuid' -> 'date-time' (x1)
    - 'date-time' -> 'uuid' (x1)
- **Column 14** (2 changes):
    - '' -> '2024-08-12T15:19:22.678Z' (x1)
    - '2024-08-12T15:19:22.678Z' -> '' (x1)

### Sheet: **500**
- **Column 1** (3 changes):
    - 'X-Request-ID' -> 'Generic Error' (x1)
    - 'X-Request-ID' -> 'X-Response-Timestamp' (x1)
    - 'X-Response-Timestamp' -> 'Generic Error' (x1)
- **Column 4** (2 changes):
    - 'string' -> 'response' (x2)
- **Column 7** (2 changes):
    - 'uuid' -> 'date-time' (x1)
    - 'date-time' -> 'uuid' (x1)
- **Column 14** (2 changes):
    - '' -> '2024-08-12T15:19:22.678Z' (x1)
    - '2024-08-12T15:19:22.678Z' -> '' (x1)

### Sheet: **Body Example**
- **Column 1** (2 changes):
    - '{ (x2)

---