# swagger_client.SessionsApi

All URIs are relative to *https://ebanq-api-sb.testsite.icu/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_operation**](SessionsApi.md#close_operation) | **GET** /sessions/{session_id}/close | Close session
[**create_operation**](SessionsApi.md#create_operation) | **POST** /sessions | Create session.

# **close_operation**
> CreatedResponce close_operation(session_id)

Close session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SessionsApi(swagger_client.ApiClient(configuration))
session_id = 'session_id_example' # str | id active session

try:
    # Close session
    api_response = api_instance.close_operation(session_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->close_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| id active session | 

### Return type

[**CreatedResponce**](CreatedResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_operation**
> OperationCreateResponce create_operation(body=body)

Create session.

Create session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SessionsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Create session.
    api_response = api_instance.create_operation(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionsApi->create_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**OperationCreateResponce**](OperationCreateResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

