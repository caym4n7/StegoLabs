f = open("container.txt", "r")
text_container = f.read()
f.close()

secret_message = "hello"

onespace = " "
twospace = "  "

encoded_message = ""

wordList = text_container.split() 

def str2bin():
	binary_secret = ' '.join(format(ord(x), 'b') for x in secret_message)
	split_binary_secret = "".join(binary_secret.split()) # remove whitespaces
	return split_binary_secret

print(str2bin())

split_binary_secret = str2bin()

def encode_message(split_binary_secret, encoded_message):
	for i in range(len(split_binary_secret)):
		if split_binary_secret[i] == '1':
			encoded_message += wordList[i] + twospace
		else:
			encoded_message += wordList[i] + onespace
	return encoded_message

print(encode_message(split_binary_secret, encoded_message))

