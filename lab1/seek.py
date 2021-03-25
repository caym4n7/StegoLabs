f = open("encoded_message.txt", "r")
encoded_message = f.read()
f.close()

code = ""

x = 0 

def decode_message(code, x):
	for i in range(len(encoded_message)):
		if x+1 < len(encoded_message):
			if encoded_message[x] + encoded_message[x+1] == "  ":
				code = code + "1"
				x = x+2
			elif encoded_message[x] == " ":
				code = code + "0"
		x += 1
	return code	

decode_message(code, x)

def BinaryToDecimal(binary):  
	string = int(binary, 2)
	return string
      
bin_data = decode_message(code, x)
   
print("The binary value is:", bin_data)
   
str_data =' '
   
for i in range(0, len(bin_data), 8):
    temp_data = bin_data[i:i + 8]
    decimal_data = BinaryToDecimal(temp_data)
    str_data = str_data + chr(decimal_data) 
  
print("decoded message:", str_data)