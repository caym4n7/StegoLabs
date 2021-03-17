f = open("encoded_message.txt", "r")
encoded_message = f.read()
f.close()

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
print(code)