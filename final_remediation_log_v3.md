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
- **Column Unknown** (2 edits):
  - ADDED Row Key='v1_transactions_assessments.251111' **(x1 rows)**
  - REMOVED Row Key='vop_v1_payee_verifications.251111' **(x1 rows)**

### Sheet: Schemas
- **Column 2** (11 edits):
  - '' -> 'Standard amount.' **(x1 rows)**
  - 'Business Identifier Code (BIC) in 8 or 11 characters format' -> 'Business Identifier Code (BIC) in 8 or 11 characters format.' **(x1 rows)**
  - 'BIC of the Agent managing the Creditor's Account present in the transaction.\r\nIf a 8 characters BIC is assigned as value, all transactions having a creditorBic starting with the same 8 characters will be considered.' -> 'BIC of the Agent managing the Creditor's Account present in the transaction. If a 8 characters BIC is assigned as value, all transactions having a creditorBic starting with the same 8 characters will be considered.' **(x1 rows)**
  - 'Name associated with the Creditor's Account present in the transaction.\r\n All transactions starting with the value assigned will be considered.' -> 'Name associated with the Creditor's Account present in the transaction. All transactions starting with the value assigned will be considered.' **(x1 rows)**
  - 'BIC of the Agent managing the Debtor's Account present in the transaction.\r\nIf a 8 characters BIC is assigned as value, all transactions having a debtorBic starting with the same 8 characters will be considered.' -> 'BIC of the Agent managing the Debtor's Account present in the transaction. If a 8 characters BIC is assigned as value, all transactions having a debtorBic starting with the same 8 characters will be considered.' **(x1 rows)**
  - 'Name associated with the Debtor's Account present in the transaction.\r\nAll transactions starting with the value assigned will be considered.' -> 'Name associated with the Debtor's Account present in the transaction. All transactions starting with the value assigned will be considered.' **(x1 rows)**
  - 'Maximum reference date and time. It cannot exceed 3 days from *minReferenceDateTime*.\r\nReference Date Time must be intended as *settlementDate* for SCT and *acceptanceDateTime* for SCTInst.' -> 'Maximum reference date and time. It cannot exceed 3 days from *minReferenceDateTime*. Reference Date Time must be intended as *settlementDate* for SCT and *acceptanceDateTime* for SCTInst.' **(x1 rows)**
  - 'Minimum reference date and time.\r\nReference Date Time must be intended as *settlementDate* for SCT and *acceptanceDateTime* for SCTInst.' -> 'Minimum reference date and time. Reference Date Time must be intended as *settlementDate* for SCT and *acceptanceDateTime* for SCTInst.' **(x1 rows)**
  - 'Reference date and time of the potential transaction that has to be assessed.\r\nIt must me intended as *settlementDate* for SCT and *acceptanceDateTime* for SCTInst services.' -> 'Reference date and time of the potential transaction that has to be assessed. It must me intended as *settlementDate* for SCT and *acceptanceDateTime* for SCTInst services.' **(x1 rows)**
  - 'Reference date and time of the transaction.\r\nIt must be intended as *settlementDate* for SCT and *acceptanceDtateTime* for SCTInst transactions.' -> 'Reference date and time of the transaction. It must be intended as *settlementDate* for SCT and *acceptanceDtateTime* for SCTInst transactions.' **(x1 rows)**
  - 'Identifier of the transaction, unique for the Debtor''s Agent.' -> 'Identifier of the transaction, unique for the Debtor's Agent.' **(x1 rows)**
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
  - '{rel: next href: | /transactions/investigations/reports/fc91e31c-820f-4a9e-94ba-371cb2dcaa1d?page=2}' -> '{'rel': 'next', 'href': '/transactions/investigations/reports/fc91e31c-820f-4a9e-94ba-371cb2dcaa1d?page=2\n'}' **(x1 rows)**
  - '{instructingAgentBic: FPADITMM instructedAgentBic: FPADITMM transactionId: string debtorName: string debtorBic: FPADITMMXXX debtorIban: IT78K0300203280111271851199 creditorName: string creditorBic: FPADITMMXXX creditorIban: IT78K0300203280111271851199 amount: 340.75 currency: EUR referenceDateTime: '2019-08-24T14:15:22Z' categoryPurpose: ABCD purposeCode: ABCD}' -> '{'instructingAgentBic': 'FPADITMM', 'instructedAgentBic': 'FPADITMM', 'transactionId': 'string', 'debtorName': 'string', 'debtorBic': 'FPADITMMXXX', 'debtorIban': 'IT78K0300203280111271851199', 'creditorName': 'string', 'creditorBic': 'FPADITMMXXX', 'creditorIban': 'IT78K0300203280111271851199', 'amount': 340.75, 'currency': 'EUR', 'referenceDateTime': '2019-08-24T14:15:22Z', 'categoryPurpose': 'ABCD', 'purposeCode': 'ABCD'}' **(x1 rows)**
  - '{messageType: WARNING messageCode: W001 messageText: Partial outcome.}' -> '{'messageType': 'WARNING', 'messageCode': 'W001', 'messageText': 'Partial outcome.'}' **(x1 rows)**
  - '{serviceType: SCT debtorBic: FPADITMMXXX transactionId: 41e400e45 referenceDateTime: '2019-08-24T14:15:22Z'}' -> '{'serviceType': 'SCT', 'debtorBic': 'FPADITMMXXX', 'transactionId': '41e400e45', 'referenceDateTime': '2019-08-24T14:15:22Z'}' **(x1 rows)**
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
  - '{ accountName: Mario Rossi accountBic: FPADITMMXXX requestedModels: - modelName: Model1 modelVersion: '1.0' - modelName: Model2 modelVersion: '1.0' }' -> 'accountName: Mario Rossi accountBic: FPADITMMXXX requestedModels: - modelName: Model1 modelVersion: '1.0' - modelName: Model2 modelVersion: '1.0'' **(x1 rows)**
  - '{ accountName: Mario Rossi accountBic: FPADITMMXXX accountIban: IT02E0300203280782375262458 requestedModels: - modelName: Model1 modelVersion: '1.0' - modelName: Model2 modelVersion: '1.0' }' -> 'accountName: Mario Rossi accountBic: FPADITMMXXX accountIban: IT02E0300203280782375262458 requestedModels: - modelName: Model1 modelVersion: '1.0' - modelName: Model2 modelVersion: '1.0'' **(x1 rows)**

## account_assessment_vop.251111.xlsm
### Sheet: 201
- **Column 3** (1 edits):
  - '' -> 'Created' **(x1 rows)**

### Sheet: Body Example
- **Column 1** (2 edits):
  - '{ accountAssessment: requestedModels: - modelName: Model1 modelVersion: '1.0' - modelName: Model2 modelVersion: '1.0' vop: party: name: John Doe partyAccount: iban: IT76L0300203280825973665778 partyAgent: financialInstitutionId: bicfi: BICEXAMPLE1 }' -> 'accountAssessment: requestedModels: - modelName: Model1 modelVersion: '1.0' - modelName: Model2 modelVersion: '1.0' vop: party: name: John Doe partyAccount: iban: IT76L0300203280825973665778 partyAgent: financialInstitutionId: bicfi: BICEXAMPLE1' **(x1 rows)**
  - '{ accountAssessment: requestedModels: - modelName: Model1 modelVersion: '1.0' - modelName: Model2 modelVersion: '1.0' vop: party: name: John Doe partyAccount: iban: IT76L0300203280825973665778 partyAgent: financialInstitutionId: bicfi: BICEXAMPLE1 requestingAgent: financialInstitutionId: bicfi: BICEXAMPLE2 }' -> 'accountAssessment: requestedModels: - modelName: Model1 modelVersion: '1.0' - modelName: Model2 modelVersion: '1.0' vop: party: name: John Doe partyAccount: iban: IT76L0300203280825973665778 partyAgent: financialInstitutionId: bicfi: BICEXAMPLE1 requestingAgent: financialInstitutionId: bicfi: BICEXAMPLE2' **(x1 rows)**

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
  - LOWRISK' **(x2 rows)**

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
  - '{ reportName: Test }' -> 'reportName: Test' **(x1 rows)**
  - '{ transactionFilter: instructingAgentBic: FPADITMM serviceType: SCT debtorIban: IT78K0300203280111271851199 minAmount: 1000 currency: EUR minReferenceDateTime: '2023-05-01T00:00:00Z' maxReferenceDateTime: '2023-05-02T23:59:59Z' }' -> 'transactionFilter: instructingAgentBic: FPADITMM serviceType: SCT debtorIban: IT78K0300203280111271851199 minAmount: 1000 currency: EUR minReferenceDateTime: '2023-05-01T00:00:00Z' maxReferenceDateTime: '2023-05-02T23:59:59Z'' **(x1 rows)**

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
  - '{ value: party: name: John Doe partyAccount: iban: IT76L0300203280825973665778 partyAgent: financialInstitutionId: bicfi: BICEXAMPLE1 }' -> 'requestedModels: - modelName: Model1 modelVersion: '1.0' - modelName: Model5 modelVersion: '1.1'' **(x1 rows)**
  - '{ value: party: name: John Doe partyAccount: iban: IT76L0300203280825973665778 partyAgent: financialInstitutionId: bicfi: BICEXAMPLE1 requestingAgent: financialInstitutionId: bicfi: BICEXAMPLE2 }' -> 'transactionData: serviceType: SCTInst transactionId: 41e400e45 debtorName: Mario Rossi debtorBic: FPADITMMXXX debtorIban: IT02E0300203280782375262458 creditorName: Eric Mulder creditorBic: FPFPDEMM441 creditorIban: DE89370400440532013000 amount: 1000 currency: EUR referenceDateTime: '2023-03-23T14:15:22Z' categoryPurpose: ABCD purposeCode: ABCD requestedModels: - modelName: Model1 modelVersion: '1.0' - modelName: Model5 modelVersion: '1.1'' **(x1 rows)**
