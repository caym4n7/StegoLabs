def seekMessage(encoded_message):

	code = ""
	x = 0 

	for i in range(len(encoded_message)):
		if x+1 < len(encoded_message):
			if encoded_message[x] + encoded_message[x+1] == "  ":
				code = code + "1"
				x = x+2
			elif encoded_message[x] == " ":
				code = code + "0"
		x += 1
	return code	

def BinaryToDecimal(binary):  
	string = int(binary, 2)
	return string      
  
def DecimalToString(encoded_message):

	bin_data = seekMessage(encoded_message)
	str_data =' '
	   
	for i in range(0, len(bin_data), 8):
	    temp_data = bin_data[i:i + 8]
	    decimal_data = BinaryToDecimal(temp_data)
	    str_data += chr(decimal_data) 
	  
	print("Message found!:", str_data)

def decode():
	encoded_file_name = input("Enter text-file name (example.txt): ")
	f = open(encoded_file_name, "r")
	encoded_message = f.read()
	f.close()

	decoded_message = DecimalToString(encoded_message)



