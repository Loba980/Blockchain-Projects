import hashlib
import json
from time import time

chain = []

def block(proof, previous_hash=None):
	transaction={
	'sender': 'Loba',
	'recipient': 'Bob',
	'amount' : '2 ETH'
	}

	data={
	'index' : 1,
	'timestamp' : time(),
	'transactions' : transaction,
	'gas/fee' : 0.63,
	'proof' : proof,
	'previous_hash' : previous_hash
	}

	chain.append(block)
	print('Block Information: ', data)
	string_object = json.dumps(data)
	block_string = string_object.encode()

	raw_hash = hashlib.sha256(block_string)
	hex_hash = raw_hash.hexdigest()
	print("Hash code of the block: ", hex_hash)

block(previous_hash="There is no previous hash since this is the first blick created.", proof=000)