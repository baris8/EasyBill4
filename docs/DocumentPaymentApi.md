# openapi_client.DocumentPaymentApi

All URIs are relative to *https://api.easybill.de/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_payments_get**](DocumentPaymentApi.md#document_payments_get) | **GET** /document-payments | Fetch document payments list
[**document_payments_id_delete**](DocumentPaymentApi.md#document_payments_id_delete) | **DELETE** /document-payments/{id} | Delete document payment
[**document_payments_id_get**](DocumentPaymentApi.md#document_payments_id_get) | **GET** /document-payments/{id} | Fetch document payment
[**document_payments_post**](DocumentPaymentApi.md#document_payments_post) | **POST** /document-payments | Create document payment


# **document_payments_get**
> DocumentPayments document_payments_get(limit=limit, page=page, document_id=document_id, payment_at=payment_at, reference=reference)

Fetch document payments list

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.easybill.de/rest/v1
configuration.host = "https://api.easybill.de/rest/v1"

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentPaymentApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)
document_id = 'document_id_example' # str | Filter payments by document_id. You can add multiple ids separate by comma like id,id,id. (optional)
payment_at = 'payment_at_example' # str | Filter payments by payment_at. You can filter one date with payment_at=2014-12-10 or between like 2015-01-01,2015-12-31. (optional)
reference = 'reference_example' # str | Filter payments by reference. You can add multiple references separate by comma like id,id,id. (optional)

    try:
        # Fetch document payments list
        api_response = api_instance.document_payments_get(limit=limit, page=page, document_id=document_id, payment_at=payment_at, reference=reference)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentPaymentApi->document_payments_get: %s\n" % e)
```

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.easybill.de/rest/v1
configuration.host = "https://api.easybill.de/rest/v1"

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentPaymentApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)
document_id = 'document_id_example' # str | Filter payments by document_id. You can add multiple ids separate by comma like id,id,id. (optional)
payment_at = 'payment_at_example' # str | Filter payments by payment_at. You can filter one date with payment_at=2014-12-10 or between like 2015-01-01,2015-12-31. (optional)
reference = 'reference_example' # str | Filter payments by reference. You can add multiple references separate by comma like id,id,id. (optional)

    try:
        # Fetch document payments list
        api_response = api_instance.document_payments_get(limit=limit, page=page, document_id=document_id, payment_at=payment_at, reference=reference)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentPaymentApi->document_payments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limited the result. Default is 100. Maximum can be 1000. | [optional] 
 **page** | **int**| Set current Page. Default is 1. | [optional] 
 **document_id** | **str**| Filter payments by document_id. You can add multiple ids separate by comma like id,id,id. | [optional] 
 **payment_at** | **str**| Filter payments by payment_at. You can filter one date with payment_at&#x3D;2014-12-10 or between like 2015-01-01,2015-12-31. | [optional] 
 **reference** | **str**| Filter payments by reference. You can add multiple references separate by comma like id,id,id. | [optional] 

### Return type

[**DocumentPayments**](DocumentPayments.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_payments_id_delete**
> document_payments_id_delete(id)

Delete document payment

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.easybill.de/rest/v1
configuration.host = "https://api.easybill.de/rest/v1"

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentPaymentApi(api_client)
    id = 56 # int | ID of document payment

    try:
        # Delete document payment
        api_instance.document_payments_id_delete(id)
    except ApiException as e:
        print("Exception when calling DocumentPaymentApi->document_payments_id_delete: %s\n" % e)
```

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.easybill.de/rest/v1
configuration.host = "https://api.easybill.de/rest/v1"

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentPaymentApi(api_client)
    id = 56 # int | ID of document payment

    try:
        # Delete document payment
        api_instance.document_payments_id_delete(id)
    except ApiException as e:
        print("Exception when calling DocumentPaymentApi->document_payments_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of document payment | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful operation |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_payments_id_get**
> DocumentPayment document_payments_id_get(id)

Fetch document payment

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.easybill.de/rest/v1
configuration.host = "https://api.easybill.de/rest/v1"

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentPaymentApi(api_client)
    id = 56 # int | ID of document payment

    try:
        # Fetch document payment
        api_response = api_instance.document_payments_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentPaymentApi->document_payments_id_get: %s\n" % e)
```

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.easybill.de/rest/v1
configuration.host = "https://api.easybill.de/rest/v1"

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentPaymentApi(api_client)
    id = 56 # int | ID of document payment

    try:
        # Fetch document payment
        api_response = api_instance.document_payments_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentPaymentApi->document_payments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of document payment | 

### Return type

[**DocumentPayment**](DocumentPayment.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_payments_post**
> DocumentPayment document_payments_post(body, paid=paid)

Create document payment

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.easybill.de/rest/v1
configuration.host = "https://api.easybill.de/rest/v1"

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentPaymentApi(api_client)
    body = openapi_client.DocumentPayment() # DocumentPayment | 
paid = True # bool | Mark document as paid when amount less then payment amount. (optional)

    try:
        # Create document payment
        api_response = api_instance.document_payments_post(body, paid=paid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentPaymentApi->document_payments_post: %s\n" % e)
```

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: Bearer
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
configuration = openapi_client.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.easybill.de/rest/v1
configuration.host = "https://api.easybill.de/rest/v1"

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentPaymentApi(api_client)
    body = openapi_client.DocumentPayment() # DocumentPayment | 
paid = True # bool | Mark document as paid when amount less then payment amount. (optional)

    try:
        # Create document payment
        api_response = api_instance.document_payments_post(body, paid=paid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentPaymentApi->document_payments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentPayment**](DocumentPayment.md)|  | 
 **paid** | **bool**| Mark document as paid when amount less then payment amount. | [optional] 

### Return type

[**DocumentPayment**](DocumentPayment.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

