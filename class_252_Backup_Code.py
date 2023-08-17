from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

loba_account = '0x0beB512761956A3520700061Ae72C71D726810b0'
james_account = '0x81dE5ef025742a4a8B69860504E6aCa0cc2F8B77'
private_key = '0xa2f674cb39f1f7f90998fd7b51696a2f22c040c43075fcc725abd3b824c9a7bb'

nonce = web3.eth.get_transaction_count(loba_account)

tx = {
    'nonce': nonce,
    'to': james_account,
    'value': web3.to_wei(6, 'ether'),
    'gas': 21000,
    'gasPrice': web3.to_wei(125, 'gwei')
}

signed_tx = web3.eth.account.sign_transaction(tx, private_key)
transaction_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

print(web3.to_hex(transaction_hash))
