# openapi_client.TaskApi

All URIs are relative to *https://api.easybill.de/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_get**](TaskApi.md#tasks_get) | **GET** /tasks | Fetch tasks list
[**tasks_id_delete**](TaskApi.md#tasks_id_delete) | **DELETE** /tasks/{id} | Delete task
[**tasks_id_get**](TaskApi.md#tasks_id_get) | **GET** /tasks/{id} | Fetch task
[**tasks_id_put**](TaskApi.md#tasks_id_put) | **PUT** /tasks/{id} | Update task
[**tasks_post**](TaskApi.md#tasks_post) | **POST** /tasks | Create task


# **tasks_get**
> Tasks tasks_get(limit=limit, page=page)

Fetch tasks list

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
    api_instance = openapi_client.TaskApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)

    try:
        # Fetch tasks list
        api_response = api_instance.tasks_get(limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->tasks_get: %s\n" % e)
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
    api_instance = openapi_client.TaskApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)

    try:
        # Fetch tasks list
        api_response = api_instance.tasks_get(limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limited the result. Default is 100. Maximum can be 1000. | [optional] 
 **page** | **int**| Set current Page. Default is 1. | [optional] 

### Return type

[**Tasks**](Tasks.md)

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

# **tasks_id_delete**
> tasks_id_delete(id)

Delete task

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 56 # int | ID of task

    try:
        # Delete task
        api_instance.tasks_id_delete(id)
    except ApiException as e:
        print("Exception when calling TaskApi->tasks_id_delete: %s\n" % e)
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
    api_instance = openapi_client.TaskApi(api_client)
    id = 56 # int | ID of task

    try:
        # Delete task
        api_instance.tasks_id_delete(id)
    except ApiException as e:
        print("Exception when calling TaskApi->tasks_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of task | 

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

# **tasks_id_get**
> Task tasks_id_get(id)

Fetch task

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 56 # int | ID of task

    try:
        # Fetch task
        api_response = api_instance.tasks_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->tasks_id_get: %s\n" % e)
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
    api_instance = openapi_client.TaskApi(api_client)
    id = 56 # int | ID of task

    try:
        # Fetch task
        api_response = api_instance.tasks_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->tasks_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of task | 

### Return type

[**Task**](Task.md)

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

# **tasks_id_put**
> Task tasks_id_put(id, body)

Update task

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
    api_instance = openapi_client.TaskApi(api_client)
    id = 56 # int | ID of task
body = openapi_client.Task() # Task | 

    try:
        # Update task
        api_response = api_instance.tasks_id_put(id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->tasks_id_put: %s\n" % e)
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
    api_instance = openapi_client.TaskApi(api_client)
    id = 56 # int | ID of task
body = openapi_client.Task() # Task | 

    try:
        # Update task
        api_response = api_instance.tasks_id_put(id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->tasks_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of task | 
 **body** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid task |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_post**
> Task tasks_post(body)

Create task

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
    api_instance = openapi_client.TaskApi(api_client)
    body = openapi_client.Task() # Task | 

    try:
        # Create task
        api_response = api_instance.tasks_post(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->tasks_post: %s\n" % e)
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
    api_instance = openapi_client.TaskApi(api_client)
    body = openapi_client.Task() # Task | 

    try:
        # Create task
        api_response = api_instance.tasks_post(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskApi->tasks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

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

