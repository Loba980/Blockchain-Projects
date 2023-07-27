#import the Web3 module from Web3 library
from web3 import Web3
#Task 1
url = 'https://mainnet.infura.io/v3/77e6c2055f524fbb98863331f694ce50'
web3 = Web3(Web3.HTTPProvider(url))
#Task 2
latest_block = web3.eth.getBlock(13054520)
print('Latest Block of Ethereum Blockchain: ', latest_block)
#Task 3
block_transaction_count = get_block_transaction_count(13054520)
print('Number of transactions happened in the block: ', block_transaction_count)
#Task 4
Transaction_fee = fee_history(Block_count=1000, Newest_block='latest', Reward_percentiles=None)
print('Number of transactions happened in the block: ', Transaction_fee)