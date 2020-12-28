# swagger_client.TerminalsApi

All URIs are relative to *https://ebanq-api-sb.testsite.icu/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_dispenser_levels**](TerminalsApi.md#change_dispenser_levels) | **POST** /terminals/collection | Change cash levels
[**get_dispenser_levels_info**](TerminalsApi.md#get_dispenser_levels_info) | **GET** /terminals/collection | Info about levels
[**operation_acceptor**](TerminalsApi.md#operation_acceptor) | **POST** /terminals/accepter | Operation about accepter
[**operation_d_get_settings**](TerminalsApi.md#operation_d_get_settings) | **POST** /terminals/settings | Get settings for the terminal. If a new terminal is added to the list of new terminals

# **change_dispenser_levels**
> CreatedResponce change_dispenser_levels(body=body)

Change cash levels

Change cash levels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TerminalsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Change cash levels
    api_response = api_instance.change_dispenser_levels(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalsApi->change_dispenser_levels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**CreatedResponce**](CreatedResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dispenser_levels_info**
> CollectionResponce get_dispenser_levels_info()

Info about levels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TerminalsApi(swagger_client.ApiClient(configuration))

try:
    # Info about levels
    api_response = api_instance.get_dispenser_levels_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalsApi->get_dispenser_levels_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollectionResponce**](CollectionResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operation_acceptor**
> AccepterResponce operation_acceptor(body=body)

Operation about accepter

Operation about accepter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TerminalsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Operation about accepter
    api_response = api_instance.operation_acceptor(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalsApi->operation_acceptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**AccepterResponce**](AccepterResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operation_d_get_settings**
> SettingsResponce operation_d_get_settings(body=body)

Get settings for the terminal. If a new terminal is added to the list of new terminals

Get settings for the terminal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TerminalsApi()
body = NULL # object |  (optional)

try:
    # Get settings for the terminal. If a new terminal is added to the list of new terminals
    api_response = api_instance.operation_d_get_settings(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TerminalsApi->operation_d_get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**SettingsResponce**](SettingsResponce.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

