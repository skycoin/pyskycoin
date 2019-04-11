# skyhwd.DefaultApi

All URIs are relative to *http://127.0.0.1:9510/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_settings_post**](DefaultApi.md#apply_settings_post) | **POST** /apply_settings | 
[**backup_post**](DefaultApi.md#backup_post) | **POST** /backup | 
[**cancel_put**](DefaultApi.md#cancel_put) | **PUT** /cancel | 
[**check_message_signature_post**](DefaultApi.md#check_message_signature_post) | **POST** /check_message_signature | 
[**connected_get**](DefaultApi.md#connected_get) | **GET** /connected | 
[**csrf_get**](DefaultApi.md#csrf_get) | **GET** /csrf | 
[**features_get**](DefaultApi.md#features_get) | **GET** /features | 
[**firmware_update_put**](DefaultApi.md#firmware_update_put) | **PUT** /firmware_update | 
[**generate_addresses_post**](DefaultApi.md#generate_addresses_post) | **POST** /generate_addresses | 
[**generate_mnemonic_post**](DefaultApi.md#generate_mnemonic_post) | **POST** /generate_mnemonic | 
[**intermediate_passphrase_post**](DefaultApi.md#intermediate_passphrase_post) | **POST** /intermediate/passphrase | 
[**intermediate_pin_matrix_post**](DefaultApi.md#intermediate_pin_matrix_post) | **POST** /intermediate/pin_matrix | 
[**intermediate_word_post**](DefaultApi.md#intermediate_word_post) | **POST** /intermediate/word | 
[**recovery_post**](DefaultApi.md#recovery_post) | **POST** /recovery | 
[**set_mnemonic_post**](DefaultApi.md#set_mnemonic_post) | **POST** /set_mnemonic | 
[**set_pin_code_post**](DefaultApi.md#set_pin_code_post) | **POST** /set_pin_code | 
[**sign_message_post**](DefaultApi.md#sign_message_post) | **POST** /sign_message | 
[**transaction_sign_post**](DefaultApi.md#transaction_sign_post) | **POST** /transaction_sign | 
[**wipe_delete**](DefaultApi.md#wipe_delete) | **DELETE** /wipe | 


# **apply_settings_post**
> HTTPSuccessResponse apply_settings_post(apply_settings_request=apply_settings_request)



Apply hardware wallet settings.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))
apply_settings_request = skyhwd.ApplySettingsRequest() # ApplySettingsRequest | ApplySettingsRequest is request data for /api/v1/apply_settings (optional)

try:
    api_response = api_instance.apply_settings_post(apply_settings_request=apply_settings_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->apply_settings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apply_settings_request** | [**ApplySettingsRequest**](ApplySettingsRequest.md)| ApplySettingsRequest is request data for /api/v1/apply_settings | [optional] 

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_post**
> HTTPSuccessResponse backup_post()



Start seed backup procedure.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))

try:
    api_response = api_instance.backup_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->backup_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_put**
> HTTPSuccessResponse cancel_put()



Cancels the current operation.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))

try:
    api_response = api_instance.cancel_put()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->cancel_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_message_signature_post**
> HTTPSuccessResponse check_message_signature_post(check_message_signature_request=check_message_signature_request)



Check a message signature matches the given address.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))
check_message_signature_request = skyhwd.CheckMessageSignatureRequest() # CheckMessageSignatureRequest | CheckMessageSignatureRequest is request data for /api/v1/check_message_signature (optional)

try:
    api_response = api_instance.check_message_signature_post(check_message_signature_request=check_message_signature_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->check_message_signature_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_message_signature_request** | [**CheckMessageSignatureRequest**](CheckMessageSignatureRequest.md)| CheckMessageSignatureRequest is request data for /api/v1/check_message_signature | [optional] 

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connected_get**
> InlineResponse200 connected_get()



check whether device is connected or not.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))

try:
    api_response = api_instance.connected_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->connected_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csrf_get**
> CSRFResponse csrf_get()



Returns csrf token

### Example
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyhwd.DefaultApi()

try:
    api_response = api_instance.csrf_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->csrf_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CSRFResponse**](CSRFResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **features_get**
> FeaturesResponse features_get()



Returns device information.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))

try:
    api_response = api_instance.features_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->features_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FeaturesResponse**](FeaturesResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmware_update_put**
> HTTPSuccessResponse firmware_update_put()



Update firmware

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))

try:
    api_response = api_instance.firmware_update_put()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->firmware_update_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_addresses_post**
> GenerateAddressesResponse generate_addresses_post(generate_addresses_request=generate_addresses_request)



Generate addresses for the hardware wallet seed.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))
generate_addresses_request = skyhwd.GenerateAddressesRequest() # GenerateAddressesRequest | GenerateAddressesRequest is request data for /api/v1/generate_addresses (optional)

try:
    api_response = api_instance.generate_addresses_post(generate_addresses_request=generate_addresses_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_addresses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_addresses_request** | [**GenerateAddressesRequest**](GenerateAddressesRequest.md)| GenerateAddressesRequest is request data for /api/v1/generate_addresses | [optional] 

### Return type

[**GenerateAddressesResponse**](GenerateAddressesResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mnemonic_post**
> HTTPSuccessResponse generate_mnemonic_post(generate_mnemonic_request=generate_mnemonic_request)



Generate mnemonic can be used to initialize the device with a random seed.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))
generate_mnemonic_request = skyhwd.GenerateMnemonicRequest() # GenerateMnemonicRequest | GenerateMnemonicRequest is request data for /api/v1/generate_mnemonic (optional)

try:
    api_response = api_instance.generate_mnemonic_post(generate_mnemonic_request=generate_mnemonic_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_mnemonic_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_mnemonic_request** | [**GenerateMnemonicRequest**](GenerateMnemonicRequest.md)| GenerateMnemonicRequest is request data for /api/v1/generate_mnemonic | [optional] 

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intermediate_passphrase_post**
> HTTPSuccessResponse intermediate_passphrase_post(passphrase_request=passphrase_request)



passphrase ack request.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))
passphrase_request = skyhwd.PassphraseRequest() # PassphraseRequest | PassPhraseRequest is request data for /api/v1/intermediate/passphrase (optional)

try:
    api_response = api_instance.intermediate_passphrase_post(passphrase_request=passphrase_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->intermediate_passphrase_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **passphrase_request** | [**PassphraseRequest**](PassphraseRequest.md)| PassPhraseRequest is request data for /api/v1/intermediate/passphrase | [optional] 

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intermediate_pin_matrix_post**
> HTTPSuccessResponse intermediate_pin_matrix_post(pin_matrix_request=pin_matrix_request)



pin matrix ack request.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))
pin_matrix_request = skyhwd.PinMatrixRequest() # PinMatrixRequest | PinMatrixRequest is request data for /api/v1/intermediate/pin_matrix (optional)

try:
    api_response = api_instance.intermediate_pin_matrix_post(pin_matrix_request=pin_matrix_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->intermediate_pin_matrix_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pin_matrix_request** | [**PinMatrixRequest**](PinMatrixRequest.md)| PinMatrixRequest is request data for /api/v1/intermediate/pin_matrix | [optional] 

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intermediate_word_post**
> HTTPSuccessResponse intermediate_word_post(word_request=word_request)



word ack request.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))
word_request = skyhwd.WordRequest() # WordRequest | WordRequest is request data for /api/v1/intermediate/word (optional)

try:
    api_response = api_instance.intermediate_word_post(word_request=word_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->intermediate_word_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **word_request** | [**WordRequest**](WordRequest.md)| WordRequest is request data for /api/v1/intermediate/word | [optional] 

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recovery_post**
> HTTPSuccessResponse recovery_post(recovery_request=recovery_request)



Recover existing wallet using seed.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))
recovery_request = skyhwd.RecoveryRequest() # RecoveryRequest | RecoveryRequest is request data for /api/v1/check_message_signature (optional)

try:
    api_response = api_instance.recovery_post(recovery_request=recovery_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->recovery_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recovery_request** | [**RecoveryRequest**](RecoveryRequest.md)| RecoveryRequest is request data for /api/v1/check_message_signature | [optional] 

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mnemonic_post**
> HTTPSuccessResponse set_mnemonic_post(set_mnemonic_request=set_mnemonic_request)



Set mnemonic can be used to initialize the device with your own seed.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))
set_mnemonic_request = skyhwd.SetMnemonicRequest() # SetMnemonicRequest | SetMnemonicRequest is request data for /api/v1/set_mnemonic (optional)

try:
    api_response = api_instance.set_mnemonic_post(set_mnemonic_request=set_mnemonic_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->set_mnemonic_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_mnemonic_request** | [**SetMnemonicRequest**](SetMnemonicRequest.md)| SetMnemonicRequest is request data for /api/v1/set_mnemonic | [optional] 

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pin_code_post**
> HTTPSuccessResponse set_pin_code_post()



Configure a pin code on the device.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))

try:
    api_response = api_instance.set_pin_code_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->set_pin_code_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_message_post**
> SignMessageResponse sign_message_post(sign_message_request=sign_message_request)



Sign a message using the secret key at given index.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))
sign_message_request = skyhwd.SignMessageRequest() # SignMessageRequest | SignMessageRequest is request data for /api/signMessage (optional)

try:
    api_response = api_instance.sign_message_post(sign_message_request=sign_message_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->sign_message_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_message_request** | [**SignMessageRequest**](SignMessageRequest.md)| SignMessageRequest is request data for /api/signMessage | [optional] 

### Return type

[**SignMessageResponse**](SignMessageResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_sign_post**
> TransactionSignResponse transaction_sign_post(transaction_sign_request=transaction_sign_request)



Sign a transaction with the hardware wallet.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))
transaction_sign_request = skyhwd.TransactionSignRequest() # TransactionSignRequest | TransactionSignRequest is request data for /api/v1/transactionSign (optional)

try:
    api_response = api_instance.transaction_sign_post(transaction_sign_request=transaction_sign_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transaction_sign_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_sign_request** | [**TransactionSignRequest**](TransactionSignRequest.md)| TransactionSignRequest is request data for /api/v1/transactionSign | [optional] 

### Return type

[**TransactionSignResponse**](TransactionSignResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wipe_delete**
> HTTPSuccessResponse wipe_delete()



clean all the configurations.

### Example

* Api Key Authentication (csrfAuth): 
```python
from __future__ import print_function
import time
import skyhwd
from skyhwd.rest import ApiException
from pprint import pprint

# Configure API key authorization: csrfAuth
configuration = skyhwd.Configuration()
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyhwd.DefaultApi(skyhwd.ApiClient(configuration))

try:
    api_response = api_instance.wipe_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wipe_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HTTPSuccessResponse**](HTTPSuccessResponse.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

