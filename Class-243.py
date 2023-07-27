from web3 import Web3
from web3.middleware import geth_poa_middleware

API_url = 'https://mainnet.infura.io/v3/ec5acb1175dc468c9f3ee9a84a02fe98'
web3 = Web3(Web3.HTTPProvider(API_url))

Block_data = web3.eth.get_block(12964964)
print('Block Data: ', Block_data)

print('Gas Used: ', Block_data ['gasUsed'])
print('Total difficulty: ', Block_data ['difficulty'])

print('Transaction Data: ', Block_data ['transactions'])
transaction = web3.eth.get_transaction('0x00eef1396c5721eb7886b9f6befa2a9a97dd0c7bee13fe8eca8c48fb2328ab80')
print('Data: ', transaction)