# Full Remediation Log
Complete list of differences detected between Original and Current templates.

## $index.xlsm
### Sheet: Parameters
- **Column 2** (1 edits):
  - 'header' -> 'path' **(x1 rows)**
- **Column 7** (3 edits):
  - '' -> 'Yes' **(x2 rows)**
  - 'M' -> 'Yes' **(x1 rows)**

### Sheet: Paths
- **Column 4** (1 edits):
  - 'Performs a simultaneous Account Assessment and Verification of Payee request for an account, identified by an IBAN. **(x1 rows)**
- **Column Unknown** (2 edits):
  - ADDED Row Key='v1_transactions_assessments.251111' **(x1 rows)**
  - REMOVED Row Key='vop_v1_payee_verifications.251111' **(x1 rows)**

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

### Sheet: Body Example
- **Column 1** (2 edits):
  - '{ **(x2 rows)**

## account_assessment_vop.251111.xlsm
### Sheet: 201
- **Column 3** (1 edits):
  - '' -> 'Created' **(x1 rows)**

### Sheet: Body Example
- **Column 1** (2 edits):
  - '{ **(x2 rows)**

## account_assessment_vop_bulk.251111.xlsm
### Sheet: 201
- **Column 3** (1 edits):
  - '' -> 'Created' **(x1 rows)**

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
### Sheet: 400
- **Column 4** (1 edits):
  - 'string' -> 'header' **(x1 rows)**

### Sheet: 401
- **Column 1** (1 edits):
  - 'X-Request-ID' -> 'Unauthorized' **(x1 rows)**
- **Column 4** (1 edits):
  - 'string' -> 'response' **(x1 rows)**

### Sheet: 500
- **Column 1** (1 edits):
  - 'X-Request-ID' -> 'Generic Error' **(x1 rows)**
- **Column 4** (1 edits):
  - 'string' -> 'response' **(x1 rows)**

### Sheet: Body Example
- **Column 1** (2 edits):
  - '{ **(x2 rows)**
