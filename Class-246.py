from web3 import Web3
import json
import requests

infura_url = 'https://mainnet.infura.io/v3/77e6c2055f524fbb98863331f694ce50'
web31 = Web3(Web3.HTTPProvider(infura_url)) #establish the connection

req_ethgas_data = requests.get('https://ethgasstation.info/json/ethgasAPI.json') #get the data from the API in json format.
latest_block_info = json.loads(req_ethgas_data.content) # convert the json formatted data to normal data.

#access various costs of transactions depending upon the speed.
print('safeLow', latest_block_info['safeLow'])
print('average', latest_block_info['average'])
print('fast', latest_block_info['fast'])
print('fastest', latest_block_info['fastest'])
print('Block number:', latest_block_info['blockNum'])

gas_price = web31.eth.gas_price
gas_price_in_eth = gas_price/10**18
print('Gas price in ether:', gas_price_in_eth)
gas_price_in_dollar = gas_price_in_eth * 2,465.00
print("Gas price in dollars:", gas_price_in_dollar)

Block_data = web31.eth.get_block(17538341)
#print('Block data: '. Block_data)
lastest_trans = Block_data['transactions'][-1].hex()
print('Transaction hash data:', lastest_trans)
trans_info = web31.eth.get_transaction(lastest_trans)
gas_estimate = web31.eth.estimate_gas({'to': trans_info['to'], 'from': trans_info['from']})
print('Gas used in this transaction was: ', gas_estimate)
print('Your gas limit is: ', trans_info['gas'])