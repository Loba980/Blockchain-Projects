import hashlib
import json
from time import time

chain = []

def block(proof, previous_hash=None):
	transaction={
	'sender': 'Satoshi',
	'recipient': 'Mike',
	'amount' : '5 ETH'
	}

	data={
	'Block Height' : 782349,
	'Timestamp' : time(),
	'Transactions' : transaction,
	'Block Reward' : '0.956324 (4MINERS: PPLNS) in 2hrs 31mins',
	'Uncles Reward': 2,
	'Difficulty' : '4.782.903',
	'Total Difficulty' : '8.423.046.981',
	'Size' : '2.38 Gigabytes',
	'Gas Used' : '7.292.349 (62.30%)',
	'Gas Limit' : '10.539.697'
	}

	chain.append(block)
	print('Block Information: ', data)
	json_data = json.dumps(data)
	encoded_data = json_data.encode()\

	sha256_data = hashlib.sha256(encoded_data)
	hexed_data = sha256_data.hexdigest()
	print("Hash code of the block: ", hexed_data)

block(previous_hash="There is no previous hash since this is the first blick created.", proof=000)