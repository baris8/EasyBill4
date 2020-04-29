# SEPAPayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Amount in cents (e.g. \&quot;150\&quot; &#x3D; 1.50€) | 
**created_at** | **datetime** |  | [optional] [readonly] 
**creditor_bic** | **str** | If type is DEBIT, this field is overwritten with the selected bank account data on export. | [optional] [default to 'null']
**creditor_iban** | **str** | Mandatory if type is CREDIT. If type is DEBIT, this field is overwritten with the selected bank account data on export. | [optional] 
**creditor_name** | **str** | Mandatory if type is CREDIT. If type is DEBIT, this field is overwritten with the selected bank account data on export. | [optional] 
**debitor_bic** | **str** | If type is CREDIT, this field is overwritten with the selected bank account data on export. | [optional] [default to 'null']
**debitor_iban** | **str** | Mandatory if type is DEBIT. If type is CREDIT, this field is overwritten with the selected bank account data on export. | 
**debitor_name** | **str** | Mandatory if type is DEBIT. If type is CREDIT, this field is overwritten with the selected bank account data on export. | 
**document_id** | **int** |  | 
**export_at** | **datetime** | If a date is set, this record is marked as exported | [optional] 
**export_error** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**local_instrument** | **str** | CORE: SEPA Core Direct Debit&lt;br/&gt; COR1: SEPA-Basislastschrift COR1&lt;br/&gt; B2B: SEPA Business to Business Direct Debit | 
**mandate_date_of_signature** | **date** |  | 
**mandate_id** | **str** |  | 
**reference** | **str** |  | 
**remittance_information** | **str** |  | [optional] [default to 'null']
**requested_at** | **date** | Booking date | [optional] 
**sequence_type** | **str** | FRST: Erstlastschrift&lt;br/&gt; RCUR: Folgelastschrift&lt;br/&gt; OOFF: Einmallastschrift&lt;br/&gt; FNAL: Letztmalige Lastschrift | 
**updated_at** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [default to 'DEBIT']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


