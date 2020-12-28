# swagger_client.AccountsApi

All URIs are relative to *https://ebanq-api-sb.testsite.icu/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account**](AccountsApi.md#create_account) | **POST** /accounts | Create account
[**credit_account**](AccountsApi.md#credit_account) | **POST** /accounts/credit | Credit request.
[**credit_review_account**](AccountsApi.md#credit_review_account) | **POST** /accounts/credit/review | Evaluates credit request.
[**debit_account**](AccountsApi.md#debit_account) | **POST** /accounts/debit | Debit request.
[**debit_review_account**](AccountsApi.md#debit_review_account) | **POST** /accounts/debit/review | Evaluates debit request.
[**get_account**](AccountsApi.md#get_account) | **GET** /accounts/info/{accountName} | Get account&#x60;s info
[**get_list_accounts**](AccountsApi.md#get_list_accounts) | **GET** /accounts/list/{UserId} | Get accounts list
[**transfer_account**](AccountsApi.md#transfer_account) | **POST** /accounts/transfer/accounts | Create transfer request.

# **create_account**
> AccountResponce create_account(body=body)

Create account

Create account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Create account
    api_response = api_instance.create_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**AccountResponce**](AccountResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_account**
> CreditResponce credit_account(body=body)

Credit request.

Credit request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Credit request.
    api_response = api_instance.credit_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->credit_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**CreditResponce**](CreditResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_review_account**
> CreditReviewResponce credit_review_account(body=body)

Evaluates credit request.

Evaluates credit request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Evaluates credit request.
    api_response = api_instance.credit_review_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->credit_review_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**CreditReviewResponce**](CreditReviewResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debit_account**
> DebitResponce debit_account(body=body)

Debit request.

Debit request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Debit request.
    api_response = api_instance.debit_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->debit_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**DebitResponce**](DebitResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **debit_review_account**
> DebitReviewResponce debit_review_account(body=body)

Evaluates debit request.

Evaluates debit request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Evaluates debit request.
    api_response = api_instance.debit_review_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->debit_review_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**DebitReviewResponce**](DebitReviewResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> AccountResponce get_account(account_name)

Get account`s info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
account_name = 'account_name_example' # str | The name of account

try:
    # Get account`s info
    api_response = api_instance.get_account(account_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_name** | **str**| The name of account | 

### Return type

[**AccountResponce**](AccountResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_accounts**
> InlineResponse200 get_list_accounts(user_id)

Get accounts list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | The id users

try:
    # Get accounts list
    api_response = api_instance.get_list_accounts(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->get_list_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The id users | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_account**
> TransferResponce transfer_account(body=body)

Create transfer request.

Create transfer request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Create transfer request.
    api_response = api_instance.transfer_account(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->transfer_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**TransferResponce**](TransferResponce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

