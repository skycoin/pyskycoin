# skyapi
Skycoin is a next-generation cryptocurrency.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.26.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://skycoin.net](https://skycoin.net)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import skyapi 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import skyapi
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import skyapi
from skyapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = skyapi.DefaultApi(skyapi.ApiClient(configuration))

try:
    # Returns the total number of unique address that have coins.
    api_response = api_instance.address_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->address_count: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:6420*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**address_count**](docs/DefaultApi.md#address_count) | **GET** /api/v1/addresscount | Returns the total number of unique address that have coins.
*DefaultApi* | [**address_uxouts**](docs/DefaultApi.md#address_uxouts) | **GET** /api/v1/address_uxouts | 
*DefaultApi* | [**api_v1_rawtx_get**](docs/DefaultApi.md#api_v1_rawtx_get) | **GET** /api/v1/rawtx | 
*DefaultApi* | [**api_v2_metrics_get**](docs/DefaultApi.md#api_v2_metrics_get) | **GET** /api/v2/metrics | 
*DefaultApi* | [**balance_get**](docs/DefaultApi.md#balance_get) | **GET** /api/v1/balance | Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
*DefaultApi* | [**balance_post**](docs/DefaultApi.md#balance_post) | **POST** /api/v1/balance | Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
*DefaultApi* | [**block**](docs/DefaultApi.md#block) | **GET** /api/v1/block | Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
*DefaultApi* | [**blockchain_metadata**](docs/DefaultApi.md#blockchain_metadata) | **GET** /api/v1/blockchain/metadata | Returns the blockchain metadata.
*DefaultApi* | [**blockchain_progress**](docs/DefaultApi.md#blockchain_progress) | **GET** /api/v1/blockchain/progress | Returns the blockchain sync progress.
*DefaultApi* | [**blocks**](docs/DefaultApi.md#blocks) | **GET** /api/v1/blocks | Returns the balance of one or more addresses, both confirmed and predicted. The predicted balance is the confirmed balance minus the pending spends.
*DefaultApi* | [**coin_supply**](docs/DefaultApi.md#coin_supply) | **GET** /api/v1/coinSupply | 
*DefaultApi* | [**csrf**](docs/DefaultApi.md#csrf) | **GET** /api/v1/csrf | Creates a new CSRF token. Previous CSRF tokens are invalidated by this call.
*DefaultApi* | [**data_delete**](docs/DefaultApi.md#data_delete) | **DELETE** /api/v2/data | 
*DefaultApi* | [**data_get**](docs/DefaultApi.md#data_get) | **GET** /api/v2/data | 
*DefaultApi* | [**data_post**](docs/DefaultApi.md#data_post) | **POST** /api/v2/data | 
*DefaultApi* | [**default_connections**](docs/DefaultApi.md#default_connections) | **GET** /api/v1/network/defaultConnections | defaultConnectionsHandler returns the list of default hardcoded bootstrap addresses.\\n They are not necessarily connected to.
*DefaultApi* | [**health**](docs/DefaultApi.md#health) | **GET** /api/v1/health | Returns node health data.
*DefaultApi* | [**last_blocks**](docs/DefaultApi.md#last_blocks) | **GET** /api/v1/last_blocks | 
*DefaultApi* | [**network_connection**](docs/DefaultApi.md#network_connection) | **GET** /api/v1/network/connection | This endpoint returns a specific connection.
*DefaultApi* | [**network_connections**](docs/DefaultApi.md#network_connections) | **GET** /api/v1/network/connections | This endpoint returns all outgoings connections.
*DefaultApi* | [**network_connections_disconnect**](docs/DefaultApi.md#network_connections_disconnect) | **POST** /api/v1/network/connection/disconnect | 
*DefaultApi* | [**network_connections_exchange**](docs/DefaultApi.md#network_connections_exchange) | **GET** /api/v1/network/connections/exchange | 
*DefaultApi* | [**network_connections_trust**](docs/DefaultApi.md#network_connections_trust) | **GET** /api/v1/network/connections/trust | trustConnectionsHandler returns all trusted connections.\\n They are not necessarily connected to. In the default configuration, these will be a subset of the default hardcoded bootstrap addresses.
*DefaultApi* | [**outputs_get**](docs/DefaultApi.md#outputs_get) | **GET** /api/v1/outputs | If neither addrs nor hashes are specificed, return all unspent outputs. If only one filter is specified, then return outputs match the filter. Both filters cannot be specified.
*DefaultApi* | [**outputs_post**](docs/DefaultApi.md#outputs_post) | **POST** /api/v1/outputs | If neither addrs nor hashes are specificed, return all unspent outputs. If only one filter is specified, then return outputs match the filter. Both filters cannot be specified.
*DefaultApi* | [**pending_txs**](docs/DefaultApi.md#pending_txs) | **GET** /api/v1/pendingTxs | 
*DefaultApi* | [**resend_unconfirmed_txns**](docs/DefaultApi.md#resend_unconfirmed_txns) | **POST** /api/v1/resendUnconfirmedTxns | 
*DefaultApi* | [**richlist**](docs/DefaultApi.md#richlist) | **GET** /api/v1/richlist | Returns the top skycoin holders.
*DefaultApi* | [**transaction**](docs/DefaultApi.md#transaction) | **GET** /api/v1/transaction | 
*DefaultApi* | [**transaction_inject**](docs/DefaultApi.md#transaction_inject) | **POST** /api/v1/injectTransaction | Broadcast a hex-encoded, serialized transaction to the network.
*DefaultApi* | [**transaction_post**](docs/DefaultApi.md#transaction_post) | **POST** /api/v2/transaction | 
*DefaultApi* | [**transaction_post_unspent**](docs/DefaultApi.md#transaction_post_unspent) | **POST** /api/v2/transaction/unspent | 
*DefaultApi* | [**transaction_raw**](docs/DefaultApi.md#transaction_raw) | **GET** /api/v2/transaction/raw | Returns the hex-encoded byte serialization of a transaction. The transaction may be confirmed or unconfirmed.
*DefaultApi* | [**transaction_verify**](docs/DefaultApi.md#transaction_verify) | **POST** /api/v2/transaction/verify | 
*DefaultApi* | [**transactions_get**](docs/DefaultApi.md#transactions_get) | **GET** /api/v1/transactions | Returns transactions that match the filters.
*DefaultApi* | [**transactions_post**](docs/DefaultApi.md#transactions_post) | **POST** /api/v1/transactions | Returns transactions that match the filters.
*DefaultApi* | [**uxout**](docs/DefaultApi.md#uxout) | **GET** /api/v1/uxout | Returns an unspent output by ID.
*DefaultApi* | [**verify_address**](docs/DefaultApi.md#verify_address) | **POST** /api/v2/address/verify | Verifies a Skycoin address.
*DefaultApi* | [**version**](docs/DefaultApi.md#version) | **GET** /api/v1/version | 
*DefaultApi* | [**wallet**](docs/DefaultApi.md#wallet) | **GET** /api/v1/wallet | Returns a wallet by id.
*DefaultApi* | [**wallet_balance**](docs/DefaultApi.md#wallet_balance) | **GET** /api/v1/wallet/balance | Returns the wallet&#39;s balance, both confirmed and predicted.  The predicted balance is the confirmed balance minus the pending spends.
*DefaultApi* | [**wallet_create**](docs/DefaultApi.md#wallet_create) | **POST** /api/v1/wallet/create | 
*DefaultApi* | [**wallet_decrypt**](docs/DefaultApi.md#wallet_decrypt) | **POST** /api/v1/wallet/decrypt | Decrypts wallet.
*DefaultApi* | [**wallet_encrypt**](docs/DefaultApi.md#wallet_encrypt) | **POST** /api/v1/wallet/encrypt | Encrypt wallet.
*DefaultApi* | [**wallet_folder**](docs/DefaultApi.md#wallet_folder) | **GET** /api/v1/wallets/folderName | 
*DefaultApi* | [**wallet_new_address**](docs/DefaultApi.md#wallet_new_address) | **POST** /api/v1/wallet/newAddress | 
*DefaultApi* | [**wallet_new_seed**](docs/DefaultApi.md#wallet_new_seed) | **GET** /api/v1/wallet/newSeed | 
*DefaultApi* | [**wallet_recover**](docs/DefaultApi.md#wallet_recover) | **POST** /api/v2/wallet/recover | Recovers an encrypted wallet by providing the seed. The first address will be generated from seed and compared to the first address of the specified wallet. If they match, the wallet will be regenerated with an optional password. If the wallet is not encrypted, an error is returned.
*DefaultApi* | [**wallet_seed**](docs/DefaultApi.md#wallet_seed) | **POST** /api/v1/wallet/seed | This endpoint only works for encrypted wallets. If the wallet is unencrypted, The seed will be not returned.
*DefaultApi* | [**wallet_seed_verify**](docs/DefaultApi.md#wallet_seed_verify) | **POST** /api/v2/wallet/seed/verify | Verifies a wallet seed.
*DefaultApi* | [**wallet_transaction**](docs/DefaultApi.md#wallet_transaction) | **POST** /api/v1/wallet/transaction | Creates a signed transaction
*DefaultApi* | [**wallet_transaction_sign**](docs/DefaultApi.md#wallet_transaction_sign) | **POST** /api/v2/wallet/transaction/sign | Creates a signed transaction
*DefaultApi* | [**wallet_transactions**](docs/DefaultApi.md#wallet_transactions) | **GET** /api/v1/wallet/transactions | 
*DefaultApi* | [**wallet_unload**](docs/DefaultApi.md#wallet_unload) | **POST** /api/v1/wallet/unload | Unloads wallet from the wallet service.
*DefaultApi* | [**wallet_update**](docs/DefaultApi.md#wallet_update) | **POST** /api/v1/wallet/update | Update the wallet.
*DefaultApi* | [**wallets**](docs/DefaultApi.md#wallets) | **GET** /api/v1/wallets | 


## Documentation For Models

 - [Address](docs/Address.md)
 - [ApiV1PendingTxsTransaction](docs/ApiV1PendingTxsTransaction.md)
 - [ApiV1PendingTxsTransactionOutputs](docs/ApiV1PendingTxsTransactionOutputs.md)
 - [BlockSchema](docs/BlockSchema.md)
 - [BlockSchemaBody](docs/BlockSchemaBody.md)
 - [BlockVerboseSchema](docs/BlockVerboseSchema.md)
 - [BlockVerboseSchemaBody](docs/BlockVerboseSchemaBody.md)
 - [BlockVerboseSchemaHeader](docs/BlockVerboseSchemaHeader.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2008Data](docs/InlineResponse2008Data.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponseDefault](docs/InlineResponseDefault.md)
 - [NetworkConnectionSchema](docs/NetworkConnectionSchema.md)
 - [NetworkConnectionSchemaUnconfirmedVerifyTransaction](docs/NetworkConnectionSchemaUnconfirmedVerifyTransaction.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionEncoded](docs/TransactionEncoded.md)
 - [TransactionEncodedS](docs/TransactionEncodedS.md)
 - [TransactionStatus](docs/TransactionStatus.md)
 - [TransactionTxn](docs/TransactionTxn.md)
 - [TransactionV2ParamsAddress](docs/TransactionV2ParamsAddress.md)
 - [TransactionV2ParamsAddressHoursSelection](docs/TransactionV2ParamsAddressHoursSelection.md)
 - [TransactionV2ParamsUnspent](docs/TransactionV2ParamsUnspent.md)
 - [TransactionV2ParamsUnspentHoursSelection](docs/TransactionV2ParamsUnspentHoursSelection.md)
 - [TransactionV2ParamsUnspentTo](docs/TransactionV2ParamsUnspentTo.md)
 - [TransactionVerbose](docs/TransactionVerbose.md)
 - [TransactionVerboseTxn](docs/TransactionVerboseTxn.md)
 - [TransactionVerboseTxnInputs](docs/TransactionVerboseTxnInputs.md)
 - [TransactionVerifyRequest](docs/TransactionVerifyRequest.md)
 - [WalletTransactionRequest](docs/WalletTransactionRequest.md)
 - [WalletTransactionRequestHoursSelection](docs/WalletTransactionRequestHoursSelection.md)
 - [WalletTransactionRequestWallet](docs/WalletTransactionRequestWallet.md)
 - [WalletTransactionSignRequest](docs/WalletTransactionSignRequest.md)


## Documentation For Authorization


## csrfAuth

- **Type**: API key
- **API key parameter name**: X-CSRF-TOKEN
- **Location**: HTTP header


## Author

contact@skycoin.net


