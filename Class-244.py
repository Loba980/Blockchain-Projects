from web3 import Web3
from web3.middleware import geth_poa_middleware

API_url = 'https://mainnet.infura.io/v3/77e6c2055f524fbb98863331f694ce50'
web3 = Web3(Web3.HTTPProvider(API_url))

#w3 = Web3(Web3.IPCProvider())
Block_data = w3.eth.getBlock('13054520')


transaction = web3.eth.get_transaction('0x8c60f6fe8d8f795692016212f1db5e0ddbd83e958cb0899b68a611881b4a1cde') 
print('blockHash:', transaction['blockHash'].hex())
print('blockNumber:', transaction['blockNumber'])
print('from:', transaction['from'])
print('gas:', transaction['gas'])
print('gasPrice in ether:', transaction['gasPrice'])
print('hash:', transaction['hash'].hex())
print('input:', transaction['input'])
print('nonce:', transaction['nonce'])
print('signature:', transaction['s'].hex())
print('to:', transaction['to'])
print('value:', transaction['value'])