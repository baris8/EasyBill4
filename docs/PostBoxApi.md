# openapi_client.PostBoxApi

All URIs are relative to *https://api.easybill.de/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_boxes_get**](PostBoxApi.md#post_boxes_get) | **GET** /post-boxes | Fetch post box list
[**post_boxes_id_delete**](PostBoxApi.md#post_boxes_id_delete) | **DELETE** /post-boxes/{id} | Delete post box
[**post_boxes_id_get**](PostBoxApi.md#post_boxes_id_get) | **GET** /post-boxes/{id} | Fetch post box


# **post_boxes_get**
> PostBoxes post_boxes_get(limit=limit, page=page, type=type, status=status, document_id=document_id)

Fetch post box list

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
    api_instance = openapi_client.PostBoxApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)
type = 'type_example' # str | Filter post boxes by type. Multiple typs seperate with , like type=EMAIL,FAX. (optional)
status = 'status_example' # str | Filter post boxes by status. (optional)
document_id = 'document_id_example' # str | Filter post boxes by document_id. You can add multiple document ids separate by comma like id,id,id. (optional)

    try:
        # Fetch post box list
        api_response = api_instance.post_boxes_get(limit=limit, page=page, type=type, status=status, document_id=document_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PostBoxApi->post_boxes_get: %s\n" % e)
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
    api_instance = openapi_client.PostBoxApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)
type = 'type_example' # str | Filter post boxes by type. Multiple typs seperate with , like type=EMAIL,FAX. (optional)
status = 'status_example' # str | Filter post boxes by status. (optional)
document_id = 'document_id_example' # str | Filter post boxes by document_id. You can add multiple document ids separate by comma like id,id,id. (optional)

    try:
        # Fetch post box list
        api_response = api_instance.post_boxes_get(limit=limit, page=page, type=type, status=status, document_id=document_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PostBoxApi->post_boxes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limited the result. Default is 100. Maximum can be 1000. | [optional] 
 **page** | **int**| Set current Page. Default is 1. | [optional] 
 **type** | **str**| Filter post boxes by type. Multiple typs seperate with , like type&#x3D;EMAIL,FAX. | [optional] 
 **status** | **str**| Filter post boxes by status. | [optional] 
 **document_id** | **str**| Filter post boxes by document_id. You can add multiple document ids separate by comma like id,id,id. | [optional] 

### Return type

[**PostBoxes**](PostBoxes.md)

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

# **post_boxes_id_delete**
> post_boxes_id_delete(id)

Delete post box

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
    api_instance = openapi_client.PostBoxApi(api_client)
    id = 56 # int | ID of post box

    try:
        # Delete post box
        api_instance.post_boxes_id_delete(id)
    except ApiException as e:
        print("Exception when calling PostBoxApi->post_boxes_id_delete: %s\n" % e)
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
    api_instance = openapi_client.PostBoxApi(api_client)
    id = 56 # int | ID of post box

    try:
        # Delete post box
        api_instance.post_boxes_id_delete(id)
    except ApiException as e:
        print("Exception when calling PostBoxApi->post_boxes_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of post box | 

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

# **post_boxes_id_get**
> PostBox post_boxes_id_get(id)

Fetch post box

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
    api_instance = openapi_client.PostBoxApi(api_client)
    id = 56 # int | ID of post box

    try:
        # Fetch post box
        api_response = api_instance.post_boxes_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PostBoxApi->post_boxes_id_get: %s\n" % e)
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
    api_instance = openapi_client.PostBoxApi(api_client)
    id = 56 # int | ID of post box

    try:
        # Fetch post box
        api_response = api_instance.post_boxes_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PostBoxApi->post_boxes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of post box | 

### Return type

[**PostBox**](PostBox.md)

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

