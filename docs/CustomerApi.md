# openapi_client.CustomerApi

All URIs are relative to *https://api.easybill.de/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_get**](CustomerApi.md#customers_get) | **GET** /customers | Fetch customers list
[**customers_id_delete**](CustomerApi.md#customers_id_delete) | **DELETE** /customers/{id} | Delete customer
[**customers_id_get**](CustomerApi.md#customers_id_get) | **GET** /customers/{id} | Fetch customer
[**customers_id_put**](CustomerApi.md#customers_id_put) | **PUT** /customers/{id} | Update Customer
[**customers_post**](CustomerApi.md#customers_post) | **POST** /customers | Create customer


# **customers_get**
> Customers customers_get(limit=limit, page=page, group_id=group_id, additional_group_id=additional_group_id, number=number, country=country, zip_code=zip_code, emails=emails, first_name=first_name, last_name=last_name, company_name=company_name, created_at=created_at)

Fetch customers list

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
    api_instance = openapi_client.CustomerApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)
group_id = 'group_id_example' # str | Filter customers by group_id. You can add multiple group ids separate by comma like id,id,id. (optional)
additional_group_id = 'additional_group_id_example' # str | Filter customers by additional_group_id. You can add multiple group ids separate by comma like id,id,id. (optional)
number = 'number_example' # str | Filter customers by number. You can add multiple numbers separate by comma like no,no,no. (optional)
country = 'country_example' # str | Filter customers by country. You can add multiple countries separate by comma like DE,PL,FR. (optional)
zip_code = 'zip_code_example' # str | Filter customers by zip_code. You can add multiple zip codes separate by comma like zip,zip,zip. (optional)
emails = 'emails_example' # str | Filter customers by emails. You can add multiple emails separate by comma like mail,mail,mail. (optional)
first_name = 'first_name_example' # str | Filter customers by first_name. You can add multiple names separate by comma like name,name,name. (optional)
last_name = 'last_name_example' # str | Filter customers by first_name. You can add multiple names separate by comma like name,name,name. (optional)
company_name = 'company_name_example' # str | Filter customers by first_name. You can add multiple names separate by comma like name,name,name. (optional)
created_at = 'created_at_example' # str | Filter customers by created_at. You can filter one date with created_at=2014-12-10 or between like 2015-01-01,2015-12-31. (optional)

    try:
        # Fetch customers list
        api_response = api_instance.customers_get(limit=limit, page=page, group_id=group_id, additional_group_id=additional_group_id, number=number, country=country, zip_code=zip_code, emails=emails, first_name=first_name, last_name=last_name, company_name=company_name, created_at=created_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomerApi->customers_get: %s\n" % e)
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
    api_instance = openapi_client.CustomerApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)
group_id = 'group_id_example' # str | Filter customers by group_id. You can add multiple group ids separate by comma like id,id,id. (optional)
additional_group_id = 'additional_group_id_example' # str | Filter customers by additional_group_id. You can add multiple group ids separate by comma like id,id,id. (optional)
number = 'number_example' # str | Filter customers by number. You can add multiple numbers separate by comma like no,no,no. (optional)
country = 'country_example' # str | Filter customers by country. You can add multiple countries separate by comma like DE,PL,FR. (optional)
zip_code = 'zip_code_example' # str | Filter customers by zip_code. You can add multiple zip codes separate by comma like zip,zip,zip. (optional)
emails = 'emails_example' # str | Filter customers by emails. You can add multiple emails separate by comma like mail,mail,mail. (optional)
first_name = 'first_name_example' # str | Filter customers by first_name. You can add multiple names separate by comma like name,name,name. (optional)
last_name = 'last_name_example' # str | Filter customers by first_name. You can add multiple names separate by comma like name,name,name. (optional)
company_name = 'company_name_example' # str | Filter customers by first_name. You can add multiple names separate by comma like name,name,name. (optional)
created_at = 'created_at_example' # str | Filter customers by created_at. You can filter one date with created_at=2014-12-10 or between like 2015-01-01,2015-12-31. (optional)

    try:
        # Fetch customers list
        api_response = api_instance.customers_get(limit=limit, page=page, group_id=group_id, additional_group_id=additional_group_id, number=number, country=country, zip_code=zip_code, emails=emails, first_name=first_name, last_name=last_name, company_name=company_name, created_at=created_at)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomerApi->customers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limited the result. Default is 100. Maximum can be 1000. | [optional] 
 **page** | **int**| Set current Page. Default is 1. | [optional] 
 **group_id** | **str**| Filter customers by group_id. You can add multiple group ids separate by comma like id,id,id. | [optional] 
 **additional_group_id** | **str**| Filter customers by additional_group_id. You can add multiple group ids separate by comma like id,id,id. | [optional] 
 **number** | **str**| Filter customers by number. You can add multiple numbers separate by comma like no,no,no. | [optional] 
 **country** | **str**| Filter customers by country. You can add multiple countries separate by comma like DE,PL,FR. | [optional] 
 **zip_code** | **str**| Filter customers by zip_code. You can add multiple zip codes separate by comma like zip,zip,zip. | [optional] 
 **emails** | **str**| Filter customers by emails. You can add multiple emails separate by comma like mail,mail,mail. | [optional] 
 **first_name** | **str**| Filter customers by first_name. You can add multiple names separate by comma like name,name,name. | [optional] 
 **last_name** | **str**| Filter customers by first_name. You can add multiple names separate by comma like name,name,name. | [optional] 
 **company_name** | **str**| Filter customers by first_name. You can add multiple names separate by comma like name,name,name. | [optional] 
 **created_at** | **str**| Filter customers by created_at. You can filter one date with created_at&#x3D;2014-12-10 or between like 2015-01-01,2015-12-31. | [optional] 

### Return type

[**Customers**](Customers.md)

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

# **customers_id_delete**
> customers_id_delete(id)

Delete customer

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
    api_instance = openapi_client.CustomerApi(api_client)
    id = 56 # int | ID of customer that needs to be deleted

    try:
        # Delete customer
        api_instance.customers_id_delete(id)
    except ApiException as e:
        print("Exception when calling CustomerApi->customers_id_delete: %s\n" % e)
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
    api_instance = openapi_client.CustomerApi(api_client)
    id = 56 # int | ID of customer that needs to be deleted

    try:
        # Delete customer
        api_instance.customers_id_delete(id)
    except ApiException as e:
        print("Exception when calling CustomerApi->customers_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of customer that needs to be deleted | 

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

# **customers_id_get**
> Customer customers_id_get(id)

Fetch customer

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
    api_instance = openapi_client.CustomerApi(api_client)
    id = 56 # int | ID of customer that needs to be fetched

    try:
        # Fetch customer
        api_response = api_instance.customers_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomerApi->customers_id_get: %s\n" % e)
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
    api_instance = openapi_client.CustomerApi(api_client)
    id = 56 # int | ID of customer that needs to be fetched

    try:
        # Fetch customer
        api_response = api_instance.customers_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomerApi->customers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of customer that needs to be fetched | 

### Return type

[**Customer**](Customer.md)

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

# **customers_id_put**
> Customer customers_id_put(id, body)

Update Customer

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
    api_instance = openapi_client.CustomerApi(api_client)
    id = 56 # int | ID of customer that needs to be updated
body = openapi_client.Customer() # Customer | 

    try:
        # Update Customer
        api_response = api_instance.customers_id_put(id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomerApi->customers_id_put: %s\n" % e)
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
    api_instance = openapi_client.CustomerApi(api_client)
    id = 56 # int | ID of customer that needs to be updated
body = openapi_client.Customer() # Customer | 

    try:
        # Update Customer
        api_response = api_instance.customers_id_put(id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomerApi->customers_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of customer that needs to be updated | 
 **body** | [**Customer**](Customer.md)|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid Customer |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_post**
> Customer customers_post(body)

Create customer

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
    api_instance = openapi_client.CustomerApi(api_client)
    body = openapi_client.Customer() # Customer | 

    try:
        # Create customer
        api_response = api_instance.customers_post(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomerApi->customers_post: %s\n" % e)
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
    api_instance = openapi_client.CustomerApi(api_client)
    body = openapi_client.Customer() # Customer | 

    try:
        # Create customer
        api_response = api_instance.customers_post(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CustomerApi->customers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Customer**](Customer.md)|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Invalid Customer |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

