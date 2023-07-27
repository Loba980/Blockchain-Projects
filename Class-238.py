import hashlib

text_1="Joe gave 50 dollars to Max"
result= hashlib.sha3_256(text_1.encode())
print("The first SHA256 is: ", result.hexdigest())

text_2="Joe gave 350 dollars to Johnny"
result= hashlib.sha3_256(text_2.encode())
print("The second SHA256 is: ", result.hexdigest())

text_3="Max gave 20 dollars to Johnny"
result= hashlib.sha3_256(text_3.encode())
print("The third SHA256 is: ", result.hexdigest())

text_4="Loba had 45 dollars"
result= hashlib.sha3_256(text_4.encode())
print("The fourth SHA256 is: ", result.hexdigest())

text_5="I put 20 dollars into my bank account"
result= hashlib.sha3_256(text_5.encode())
print("The fifth SHA256 is: ", result.hexdigest())