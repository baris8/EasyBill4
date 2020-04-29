# CustomerSnapshot

A snapshot of the customer model which belongs to a document. This model is readonly and the state is final after finalization of the document. It's is identical to the state of the customer model at the time of finalization. Updates to the actual customer dataset won't affect this snapshot, however if you update the document the customer and therefore the customer snapshot may reflect a different state.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


