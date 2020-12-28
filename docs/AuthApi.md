# swagger_client.AuthApi

All URIs are relative to *https://ebanq-api-sb.testsite.icu/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receiving_token**](AuthApi.md#receiving_token) | **POST** /auth/login | Receiving token
[**refresh_token**](AuthApi.md#refresh_token) | **POST** /auth/refresh | Refresh token

# **receiving_token**
> AuthResponce receiving_token(body=body)

Receiving token

Receiving token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = NULL # object |  (optional)

try:
    # Receiving token
    api_response = api_instance.receiving_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->receiving_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**AuthResponce**](AuthResponce.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> AuthResponce refresh_token(body=body)

Refresh token

Refresh token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
body = NULL # object |  (optional)

try:
    # Refresh token
    api_response = api_instance.refresh_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**AuthResponce**](AuthResponce.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

