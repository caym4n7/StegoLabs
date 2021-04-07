f = open("encoded_message.txt", "r")
encoded_message = f.read()
f.close()	

ukrLet = "асеіорхАВСЕНІКОРТХ"
engLet = "aceiopxABCEHIKOPTX"

codes = []
code = ''

for char in encoded_message:
	if len(code) == 8:
		if code == "00000000":
			break
		codes.append(code)
		code = ""
	if char in engLet:
		code += "1"
	elif char in ukrLet:
		code += "0"

#decoded_message = ''.join(codes)
#print(decoded_message)

print(codes)


