# Customer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquire_options** | **int** | 1 &#x3D; Empfehlung eines anderen Kunden, 2 &#x3D; Zeitungsanzeige, 3 &#x3D; Eigene Akquisition, 4 &#x3D; Mitarbeiter Akquisition, 5 &#x3D; Google, 6 &#x3D; Gelbe Seiten, 7 &#x3D; Kostenlose Internet Plattform, 8 &#x3D; Bezahlte Internet Plattform | [optional] 
**additional_groups_ids** | **list[int]** |  | [optional] [readonly] 
**bank_account** | **str** |  | [optional] 
**bank_account_owner** | **str** |  | [optional] 
**bank_bic** | **str** |  | [optional] 
**bank_code** | **str** |  | [optional] 
**bank_iban** | **str** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**birth_date** | **date** |  | [optional] 
**cash_allowance** | **float** |  | [optional] 
**cash_allowance_days** | **int** |  | [optional] 
**cash_discount** | **float** |  | [optional] 
**cash_discount_type** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**company_name** | **str** |  | 
**country** | **str** |  | [optional] 
**created_at** | **date** |  | [optional] [readonly] 
**updated_at** | **str** |  | [optional] [readonly] 
**delivery_city** | **str** |  | [optional] 
**delivery_company_name** | **str** |  | [optional] 
**delivery_country** | **str** |  | [optional] 
**delivery_first_name** | **str** |  | [optional] 
**delivery_last_name** | **str** |  | [optional] 
**delivery_personal** | **bool** |  | [optional] 
**delivery_salutation** | **int** | 0 &#x3D; nothing, 1 &#x3D; Mr, 2 &#x3D; Mrs, 3 &#x3D; Company, 4 &#x3D; Mr &amp; Mrs, 5 &#x3D; Married couple, 6 &#x3D; Family | [optional] 
**delivery_street** | **str** |  | [optional] 
**delivery_suffix_1** | **str** |  | [optional] 
**delivery_suffix_2** | **str** |  | [optional] 
**delivery_zip_code** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] [readonly] 
**emails** | **list[str]** |  | [optional] 
**fax** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**grace_period** | **int** | will be replaced by its alias due_in_days. | [optional] 
**due_in_days** | **int** | due date in days | [optional] 
**group_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] [readonly] 
**info_1** | **str** |  | [optional] 
**info_2** | **str** |  | [optional] 
**internet** | **str** |  | [optional] 
**last_name** | **str** |  | 
**login_id** | **int** |  | [optional] 
**mobile** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**number** | **str** | Automatically generated if empty. | [optional] 
**payment_options** | **int** | 1 &#x3D; Stets pünktliche Zahlung, 2 &#x3D; überwiegend pünktliche Zahlung, 3 &#x3D; überwiegend verspätete Zahlung, 5 &#x3D; Grundsätzlich verspätete Zahlung | [optional] 
**personal** | **bool** |  | [optional] [default to False]
**phone_1** | **str** |  | [optional] 
**phone_2** | **str** |  | [optional] 
**postbox** | **str** |  | [optional] 
**postbox_city** | **str** |  | [optional] 
**postbox_country** | **str** |  | [optional] 
**postbox_zip_code** | **str** |  | [optional] 
**sale_price_level** | **str** |  | [optional] 
**salutation** | **int** | 0 &#x3D; nothing, 1 &#x3D; Mr, 2 &#x3D; Mrs, 3 &#x3D; Company, 4 &#x3D; Mr &amp; Mrs, 5 &#x3D; Married couple, 6 &#x3D; Family | [optional] 
**sepa_agreement** | **str** | BASIC &#x3D; SEPA-Basislastschrift, COR1 &#x3D; SEPA-Basislastschrift COR1, COMPANY &#x3D; SEPA-Firmenlastschrift, NULL &#x3D; Noch kein Mandat erteilt | [optional] 
**sepa_agreement_date** | **date** |  | [optional] 
**sepa_mandate_reference** | **str** |  | [optional] 
**since_date** | **date** |  | [optional] 
**street** | **str** |  | [optional] 
**suffix_1** | **str** |  | [optional] 
**suffix_2** | **str** |  | [optional] 
**tax_number** | **str** |  | [optional] 
**court** | **str** |  | [optional] 
**court_registry_number** | **str** |  | [optional] 
**tax_options** | **str** | nStb &#x3D; Nicht steuerbar (Drittland), nStbUstID &#x3D; Nicht steuerbar (EU mit USt-IdNr.), nStbNoneUstID &#x3D; Nicht steuerbar (EU ohne USt-IdNr.), revc &#x3D; Steuerschuldwechsel §13b (Inland), IG &#x3D; Innergemeinschaftliche Lieferung, AL &#x3D; Ausfuhrlieferung, sStfr &#x3D; sonstige Steuerbefreiung, NULL &#x3D; Umsatzsteuerpflichtig | [optional] 
**title** | **str** |  | [optional] 
**vat_identifier** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


