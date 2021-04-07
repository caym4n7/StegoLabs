f = open("encoded_message.txt", "r", encoding='utf-8')
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

decoded_message = ''.join(codes)

def BinaryToDecimal(binary):  
	string = int(binary, 2)
	return string

print("Decoded message binary:", decoded_message)
   
str_data =' '
   
for i in range(0, len(decoded_message), 8):
    temp_data = decoded_message[i:i + 8]
    decimal_data = BinaryToDecimal(temp_data)
    str_data = str_data + chr(decimal_data) 
  
print("Decoded message:", str_data)