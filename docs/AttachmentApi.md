# openapi_client.AttachmentApi

All URIs are relative to *https://api.easybill.de/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachments_get**](AttachmentApi.md#attachments_get) | **GET** /attachments | Fetch attachments list
[**attachments_id_content_get**](AttachmentApi.md#attachments_id_content_get) | **GET** /attachments/{id}/content | Fetch attachment content
[**attachments_id_delete**](AttachmentApi.md#attachments_id_delete) | **DELETE** /attachments/{id} | Delete attachment
[**attachments_id_get**](AttachmentApi.md#attachments_id_get) | **GET** /attachments/{id} | Fetch attachment
[**attachments_id_put**](AttachmentApi.md#attachments_id_put) | **PUT** /attachments/{id} | Update attachment
[**attachments_post**](AttachmentApi.md#attachments_post) | **POST** /attachments | Create attachment


# **attachments_get**
> Attachments attachments_get(limit=limit, page=page)

Fetch attachments list

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
    api_instance = openapi_client.AttachmentApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)

    try:
        # Fetch attachments list
        api_response = api_instance.attachments_get(limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_get: %s\n" % e)
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
    api_instance = openapi_client.AttachmentApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)

    try:
        # Fetch attachments list
        api_response = api_instance.attachments_get(limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limited the result. Default is 100. Maximum can be 1000. | [optional] 
 **page** | **int**| Set current Page. Default is 1. | [optional] 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachments_id_content_get**
> file attachments_id_content_get(id)

Fetch attachment content

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
    api_instance = openapi_client.AttachmentApi(api_client)
    id = 56 # int | ID of attachment

    try:
        # Fetch attachment content
        api_response = api_instance.attachments_id_content_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_id_content_get: %s\n" % e)
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
    api_instance = openapi_client.AttachmentApi(api_client)
    id = 56 # int | ID of attachment

    try:
        # Fetch attachment content
        api_response = api_instance.attachments_id_content_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_id_content_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of attachment | 

### Return type

**file**

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

# **attachments_id_delete**
> attachments_id_delete(id)

Delete attachment

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
    api_instance = openapi_client.AttachmentApi(api_client)
    id = 56 # int | ID of attachment

    try:
        # Delete attachment
        api_instance.attachments_id_delete(id)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_id_delete: %s\n" % e)
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
    api_instance = openapi_client.AttachmentApi(api_client)
    id = 56 # int | ID of attachment

    try:
        # Delete attachment
        api_instance.attachments_id_delete(id)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of attachment | 

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

# **attachments_id_get**
> Attachment attachments_id_get(id)

Fetch attachment

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
    api_instance = openapi_client.AttachmentApi(api_client)
    id = 56 # int | ID of attachment

    try:
        # Fetch attachment
        api_response = api_instance.attachments_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_id_get: %s\n" % e)
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
    api_instance = openapi_client.AttachmentApi(api_client)
    id = 56 # int | ID of attachment

    try:
        # Fetch attachment
        api_response = api_instance.attachments_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of attachment | 

### Return type

[**Attachment**](Attachment.md)

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

# **attachments_id_put**
> Attachment attachments_id_put(id, body)

Update attachment

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
    api_instance = openapi_client.AttachmentApi(api_client)
    id = 56 # int | ID of attachment
body = openapi_client.Attachment() # Attachment | 

    try:
        # Update attachment
        api_response = api_instance.attachments_id_put(id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_id_put: %s\n" % e)
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
    api_instance = openapi_client.AttachmentApi(api_client)
    id = 56 # int | ID of attachment
body = openapi_client.Attachment() # Attachment | 

    try:
        # Update attachment
        api_response = api_instance.attachments_id_put(id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of attachment | 
 **body** | [**Attachment**](Attachment.md)|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid attachment |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachments_post**
> Attachment attachments_post(file)

Create attachment

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
    api_instance = openapi_client.AttachmentApi(api_client)
    file = '/path/to/file' # file | 

    try:
        # Create attachment
        api_response = api_instance.attachments_post(file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_post: %s\n" % e)
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
    api_instance = openapi_client.AttachmentApi(api_client)
    file = '/path/to/file' # file | 

    try:
        # Create attachment
        api_response = api_instance.attachments_post(file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AttachmentApi->attachments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**|  | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

