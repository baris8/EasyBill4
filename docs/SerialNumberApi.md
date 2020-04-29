# openapi_client.SerialNumberApi

All URIs are relative to *https://api.easybill.de/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serial_numbers_get**](SerialNumberApi.md#serial_numbers_get) | **GET** /serial-numbers | Fetch a list of serial numbers for positions
[**serial_numbers_id_delete**](SerialNumberApi.md#serial_numbers_id_delete) | **DELETE** /serial-numbers/{id} | Delete a serial number for a position
[**serial_numbers_id_get**](SerialNumberApi.md#serial_numbers_id_get) | **GET** /serial-numbers/{id} | Fetch a serial number for a position
[**serial_numbers_post**](SerialNumberApi.md#serial_numbers_post) | **POST** /serial-numbers | Create s serial number for a position


# **serial_numbers_get**
> SerialNumbers serial_numbers_get(limit=limit, page=page, position_id=position_id, document_id=document_id, in_use=in_use)

Fetch a list of serial numbers for positions

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
    api_instance = openapi_client.SerialNumberApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)
position_id = 'position_id_example' # str | Filter serial numbers by position id. (optional)
document_id = 'document_id_example' # str | Filter serial numbers by document id. (optional)
in_use = True # bool | Filter serial numbers by usage. (optional)

    try:
        # Fetch a list of serial numbers for positions
        api_response = api_instance.serial_numbers_get(limit=limit, page=page, position_id=position_id, document_id=document_id, in_use=in_use)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SerialNumberApi->serial_numbers_get: %s\n" % e)
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
    api_instance = openapi_client.SerialNumberApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)
position_id = 'position_id_example' # str | Filter serial numbers by position id. (optional)
document_id = 'document_id_example' # str | Filter serial numbers by document id. (optional)
in_use = True # bool | Filter serial numbers by usage. (optional)

    try:
        # Fetch a list of serial numbers for positions
        api_response = api_instance.serial_numbers_get(limit=limit, page=page, position_id=position_id, document_id=document_id, in_use=in_use)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SerialNumberApi->serial_numbers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limited the result. Default is 100. Maximum can be 1000. | [optional] 
 **page** | **int**| Set current Page. Default is 1. | [optional] 
 **position_id** | **str**| Filter serial numbers by position id. | [optional] 
 **document_id** | **str**| Filter serial numbers by document id. | [optional] 
 **in_use** | **bool**| Filter serial numbers by usage. | [optional] 

### Return type

[**SerialNumbers**](SerialNumbers.md)

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

# **serial_numbers_id_delete**
> serial_numbers_id_delete(id)

Delete a serial number for a position

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
    api_instance = openapi_client.SerialNumberApi(api_client)
    id = 56 # int | ID of the serial number that needs to be deleted

    try:
        # Delete a serial number for a position
        api_instance.serial_numbers_id_delete(id)
    except ApiException as e:
        print("Exception when calling SerialNumberApi->serial_numbers_id_delete: %s\n" % e)
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
    api_instance = openapi_client.SerialNumberApi(api_client)
    id = 56 # int | ID of the serial number that needs to be deleted

    try:
        # Delete a serial number for a position
        api_instance.serial_numbers_id_delete(id)
    except ApiException as e:
        print("Exception when calling SerialNumberApi->serial_numbers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the serial number that needs to be deleted | 

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
**400** | Serial number in use. Operation failed. |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **serial_numbers_id_get**
> SerialNumber serial_numbers_id_get(id)

Fetch a serial number for a position

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
    api_instance = openapi_client.SerialNumberApi(api_client)
    id = 56 # int | ID of the serial number that needs to be fetched

    try:
        # Fetch a serial number for a position
        api_response = api_instance.serial_numbers_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SerialNumberApi->serial_numbers_id_get: %s\n" % e)
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
    api_instance = openapi_client.SerialNumberApi(api_client)
    id = 56 # int | ID of the serial number that needs to be fetched

    try:
        # Fetch a serial number for a position
        api_response = api_instance.serial_numbers_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SerialNumberApi->serial_numbers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the serial number that needs to be fetched | 

### Return type

[**SerialNumber**](SerialNumber.md)

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

# **serial_numbers_post**
> SerialNumber serial_numbers_post(body=body)

Create s serial number for a position

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
    api_instance = openapi_client.SerialNumberApi(api_client)
    body = openapi_client.SerialNumber() # SerialNumber |  (optional)

    try:
        # Create s serial number for a position
        api_response = api_instance.serial_numbers_post(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SerialNumberApi->serial_numbers_post: %s\n" % e)
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
    api_instance = openapi_client.SerialNumberApi(api_client)
    body = openapi_client.SerialNumber() # SerialNumber |  (optional)

    try:
        # Create s serial number for a position
        api_response = api_instance.serial_numbers_post(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SerialNumberApi->serial_numbers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SerialNumber**](SerialNumber.md)|  | [optional] 

### Return type

[**SerialNumber**](SerialNumber.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid PositionID |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

