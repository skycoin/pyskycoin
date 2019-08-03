# skyapi.DefaultApi

All URIs are relative to *http://127.0.0.1:6420*

Method | HTTP request | Description
------------- | ------------- | -------------
[**address_count**](DefaultApi.md#address_count) | **GET** /api/v1/addresscount | Returns the total number of unique address that have coins.
[**address_uxouts**](DefaultApi.md#address_uxouts) | **GET** /api/v1/address_uxouts | 
[**api_v1_rawtx_get**](DefaultApi.md#api_v1_rawtx_get) | **GET** /api/v1/rawtx | 
[**api_v2_metrics_get**](DefaultApi.md#api_v2_metrics_get) | **GET** /api/v2/metrics | 
[**balance_get**](DefaultApi.md#balance_get) | **GET** /api/v1/balance | Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
[**balance_post**](DefaultApi.md#balance_post) | **POST** /api/v1/balance | Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
[**block**](DefaultApi.md#block) | **GET** /api/v1/block | Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
[**blockchain_metadata**](DefaultApi.md#blockchain_metadata) | **GET** /api/v1/blockchain/metadata | Returns the blockchain metadata.
[**blockchain_progress**](DefaultApi.md#blockchain_progress) | **GET** /api/v1/blockchain/progress | Returns the blockchain sync progress.
[**blocks**](DefaultApi.md#blocks) | **GET** /api/v1/blocks | Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
[**coin_supply**](DefaultApi.md#coin_supply) | **GET** /api/v1/coinSupply | 
[**csrf**](DefaultApi.md#csrf) | **GET** /api/v1/csrf | Creates a new CSRF token. Previous CSRF tokens are invalidated by this call.
[**data_delete**](DefaultApi.md#data_delete) | **DELETE** /api/v2/data | 
[**data_get**](DefaultApi.md#data_get) | **GET** /api/v2/data | 
[**data_post**](DefaultApi.md#data_post) | **POST** /api/v2/data | 
[**default_connections**](DefaultApi.md#default_connections) | **GET** /api/v1/network/defaultConnections | defaultConnectionsHandler returns the list of default hardcoded bootstrap addresses.\\n They are not necessarily connected to.
[**health**](DefaultApi.md#health) | **GET** /api/v1/health | Returns node health data.
[**last_blocks**](DefaultApi.md#last_blocks) | **GET** /api/v1/last_blocks | 
[**network_connection**](DefaultApi.md#network_connection) | **GET** /api/v1/network/connection | This endpoint returns a specific connection.
[**network_connections**](DefaultApi.md#network_connections) | **GET** /api/v1/network/connections | This endpoint returns all outgoings connections.
[**network_connections_disconnect**](DefaultApi.md#network_connections_disconnect) | **POST** /api/v1/network/connection/disconnect | 
[**network_connections_exchange**](DefaultApi.md#network_connections_exchange) | **GET** /api/v1/network/connections/exchange | 
[**network_connections_trust**](DefaultApi.md#network_connections_trust) | **GET** /api/v1/network/connections/trust | trustConnectionsHandler returns all trusted connections.\\n They are not necessarily connected to. In the default configuration, these will be a subset of the default hardcoded bootstrap addresses.
[**outputs_get**](DefaultApi.md#outputs_get) | **GET** /api/v1/outputs | If neither addrs nor hashes are specificed, return all unspent outputs. If only one filter is specified, then return outputs match the filter. Both filters cannot be specified.
[**outputs_post**](DefaultApi.md#outputs_post) | **POST** /api/v1/outputs | If neither addrs nor hashes are specificed, return all unspent outputs. If only one filter is specified, then return outputs match the filter. Both filters cannot be specified.
[**pending_txs**](DefaultApi.md#pending_txs) | **GET** /api/v1/pendingTxs | 
[**resend_unconfirmed_txns**](DefaultApi.md#resend_unconfirmed_txns) | **POST** /api/v1/resendUnconfirmedTxns | 
[**richlist**](DefaultApi.md#richlist) | **GET** /api/v1/richlist | Returns the top skycoin holders.
[**transaction**](DefaultApi.md#transaction) | **GET** /api/v1/transaction | 
[**transaction_inject**](DefaultApi.md#transaction_inject) | **POST** /api/v1/injectTransaction | Broadcast a hex-encoded, serialized transaction to the network.
[**transaction_post**](DefaultApi.md#transaction_post) | **POST** /api/v2/transaction | 
[**transaction_post_unspent**](DefaultApi.md#transaction_post_unspent) | **POST** /api/v2/transaction/unspent | 
[**transaction_raw**](DefaultApi.md#transaction_raw) | **GET** /api/v2/transaction/raw | Returns the hex-encoded byte serialization of a transaction. The transaction may be confirmed or unconfirmed.
[**transaction_verify**](DefaultApi.md#transaction_verify) | **POST** /api/v2/transaction/verify | 
[**transactions_get**](DefaultApi.md#transactions_get) | **GET** /api/v1/transactions | Returns transactions that match the filters.
[**transactions_post**](DefaultApi.md#transactions_post) | **POST** /api/v1/transactions | Returns transactions that match the filters.
[**uxout**](DefaultApi.md#uxout) | **GET** /api/v1/uxout | Returns an unspent output by ID.
[**verify_address**](DefaultApi.md#verify_address) | **POST** /api/v2/address/verify | Verifies a Skycoin address.
[**version**](DefaultApi.md#version) | **GET** /api/v1/version | 
[**wallet**](DefaultApi.md#wallet) | **GET** /api/v1/wallet | Returns a wallet by id.
[**wallet_balance**](DefaultApi.md#wallet_balance) | **GET** /api/v1/wallet/balance | Returns the wallet&#39;s balance, both confirmed and predicted.  The predicted balance is the confirmed balance minus the pending spends.
[**wallet_create**](DefaultApi.md#wallet_create) | **POST** /api/v1/wallet/create | 
[**wallet_decrypt**](DefaultApi.md#wallet_decrypt) | **POST** /api/v1/wallet/decrypt | Decrypts wallet.
[**wallet_encrypt**](DefaultApi.md#wallet_encrypt) | **POST** /api/v1/wallet/encrypt | Encrypt wallet.
[**wallet_folder**](DefaultApi.md#wallet_folder) | **GET** /api/v1/wallets/folderName | 
[**wallet_new_address**](DefaultApi.md#wallet_new_address) | **POST** /api/v1/wallet/newAddress | 
[**wallet_new_seed**](DefaultApi.md#wallet_new_seed) | **GET** /api/v1/wallet/newSeed | 
[**wallet_recover**](DefaultApi.md#wallet_recover) | **POST** /api/v2/wallet/recover | Recovers an encrypted wallet by providing the seed. The first address will be generated from seed and compared to the first address of the specified wallet. If they match, the wallet will be regenerated with an optional password. If the wallet is not encrypted, an error is returned.
[**wallet_seed**](DefaultApi.md#wallet_seed) | **POST** /api/v1/wallet/seed | This endpoint only works for encrypted wallets. If the wallet is unencrypted, The seed will be not returned.
[**wallet_seed_verify**](DefaultApi.md#wallet_seed_verify) | **POST** /api/v2/wallet/seed/verify | Verifies a wallet seed.
[**wallet_transaction**](DefaultApi.md#wallet_transaction) | **POST** /api/v1/wallet/transaction | Creates a signed transaction
[**wallet_transaction_sign**](DefaultApi.md#wallet_transaction_sign) | **POST** /api/v2/wallet/transaction/sign | Creates a signed transaction
[**wallet_transactions**](DefaultApi.md#wallet_transactions) | **GET** /api/v1/wallet/transactions | 
[**wallet_unload**](DefaultApi.md#wallet_unload) | **POST** /api/v1/wallet/unload | Unloads wallet from the wallet service.
[**wallet_update**](DefaultApi.md#wallet_update) | **POST** /api/v1/wallet/update | Update the wallet.
[**wallets**](DefaultApi.md#wallets) | **GET** /api/v1/wallets | 


# **address_count**
> InlineResponse200 address_count()

Returns the total number of unique address that have coins.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    # Returns the total number of unique address that have coins.
    api_response = api_instance.address_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->address_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **address_uxouts**
> list[object] address_uxouts(address)



Returns the historical, spent outputs associated with an address

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
address = 'address_example' # str | address to filter by

try:
    api_response = api_instance.address_uxouts(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->address_uxouts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| address to filter by | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_rawtx_get**
> str api_v1_rawtx_get()



### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    api_response = api_instance.api_v1_rawtx_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v1_rawtx_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_metrics_get**
> str api_v2_metrics_get()



### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    api_response = api_instance.api_v2_metrics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->api_v2_metrics_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balance_get**
> object balance_get(addrs)

Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
addrs = 'addrs_example' # str | command separated list of addresses

try:
    # Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
    api_response = api_instance.balance_get(addrs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->balance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addrs** | **str**| command separated list of addresses | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **balance_post**
> object balance_post(addrs)

Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
addrs = 'addrs_example' # str | command separated list of addresses

try:
    # Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
    api_response = api_instance.balance_post(addrs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->balance_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addrs** | **str**| command separated list of addresses | 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block**
> list[BlockSchema] block(hash=hash, seq=seq)

Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
hash = 'hash_example' # str | get block by hash (optional)
seq = 56 # int | get block by sequence number (optional)

try:
    # Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
    api_response = api_instance.block(hash=hash, seq=seq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| get block by hash | [optional] 
 **seq** | **int**| get block by sequence number | [optional] 

### Return type

[**list[BlockSchema]**](BlockSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blockchain_metadata**
> object blockchain_metadata()

Returns the blockchain metadata.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    # Returns the blockchain metadata.
    api_response = api_instance.blockchain_metadata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->blockchain_metadata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blockchain_progress**
> object blockchain_progress()

Returns the blockchain sync progress.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    # Returns the blockchain sync progress.
    api_response = api_instance.blockchain_progress()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->blockchain_progress: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blocks**
> InlineResponse2001 blocks(start=start, end=end, seq=seq)

Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
start = 56 # int | start seq (optional)
end = 56 # int | end seq (optional)
seq = [56] # list[int] | comma-separated list of block seqs (optional)

try:
    # Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
    api_response = api_instance.blocks(start=start, end=end, seq=seq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| start seq | [optional] 
 **end** | **int**| end seq | [optional] 
 **seq** | [**list[int]**](int.md)| comma-separated list of block seqs | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **coin_supply**
> InlineResponse2002 coin_supply()



coinSupplyHandler returns coin distribution supply stats

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    api_response = api_instance.coin_supply()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->coin_supply: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csrf**
> InlineResponse2003 csrf()

Creates a new CSRF token. Previous CSRF tokens are invalidated by this call.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    # Creates a new CSRF token. Previous CSRF tokens are invalidated by this call.
    api_response = api_instance.csrf()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->csrf: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_delete**
> data_delete(type=type, key=key)



### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
type = 'type_example' # str | storage type. (optional)
key = 'key_example' # str | key of the specific value to get. (optional)

try:
    api_instance.data_delete(type=type, key=key)
except ApiException as e:
    print("Exception when calling DefaultApi->data_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| storage type. | [optional] 
 **key** | **str**| key of the specific value to get. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_get**
> object data_get(type=type, key=key)



### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
type = 'type_example' # str | storage type. (optional)
key = 'key_example' # str | key of the specific value to get. (optional)

try:
    api_response = api_instance.data_get(type=type, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| storage type. | [optional] 
 **key** | **str**| key of the specific value to get. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_post**
> data_post(type=type, key=key, val=val)



### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
type = 'type_example' # str | storage type. (optional)
key = 'key_example' # str | key of the specific value to get. (optional)
val = 'val_example' # str | additional value. (optional)

try:
    api_instance.data_post(type=type, key=key, val=val)
except ApiException as e:
    print("Exception when calling DefaultApi->data_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| storage type. | [optional] 
 **key** | **str**| key of the specific value to get. | [optional] 
 **val** | **str**| additional value. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **default_connections**
> list[str] default_connections()

defaultConnectionsHandler returns the list of default hardcoded bootstrap addresses.\\n They are not necessarily connected to.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    # defaultConnectionsHandler returns the list of default hardcoded bootstrap addresses.\\n They are not necessarily connected to.
    api_response = api_instance.default_connections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->default_connections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health**
> object health()

Returns node health data.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    # Returns node health data.
    api_response = api_instance.health()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **last_blocks**
> object last_blocks(num)



Returns the most recent N blocks on the blockchain

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
num = 56 # int | Num of blockss

try:
    api_response = api_instance.last_blocks(num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->last_blocks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num** | **int**| Num of blockss | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_connection**
> NetworkConnectionSchema network_connection(addr)

This endpoint returns a specific connection.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
addr = 'addr_example' # str | Address port

try:
    # This endpoint returns a specific connection.
    api_response = api_instance.network_connection(addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->network_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **str**| Address port | 

### Return type

[**NetworkConnectionSchema**](NetworkConnectionSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_connections**
> InlineResponse2004 network_connections(states=states, direction=direction)

This endpoint returns all outgoings connections.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
states = 'states_example' # str | Connection status. (optional)
direction = 'direction_example' # str | Direction of the connection. (optional)

try:
    # This endpoint returns all outgoings connections.
    api_response = api_instance.network_connections(states=states, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->network_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **states** | **str**| Connection status. | [optional] 
 **direction** | **str**| Direction of the connection. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_connections_disconnect**
> network_connections_disconnect(id)



This endpoint disconnects a connection by ID or address

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
id = 'id_example' # str | Address id.

try:
    api_instance.network_connections_disconnect(id)
except ApiException as e:
    print("Exception when calling DefaultApi->network_connections_disconnect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Address id. | 

### Return type

void (empty response body)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_connections_exchange**
> list[str] network_connections_exchange()



This endpoint returns all connections found through peer exchange

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    api_response = api_instance.network_connections_exchange()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->network_connections_exchange: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_connections_trust**
> list[str] network_connections_trust()

trustConnectionsHandler returns all trusted connections.\\n They are not necessarily connected to. In the default configuration, these will be a subset of the default hardcoded bootstrap addresses.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    # trustConnectionsHandler returns all trusted connections.\\n They are not necessarily connected to. In the default configuration, these will be a subset of the default hardcoded bootstrap addresses.
    api_response = api_instance.network_connections_trust()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->network_connections_trust: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outputs_get**
> object outputs_get(address=address, hash=hash)

If neither addrs nor hashes are specificed, return all unspent outputs. If only one filter is specified, then return outputs match the filter. Both filters cannot be specified.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
address = ['address_example'] # list[str] |  (optional)
hash = ['hash_example'] # list[str] |  (optional)

try:
    # If neither addrs nor hashes are specificed, return all unspent outputs. If only one filter is specified, then return outputs match the filter. Both filters cannot be specified.
    api_response = api_instance.outputs_get(address=address, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->outputs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**list[str]**](str.md)|  | [optional] 
 **hash** | [**list[str]**](str.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **outputs_post**
> object outputs_post(address=address, hash=hash)

If neither addrs nor hashes are specificed, return all unspent outputs. If only one filter is specified, then return outputs match the filter. Both filters cannot be specified.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
address = 'address_example' # str |  (optional)
hash = 'hash_example' # str |  (optional)

try:
    # If neither addrs nor hashes are specificed, return all unspent outputs. If only one filter is specified, then return outputs match the filter. Both filters cannot be specified.
    api_response = api_instance.outputs_post(address=address, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->outputs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**|  | [optional] 
 **hash** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pending_txs**
> list[InlineResponse20010] pending_txs()



### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    api_response = api_instance.pending_txs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->pending_txs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse20010]**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_unconfirmed_txns**
> object resend_unconfirmed_txns()



Broadcasts all unconfirmed transactions from the unconfirmed transaction pool

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))

try:
    api_response = api_instance.resend_unconfirmed_txns()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->resend_unconfirmed_txns: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application-json, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **richlist**
> object richlist(include_distribution=include_distribution, n=n)

Returns the top skycoin holders.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
include_distribution = True # bool | include distribution addresses or not, default value false (optional)
n = 'n_example' # str | include distribution addresses or not, default value false (optional)

try:
    # Returns the top skycoin holders.
    api_response = api_instance.richlist(include_distribution=include_distribution, n=n)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->richlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_distribution** | **bool**| include distribution addresses or not, default value false | [optional] 
 **n** | **str**| include distribution addresses or not, default value false | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction**
> Transaction transaction(txid)



Returns a transaction identified by its txid hash with just id

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
txid = 'txid_example' # str | transaction Id

try:
    api_response = api_instance.transaction(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| transaction Id | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_inject**
> str transaction_inject(rawtx)

Broadcast a hex-encoded, serialized transaction to the network.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
rawtx = 'rawtx_example' # str | hex-encoded serialized transaction string.

try:
    # Broadcast a hex-encoded, serialized transaction to the network.
    api_response = api_instance.transaction_inject(rawtx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transaction_inject: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rawtx** | **str**| hex-encoded serialized transaction string. | 

### Return type

**str**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_post**
> InlineResponse2008 transaction_post(transaction_v2_params_address=transaction_v2_params_address)



### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
transaction_v2_params_address = skyapi.TransactionV2ParamsAddress() # TransactionV2ParamsAddress |  (optional)

try:
    api_response = api_instance.transaction_post(transaction_v2_params_address=transaction_v2_params_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transaction_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_v2_params_address** | [**TransactionV2ParamsAddress**](TransactionV2ParamsAddress.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_post_unspent**
> InlineResponse2008 transaction_post_unspent(transaction_v2_params_unspent)



### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
transaction_v2_params_unspent = skyapi.TransactionV2ParamsUnspent() # TransactionV2ParamsUnspent | Unspent parameters

try:
    api_response = api_instance.transaction_post_unspent(transaction_v2_params_unspent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transaction_post_unspent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_v2_params_unspent** | [**TransactionV2ParamsUnspent**](TransactionV2ParamsUnspent.md)| Unspent parameters | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_raw**
> object transaction_raw(txid=txid)

Returns the hex-encoded byte serialization of a transaction. The transaction may be confirmed or unconfirmed.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
txid = 'txid_example' # str | Transaction id hash (optional)

try:
    # Returns the hex-encoded byte serialization of a transaction. The transaction may be confirmed or unconfirmed.
    api_response = api_instance.transaction_raw(txid=txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transaction_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction id hash | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_verify**
> object transaction_verify(transaction_verify_request)



Decode and verify an encoded transaction

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
transaction_verify_request = skyapi.TransactionVerifyRequest() # TransactionVerifyRequest | 

try:
    api_response = api_instance.transaction_verify(transaction_verify_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transaction_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_verify_request** | [**TransactionVerifyRequest**](TransactionVerifyRequest.md)|  | 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_get**
> object transactions_get(addrs=addrs, confirmed=confirmed)

Returns transactions that match the filters.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
addrs = 'addrs_example' # str | command separated list of addresses (optional)
confirmed = 'confirmed_example' # str | Whether the transactions should be confirmed [optional, must be 0 or 1; if not provided, returns all] (optional)

try:
    # Returns transactions that match the filters.
    api_response = api_instance.transactions_get(addrs=addrs, confirmed=confirmed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addrs** | **str**| command separated list of addresses | [optional] 
 **confirmed** | **str**| Whether the transactions should be confirmed [optional, must be 0 or 1; if not provided, returns all] | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_post**
> object transactions_post(addrs=addrs, confirmed=confirmed)

Returns transactions that match the filters.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
addrs = 'addrs_example' # str | command separated list of addresses (optional)
confirmed = 'confirmed_example' # str | Whether the transactions should be confirmed [optional, must be 0 or 1; if not provided, returns all] (optional)

try:
    # Returns transactions that match the filters.
    api_response = api_instance.transactions_post(addrs=addrs, confirmed=confirmed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->transactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addrs** | **str**| command separated list of addresses | [optional] 
 **confirmed** | **str**| Whether the transactions should be confirmed [optional, must be 0 or 1; if not provided, returns all] | [optional] 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uxout**
> object uxout(uxid=uxid)

Returns an unspent output by ID.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
uxid = 'uxid_example' # str | uxid to filter by (optional)

try:
    # Returns an unspent output by ID.
    api_response = api_instance.uxout(uxid=uxid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->uxout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uxid** | **str**| uxid to filter by | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_address**
> object verify_address(address)

Verifies a Skycoin address.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
address = None # object | Address id.

try:
    # Verifies a Skycoin address.
    api_response = api_instance.verify_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->verify_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | [**object**](.md)| Address id. | 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **version**
> InlineResponse2005 version()



versionHandler returns the application version info

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    api_response = api_instance.version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet**
> object wallet(id)

Returns a wallet by id.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
id = 'id_example' # str | tags to filter by

try:
    # Returns a wallet by id.
    api_response = api_instance.wallet(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| tags to filter by | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_balance**
> object wallet_balance(id)

Returns the wallet's balance, both confirmed and predicted.  The predicted balance is the confirmed balance minus the pending spends.

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
id = 'id_example' # str | tags to filter by

try:
    # Returns the wallet's balance, both confirmed and predicted.  The predicted balance is the confirmed balance minus the pending spends.
    api_response = api_instance.wallet_balance(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| tags to filter by | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_create**
> object wallet_create(seed, label, scan=scan, encrypt=encrypt, password=password)



Loads wallet from seed, will scan ahead N address and load addresses till the last one that have coins.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
seed = 'seed_example' # str | Wallet seed.
label = 'label_example' # str | Wallet label.
scan = 56 # int | The number of addresses to scan ahead for balances. (optional)
encrypt = True # bool | Encrypt wallet. (optional)
password = 'password_example' # str | Wallet Password (optional)

try:
    api_response = api_instance.wallet_create(seed, label, scan=scan, encrypt=encrypt, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seed** | **str**| Wallet seed. | 
 **label** | **str**| Wallet label. | 
 **scan** | **int**| The number of addresses to scan ahead for balances. | [optional] 
 **encrypt** | **bool**| Encrypt wallet. | [optional] 
 **password** | **str**| Wallet Password | [optional] 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_decrypt**
> object wallet_decrypt(id, password)

Decrypts wallet.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
id = 'id_example' # str | Wallet id.
password = 'password_example' # str | Wallet password.

try:
    # Decrypts wallet.
    api_response = api_instance.wallet_decrypt(id, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_decrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet id. | 
 **password** | **str**| Wallet password. | 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_encrypt**
> object wallet_encrypt(id, password)

Encrypt wallet.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
id = 'id_example' # str | Wallet id.
password = 'password_example' # str | Wallet password.

try:
    # Encrypt wallet.
    api_response = api_instance.wallet_encrypt(id, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_encrypt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet id. | 
 **password** | **str**| Wallet password. | 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_folder**
> InlineResponse2007 wallet_folder(addr)



Returns the wallet directory path

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
addr = 'addr_example' # str | Address port

try:
    api_response = api_instance.wallet_folder(addr)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addr** | **str**| Address port | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_new_address**
> object wallet_new_address(id, num=num, password=password)



Generates new addresses

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
id = 'id_example' # str | Wallet Id
num = 'num_example' # str | The number you want to generate (optional)
password = 'password_example' # str | Wallet Password (optional)

try:
    api_response = api_instance.wallet_new_address(id, num=num, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_new_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet Id | 
 **num** | **str**| The number you want to generate | [optional] 
 **password** | **str**| Wallet Password | [optional] 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_new_seed**
> object wallet_new_seed(entropy=entropy)



Returns the wallet directory path

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
entropy = 'entropy_example' # str | Entropy bitSize. (optional)

try:
    api_response = api_instance.wallet_new_seed(entropy=entropy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_new_seed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entropy** | **str**| Entropy bitSize. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_recover**
> object wallet_recover(id, seed, password=password)

Recovers an encrypted wallet by providing the seed. The first address will be generated from seed and compared to the first address of the specified wallet. If they match, the wallet will be regenerated with an optional password. If the wallet is not encrypted, an error is returned.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
id = 'id_example' # str | Wallet id.
seed = 'seed_example' # str | Wallet seed.
password = 'password_example' # str | Wallet password. (optional)

try:
    # Recovers an encrypted wallet by providing the seed. The first address will be generated from seed and compared to the first address of the specified wallet. If they match, the wallet will be regenerated with an optional password. If the wallet is not encrypted, an error is returned.
    api_response = api_instance.wallet_recover(id, seed, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_recover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet id. | 
 **seed** | **str**| Wallet seed. | 
 **password** | **str**| Wallet password. | [optional] 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_seed**
> object wallet_seed(id, password)

This endpoint only works for encrypted wallets. If the wallet is unencrypted, The seed will be not returned.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
id = 'id_example' # str | Wallet Id.
password = 'password_example' # str | Wallet password.

try:
    # This endpoint only works for encrypted wallets. If the wallet is unencrypted, The seed will be not returned.
    api_response = api_instance.wallet_seed(id, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_seed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet Id. | 
 **password** | **str**| Wallet password. | 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_seed_verify**
> object wallet_seed_verify(seed=seed)

Verifies a wallet seed.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
seed = 'seed_example' # str | Seed to be verified. (optional)

try:
    # Verifies a wallet seed.
    api_response = api_instance.wallet_seed_verify(seed=seed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_seed_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **seed** | **str**| Seed to be verified. | [optional] 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_transaction**
> object wallet_transaction(wallet_transaction_request)

Creates a signed transaction

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
wallet_transaction_request = skyapi.WalletTransactionRequest() # WalletTransactionRequest | 

try:
    # Creates a signed transaction
    api_response = api_instance.wallet_transaction(wallet_transaction_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_transaction_request** | [**WalletTransactionRequest**](WalletTransactionRequest.md)|  | 

### Return type

**object**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_transaction_sign**
> InlineResponse2009 wallet_transaction_sign(wallet_transaction_sign_request)

Creates a signed transaction

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
wallet_transaction_sign_request = skyapi.WalletTransactionSignRequest() # WalletTransactionSignRequest | 

try:
    # Creates a signed transaction
    api_response = api_instance.wallet_transaction_sign(wallet_transaction_sign_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_transaction_sign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_transaction_sign_request** | [**WalletTransactionSignRequest**](WalletTransactionSignRequest.md)|  | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_transactions**
> InlineResponse2006 wallet_transactions(id)



### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()
id = 'id_example' # str | Wallet Id.

try:
    api_response = api_instance.wallet_transactions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet Id. | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_unload**
> wallet_unload(id)

Unloads wallet from the wallet service.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
id = 'id_example' # str | Wallet Id.

try:
    # Unloads wallet from the wallet service.
    api_instance.wallet_unload(id)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_unload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet Id. | 

### Return type

void (empty response body)

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallet_update**
> str wallet_update(id, label)

Update the wallet.

### Example

* Api Key Authentication (csrfAuth):
```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint
configuration = skyapi.Configuration()
# Configure API key authorization: csrfAuth
configuration.api_key['X-CSRF-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-CSRF-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))
id = 'id_example' # str | Wallet Id.
label = 'label_example' # str | The label the wallet will be updated to.

try:
    # Update the wallet.
    api_response = api_instance.wallet_update(id, label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallet_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Wallet Id. | 
 **label** | **str**| The label the wallet will be updated to. | 

### Return type

**str**

### Authorization

[csrfAuth](../README.md#csrfAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallets**
> list[object] wallets()



Returns all loaded wallets

### Example

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = skyapi.DefaultApi()

try:
    api_response = api_instance.wallets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->wallets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, 

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

