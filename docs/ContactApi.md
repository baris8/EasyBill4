# openapi_client.ContactApi

All URIs are relative to *https://api.easybill.de/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_customer_id_contacts_get**](ContactApi.md#customers_customer_id_contacts_get) | **GET** /customers/{customerId}/contacts | Fetch customer contact list
[**customers_customer_id_contacts_id_delete**](ContactApi.md#customers_customer_id_contacts_id_delete) | **DELETE** /customers/{customerId}/contacts/{id} | Delete contact
[**customers_customer_id_contacts_id_get**](ContactApi.md#customers_customer_id_contacts_id_get) | **GET** /customers/{customerId}/contacts/{id} | Fetch contact
[**customers_customer_id_contacts_id_put**](ContactApi.md#customers_customer_id_contacts_id_put) | **PUT** /customers/{customerId}/contacts/{id} | Update Contact
[**customers_customer_id_contacts_post**](ContactApi.md#customers_customer_id_contacts_post) | **POST** /customers/{customerId}/contacts | Create new contact


# **customers_customer_id_contacts_get**
> Contacts customers_customer_id_contacts_get(customer_id, limit=limit, page=page)

Fetch customer contact list

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
    api_instance = openapi_client.ContactApi(api_client)
    customer_id = 56 # int | ID of customer that needs to be fetched
limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)

    try:
        # Fetch customer contact list
        api_response = api_instance.customers_customer_id_contacts_get(customer_id, limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactApi->customers_customer_id_contacts_get: %s\n" % e)
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
    api_instance = openapi_client.ContactApi(api_client)
    customer_id = 56 # int | ID of customer that needs to be fetched
limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)

    try:
        # Fetch customer contact list
        api_response = api_instance.customers_customer_id_contacts_get(customer_id, limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactApi->customers_customer_id_contacts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of customer that needs to be fetched | 
 **limit** | **int**| Limited the result. Default is 100. Maximum can be 1000. | [optional] 
 **page** | **int**| Set current Page. Default is 1. | [optional] 

### Return type

[**Contacts**](Contacts.md)

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

# **customers_customer_id_contacts_id_delete**
> customers_customer_id_contacts_id_delete(customer_id, id)

Delete contact

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
    api_instance = openapi_client.ContactApi(api_client)
    customer_id = 56 # int | ID of customer
id = 56 # int | ID of contact

    try:
        # Delete contact
        api_instance.customers_customer_id_contacts_id_delete(customer_id, id)
    except ApiException as e:
        print("Exception when calling ContactApi->customers_customer_id_contacts_id_delete: %s\n" % e)
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
    api_instance = openapi_client.ContactApi(api_client)
    customer_id = 56 # int | ID of customer
id = 56 # int | ID of contact

    try:
        # Delete contact
        api_instance.customers_customer_id_contacts_id_delete(customer_id, id)
    except ApiException as e:
        print("Exception when calling ContactApi->customers_customer_id_contacts_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of customer | 
 **id** | **int**| ID of contact | 

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

# **customers_customer_id_contacts_id_get**
> Contact customers_customer_id_contacts_id_get(customer_id, id)

Fetch contact

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
    api_instance = openapi_client.ContactApi(api_client)
    customer_id = 56 # int | ID of customer
id = 56 # int | ID of contact

    try:
        # Fetch contact
        api_response = api_instance.customers_customer_id_contacts_id_get(customer_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactApi->customers_customer_id_contacts_id_get: %s\n" % e)
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
    api_instance = openapi_client.ContactApi(api_client)
    customer_id = 56 # int | ID of customer
id = 56 # int | ID of contact

    try:
        # Fetch contact
        api_response = api_instance.customers_customer_id_contacts_id_get(customer_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactApi->customers_customer_id_contacts_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of customer | 
 **id** | **int**| ID of contact | 

### Return type

[**Contact**](Contact.md)

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

# **customers_customer_id_contacts_id_put**
> Contact customers_customer_id_contacts_id_put(customer_id, id, body=body)

Update Contact

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
    api_instance = openapi_client.ContactApi(api_client)
    customer_id = 56 # int | ID of customer
id = 56 # int | ID of contact
body = openapi_client.Contact() # Contact |  (optional)

    try:
        # Update Contact
        api_response = api_instance.customers_customer_id_contacts_id_put(customer_id, id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactApi->customers_customer_id_contacts_id_put: %s\n" % e)
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
    api_instance = openapi_client.ContactApi(api_client)
    customer_id = 56 # int | ID of customer
id = 56 # int | ID of contact
body = openapi_client.Contact() # Contact |  (optional)

    try:
        # Update Contact
        api_response = api_instance.customers_customer_id_contacts_id_put(customer_id, id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactApi->customers_customer_id_contacts_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of customer | 
 **id** | **int**| ID of contact | 
 **body** | [**Contact**](Contact.md)|  | [optional] 

### Return type

[**Contact**](Contact.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid contact |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_customer_id_contacts_post**
> Contact customers_customer_id_contacts_post(customer_id, body=body)

Create new contact

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
    api_instance = openapi_client.ContactApi(api_client)
    customer_id = 56 # int | ID of customer
body = openapi_client.Contact() # Contact |  (optional)

    try:
        # Create new contact
        api_response = api_instance.customers_customer_id_contacts_post(customer_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactApi->customers_customer_id_contacts_post: %s\n" % e)
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
    api_instance = openapi_client.ContactApi(api_client)
    customer_id = 56 # int | ID of customer
body = openapi_client.Contact() # Contact |  (optional)

    try:
        # Create new contact
        api_response = api_instance.customers_customer_id_contacts_post(customer_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactApi->customers_customer_id_contacts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of customer | 
 **body** | [**Contact**](Contact.md)|  | [optional] 

### Return type

[**Contact**](Contact.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid contact |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

