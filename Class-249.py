import hashlib
PB_current_hash = "573de6af99199bdc7ae9534891d512afbc2b1473f2f6a5784e0c078d67a60bf9"

str = 'Loba sends James 5 Eth amount'

result= hashlib.sha256(str.encode())
CB_previous_hash = result.hexdigest()

if PB_current_hash == CB_previous_hash:
	print('Hash has been vertified!')
else:
	print('Hash was not vertified...')