# openapi_client.DocumentApi

All URIs are relative to *https://api.easybill.de/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_get**](DocumentApi.md#documents_get) | **GET** /documents | Fetch documents list
[**documents_id_cancel_post**](DocumentApi.md#documents_id_cancel_post) | **POST** /documents/{id}/cancel | Cancel document
[**documents_id_delete**](DocumentApi.md#documents_id_delete) | **DELETE** /documents/{id} | Delete document
[**documents_id_done_put**](DocumentApi.md#documents_id_done_put) | **PUT** /documents/{id}/done | To complete a document.
[**documents_id_get**](DocumentApi.md#documents_id_get) | **GET** /documents/{id} | Fetch document
[**documents_id_pdf_get**](DocumentApi.md#documents_id_pdf_get) | **GET** /documents/{id}/pdf | Fetch pdf document
[**documents_id_put**](DocumentApi.md#documents_id_put) | **PUT** /documents/{id} | Update document
[**documents_id_send_type_post**](DocumentApi.md#documents_id_send_type_post) | **POST** /documents/{id}/send/{type} | Send document
[**documents_post**](DocumentApi.md#documents_post) | **POST** /documents | Create document


# **documents_get**
> Documents documents_get(limit=limit, page=page, type=type, is_draft=is_draft, is_archive=is_archive, customer_id=customer_id, project_id=project_id, document_date=document_date, paid_at=paid_at, title=title, number=number, cancel_id=cancel_id, fulfillment_country=fulfillment_country, vat_country=vat_country, shipping_country=shipping_country, status=status)

Fetch documents list

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
    api_instance = openapi_client.DocumentApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)
type = 'type_example' # str | Filter documents by type. Multiple typs seperate with , like type=INVOICE,CREDIT. (optional)
is_draft = 'is_draft_example' # str | Filter documents by draft flag. (optional)
is_archive = 'is_archive_example' # str | Filter documents by archive flag. (optional)
customer_id = 'customer_id_example' # str | Filter documents by customer_id. You can add multiple customer_is separate by comma like id,id,id. (optional)
project_id = 'project_id_example' # str | Filter documents by project_id. You can add multiple project_id separate by comma like id,id,id. (optional)
document_date = 'document_date_example' # str | Filter documents by document_date. You can filter one date with document_date=2014-12-10 or between like 2015-01-01,2015-12-31. (optional)
paid_at = 'paid_at_example' # str | Filter documents by paid_at. You can filter one date with paid_at=2014-12-10 or between like 2015-01-01,2015-12-31. With paid_at=null you get all unpaid documents. (optional)
title = 'title_example' # str | Filter documents by title. (optional)
number = 'number_example' # str | Filter documents by number. (optional)
cancel_id = 'cancel_id_example' # str | Filter documents by cancel_id. You can add multiple ids separate by comma like id,id,id. With cancel_id=null you get all not canceled documents. (optional)
fulfillment_country = 'fulfillment_country_example' # str | Filter documents by fulfillment_country. (optional)
vat_country = 'vat_country_example' # str | Filter documents by vat_country. (optional)
shipping_country = 'shipping_country_example' # str | Filter documents by shipping_country. (optional)
status = 'status_example' # str | Filter documents by status. Keep in mind that not every document type has a status. (optional)

    try:
        # Fetch documents list
        api_response = api_instance.documents_get(limit=limit, page=page, type=type, is_draft=is_draft, is_archive=is_archive, customer_id=customer_id, project_id=project_id, document_date=document_date, paid_at=paid_at, title=title, number=number, cancel_id=cancel_id, fulfillment_country=fulfillment_country, vat_country=vat_country, shipping_country=shipping_country, status=status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_get: %s\n" % e)
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
    api_instance = openapi_client.DocumentApi(api_client)
    limit = 56 # int | Limited the result. Default is 100. Maximum can be 1000. (optional)
page = 56 # int | Set current Page. Default is 1. (optional)
type = 'type_example' # str | Filter documents by type. Multiple typs seperate with , like type=INVOICE,CREDIT. (optional)
is_draft = 'is_draft_example' # str | Filter documents by draft flag. (optional)
is_archive = 'is_archive_example' # str | Filter documents by archive flag. (optional)
customer_id = 'customer_id_example' # str | Filter documents by customer_id. You can add multiple customer_is separate by comma like id,id,id. (optional)
project_id = 'project_id_example' # str | Filter documents by project_id. You can add multiple project_id separate by comma like id,id,id. (optional)
document_date = 'document_date_example' # str | Filter documents by document_date. You can filter one date with document_date=2014-12-10 or between like 2015-01-01,2015-12-31. (optional)
paid_at = 'paid_at_example' # str | Filter documents by paid_at. You can filter one date with paid_at=2014-12-10 or between like 2015-01-01,2015-12-31. With paid_at=null you get all unpaid documents. (optional)
title = 'title_example' # str | Filter documents by title. (optional)
number = 'number_example' # str | Filter documents by number. (optional)
cancel_id = 'cancel_id_example' # str | Filter documents by cancel_id. You can add multiple ids separate by comma like id,id,id. With cancel_id=null you get all not canceled documents. (optional)
fulfillment_country = 'fulfillment_country_example' # str | Filter documents by fulfillment_country. (optional)
vat_country = 'vat_country_example' # str | Filter documents by vat_country. (optional)
shipping_country = 'shipping_country_example' # str | Filter documents by shipping_country. (optional)
status = 'status_example' # str | Filter documents by status. Keep in mind that not every document type has a status. (optional)

    try:
        # Fetch documents list
        api_response = api_instance.documents_get(limit=limit, page=page, type=type, is_draft=is_draft, is_archive=is_archive, customer_id=customer_id, project_id=project_id, document_date=document_date, paid_at=paid_at, title=title, number=number, cancel_id=cancel_id, fulfillment_country=fulfillment_country, vat_country=vat_country, shipping_country=shipping_country, status=status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limited the result. Default is 100. Maximum can be 1000. | [optional] 
 **page** | **int**| Set current Page. Default is 1. | [optional] 
 **type** | **str**| Filter documents by type. Multiple typs seperate with , like type&#x3D;INVOICE,CREDIT. | [optional] 
 **is_draft** | **str**| Filter documents by draft flag. | [optional] 
 **is_archive** | **str**| Filter documents by archive flag. | [optional] 
 **customer_id** | **str**| Filter documents by customer_id. You can add multiple customer_is separate by comma like id,id,id. | [optional] 
 **project_id** | **str**| Filter documents by project_id. You can add multiple project_id separate by comma like id,id,id. | [optional] 
 **document_date** | **str**| Filter documents by document_date. You can filter one date with document_date&#x3D;2014-12-10 or between like 2015-01-01,2015-12-31. | [optional] 
 **paid_at** | **str**| Filter documents by paid_at. You can filter one date with paid_at&#x3D;2014-12-10 or between like 2015-01-01,2015-12-31. With paid_at&#x3D;null you get all unpaid documents. | [optional] 
 **title** | **str**| Filter documents by title. | [optional] 
 **number** | **str**| Filter documents by number. | [optional] 
 **cancel_id** | **str**| Filter documents by cancel_id. You can add multiple ids separate by comma like id,id,id. With cancel_id&#x3D;null you get all not canceled documents. | [optional] 
 **fulfillment_country** | **str**| Filter documents by fulfillment_country. | [optional] 
 **vat_country** | **str**| Filter documents by vat_country. | [optional] 
 **shipping_country** | **str**| Filter documents by shipping_country. | [optional] 
 **status** | **str**| Filter documents by status. Keep in mind that not every document type has a status. | [optional] 

### Return type

[**Documents**](Documents.md)

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

# **documents_id_cancel_post**
> Document documents_id_cancel_post(id)

Cancel document

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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document

    try:
        # Cancel document
        api_response = api_instance.documents_id_cancel_post(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_cancel_post: %s\n" % e)
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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document

    try:
        # Cancel document
        api_response = api_instance.documents_id_cancel_post(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of document | 

### Return type

[**Document**](Document.md)

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

# **documents_id_delete**
> documents_id_delete(id)

Delete document

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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document

    try:
        # Delete document
        api_instance.documents_id_delete(id)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_delete: %s\n" % e)
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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document

    try:
        # Delete document
        api_instance.documents_id_delete(id)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of document | 

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

# **documents_id_done_put**
> Document documents_id_done_put(id)

To complete a document.

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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document

    try:
        # To complete a document.
        api_response = api_instance.documents_id_done_put(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_done_put: %s\n" % e)
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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document

    try:
        # To complete a document.
        api_response = api_instance.documents_id_done_put(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_done_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of document | 

### Return type

[**Document**](Document.md)

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

# **documents_id_get**
> Document documents_id_get(id)

Fetch document

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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document

    try:
        # Fetch document
        api_response = api_instance.documents_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_get: %s\n" % e)
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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document

    try:
        # Fetch document
        api_response = api_instance.documents_id_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of document | 

### Return type

[**Document**](Document.md)

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

# **documents_id_pdf_get**
> file documents_id_pdf_get(id)

Fetch pdf document

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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document

    try:
        # Fetch pdf document
        api_response = api_instance.documents_id_pdf_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_pdf_get: %s\n" % e)
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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document

    try:
        # Fetch pdf document
        api_response = api_instance.documents_id_pdf_get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of document | 

### Return type

**file**

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_id_put**
> Document documents_id_put(id, body, refresh_customer_data=refresh_customer_data)

Update document

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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document
body = openapi_client.Document() # Document | 
refresh_customer_data = True # bool | Forces refreshing of the customer data. (optional)

    try:
        # Update document
        api_response = api_instance.documents_id_put(id, body, refresh_customer_data=refresh_customer_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_put: %s\n" % e)
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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document
body = openapi_client.Document() # Document | 
refresh_customer_data = True # bool | Forces refreshing of the customer data. (optional)

    try:
        # Update document
        api_response = api_instance.documents_id_put(id, body, refresh_customer_data=refresh_customer_data)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of document | 
 **body** | [**Document**](Document.md)|  | 
 **refresh_customer_data** | **bool**| Forces refreshing of the customer data. | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid Document |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_id_send_type_post**
> documents_id_send_type_post(id, type, body)

Send document

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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document
type = 'type_example' # str | 
body = openapi_client.PostBoxRequest() # PostBoxRequest | 

    try:
        # Send document
        api_instance.documents_id_send_type_post(id, type, body)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_send_type_post: %s\n" % e)
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
    api_instance = openapi_client.DocumentApi(api_client)
    id = 56 # int | ID of document
type = 'type_example' # str | 
body = openapi_client.PostBoxRequest() # PostBoxRequest | 

    try:
        # Send document
        api_instance.documents_id_send_type_post(id, type, body)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_id_send_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of document | 
 **type** | **str**|  | 
 **body** | [**PostBoxRequest**](PostBoxRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful operation |  -  |
**404** | Not found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_post**
> Document documents_post(body)

Create document

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
    api_instance = openapi_client.DocumentApi(api_client)
    body = openapi_client.Document() # Document | 

    try:
        # Create document
        api_response = api_instance.documents_post(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_post: %s\n" % e)
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
    api_instance = openapi_client.DocumentApi(api_client)
    body = openapi_client.Document() # Document | 

    try:
        # Create document
        api_response = api_instance.documents_post(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DocumentApi->documents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Document**](Document.md)|  | 

### Return type

[**Document**](Document.md)

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

