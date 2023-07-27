import hashlib
import json
from time import time

class Chain:
	def __init__(self):
		self.count = 0
		self.new_transactions = []
		self.chain = []
		self.new_block('No Previous Hash since this is the Gensis Block')
		
	def new_block(self, previous_hash=None):
		block={
		'count' : self.count,
		'timestamp' : time(),
		'transactions' : self.new_transactions or 'No transaction have been made since this is the Genesis Block',
		'gasfee' : 0.30,
		'previous_hash' : previous_hash
		}

		self.count =  self.count + 1
		self.chain.append(block)
		string_object = json.dumps(block)
		string_data = string_object.encode()

		raw_hash = hashlib.sha256(string_data)
		hex_data = raw_hash.hexdigest()
		self.chain.append(('current_hash: ', hex_data))
		return block

blockchain = Chain()

print(blockchain.chain)
