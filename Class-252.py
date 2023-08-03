from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

account1 = '0x86A19cd6b8923eBA24835EE3af0d9E400453CA42'
account2 = '0xBa1b815Cd041Ab08F224D624c57517FB06425611'

private_key = '0x508457eada495bd9eec2dc49e33e8fd64f1c4a3043b71822417a11d32909e2bf'
nonce = web3.eth.get_transaction_count(account1)

tx = {
    'nonce': nonce,
    'to': account2,
    'value': web3.to_wei(1, 'ether'),
    'gas': 21000,
    'gasPrice': web3.to_wei(50, 'gwei')
}

signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

print(web3.to_hex(tx_hash))