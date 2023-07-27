for nonce in range(0,5): # set a range for iteration
	equation = 25-5+nonce
	if equation == 24:
		print('Your nonce was verified and the number required was 4.') #display as "verified" and mention the nonce value at which it got verified. 
		break
	else:
		print('Sorry, the inserted nonce is not verified')#display as " not verified"





