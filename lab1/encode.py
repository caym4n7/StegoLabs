import numpy as np
import types

def messageToBinary(message):
  if type(message) == str:
    return ''.join([ format(ord(i), "08b") for i in message ])
  elif type(message) == bytes or type(message) == np.ndarray:
    return [ format(i, "08b") for i in message ]
  elif type(message) == int or type(message) == np.uint8:
    return format(message, "08b")
  else:
    raise TypeError("Input type not supported")

def hideMessage(text_container, secret_message):
	encoded_message = ""
	wordList = text_container.split()
	binary_secret = messageToBinary(secret_message)
	print(binary_secret)

	if len(binary_secret) > len(wordList):
		raise Exception("Your text container is too small for this message!")

	for i in range(len(binary_secret)):
		if binary_secret[i] == '1':
			encoded_message += wordList[i] + "  "
		else:
			encoded_message += wordList[i] + " "
	
	return encoded_message

def encode():
	file_name = input("Enter text-file name (example.txt): ")

	f = open(file_name, "r")
	text_container = f.read()
	f.close()

	data = input("Enter your message to hide: ")

	if len(data) == 0:
		raise ValueError('Data is empty!')

	encoded_message = hideMessage(text_container, data)
	print(encoded_message)
	
	encoded_file_name = input("Enter the name of new encoded text (example.txt): ")
	result = open(encoded_file_name, "w")
	result.write(encoded_message)
	result.close()


