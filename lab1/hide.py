f = open("container.txt", "r")
text_container = f.read()
f.close()

secret_message = "hello"

onespace = " "
twospace = "  "

encoded_message = ""

wordList = text_container.split() 

def str2bin():
	binary_secret = ' '.join(format(ord(x), '08b') for x in secret_message)
	return binary_secret

print(str2bin())

binary_secret = str2bin()

def encode_message(binary_secret, encoded_message):
	for i in range(len(binary_secret)):
		if binary_secret[i] == '1':
			encoded_message += wordList[i] + twospace
		else:
			encoded_message += wordList[i] + onespace
	return encoded_message

print(encode_message(binary_secret, encoded_message))

encoded_message = encode_message(binary_secret, encoded_message)

result = open("encoded_message.txt", "w")
result.write(encoded_message)
result.close()

