from web3 import Web3
import json
import requests

infura_url = 'https://mainnet.infura.io/v3/77e6c2055f524fbb98863331f694ce50'
web3 = Web3(Web3.HTTPProvider(infura_url))

req_ethgas_data = requests.get('https://ethgasstation.info/json/ethgasAPI.json')
trans_info = json.loads(req_ethgas_data.content)

print('Safe Low', trans_info['safeLow'])
print('Average', trans_info['average'])
print('Fast', trans_info['fast'])
print('Fastest', trans_info['fastest'])
print('Block Number', trans_info['blockNum'])

gas_price = web3.eth.gas_price
print('Calculated Gas Price: ', gas_price/10**9)