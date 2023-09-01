from web3 import Web3 

ganache_url = 'http://127.0.0.1:7545'
web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Loba_account = '0x3750B5fE4121D1Ace6052cB2F2483CBEB7db8a08'
Alice_account= '0xdEB4A949aF09d112Cc31b41A93f5DDb56d937e7a'

nonce = web3_ganache_connection.eth.get_transaction_count(Loba_account)
transaction_data = {
    'nonce': nonce,
    'to': Alice_account,
    'value': web3_ganache_connection.to_wei(20, 'ether'),
    'gas': 22000,
    'gasPrice': web3_ganache_connection.to_wei(10, 'gwei')
}

private_key = '0x716340d8271b07c270b99e51680a95121f0a9e29e5abd1882b3ad7c13f808439'
signed_transaction = web3_ganache_connection.eth.account.sign_transaction(transaction_data, private_key)
transaction_hash = web3_ganache_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash))