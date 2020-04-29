# DocumentRecurring

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_date** | **date** | Must be in the future | 
**frequency** | **str** |  | [optional] [default to 'MONTHLY']
**frequency_special** | **str** |  | [optional] [default to 'null']
**interval** | **int** |  | [optional] 
**end_date_or_count** | **str** | Date of last exectution day or number of times to exectute | [optional] [default to 'null']
**status** | **str** |  | [optional] [default to 'WAITING']
**as_draft** | **bool** |  | [optional] [default to False]
**is_notify** | **bool** |  | [optional] [default to False]
**send_as** | **str** |  | [optional] [default to 'null']
**is_sign** | **bool** |  | [optional] [default to False]
**is_paid** | **bool** |  | [optional] [default to False]
**paid_date_option** | **str** | Option is used to determine what date is used for the payment if is_paid is true. \&quot;next_valid_date\&quot; selects the next workday in regards to the created date of the document if the date falls on a saturday or sunday. | [optional] [default to 'created_date']
**is_sepa** | **bool** |  | [optional] [default to False]
**sepa_local_instrument** | **str** |  | [optional] [default to 'null']
**sepa_sequence_type** | **str** |  | [optional] [default to 'null']
**sepa_reference** | **str** |  | [optional] [default to 'null']
**sepa_remittance_information** | **str** |  | [optional] [default to 'null']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


