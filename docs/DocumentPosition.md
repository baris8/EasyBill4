# DocumentPosition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** |  | [optional] [default to 'null']
**description** | **str** |  | [optional] [default to 'null']
**quantity** | **float** |  | [optional] [default to 1.0]
**quantity_str** | **str** | Use quantity_str if you want to set a quantity like: 1:30 h or 3x5 m. quantity_str overwrites quantity. | [optional] 
**unit** | **str** |  | [optional] [default to 'null']
**type** | **str** |  | [optional] [default to 'POSITION']
**position** | **int** | Automatic by default (first item: 1, second item: 2, ...) | [optional] 
**single_price_net** | **float** |  | [optional] 
**single_price_gross** | **float** |  | [optional] [readonly] 
**vat_percent** | **float** |  | [optional] [default to 0.0]
**discount** | **float** |  | [optional] 
**discount_type** | **str** |  | [optional] [default to 'null']
**position_id** | **int** | If set, values are copied from the referenced position | [optional] 
**total_price_net** | **float** |  | [optional] [readonly] 
**total_price_gross** | **float** |  | [optional] [readonly] 
**total_vat** | **float** |  | [optional] [readonly] 
**serial_number_id** | **str** |  | [optional] [readonly] 
**serial_number** | **str** |  | [optional] [readonly] 
**booking_account** | **str** |  | [optional] [default to 'null']
**export_cost_1** | **str** |  | [optional] [default to 'null']
**export_cost_2** | **str** |  | [optional] [default to 'null']
**cost_price_net** | **float** |  | [optional] 
**cost_price_total** | **float** |  | [optional] [readonly] 
**cost_price_charge** | **float** |  | [optional] [readonly] 
**cost_price_charge_type** | **str** |  | [optional] [readonly] 
**item_type** | **str** |  | [optional] [default to 'UNDEFINED']
**id** | **int** |  | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


