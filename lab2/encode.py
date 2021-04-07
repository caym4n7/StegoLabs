f = open("container.txt", "r" , encoding='utf-8')
text_container = f.read()
f.close()	

secret_message = input("Enter message: ")

ukrLet = "асеіорхАВСЕНІКОРТХ"
engLet = "aceiopxABCEHIKOPTX"

def str2bin():
	binSecret = ''.join(format(ord(x), '08b') for x in secret_message)	
	return binSecret

binSecret = str2bin()
print("Message Binary:", binSecret)

i = 0
letter = ''
encoded_message = ''

if len(binSecret) > len(text_container):
	raise Exception("Your text container is too small for this message!")

for char in text_container:
	if char in ukrLet:
		if i < len(binSecret):
			if str(binSecret[i]) == "1":
				index = ukrLet.index(char)
				letter = str(engLet[index])
			elif str(binSecret[i]) == "0":
				letter = char
			
			i += 1

		else:
			letter = char
	else:
		letter = char
	
	encoded_message += letter

print(encoded_message)

result = open("encoded_message.txt", "w", encoding='utf-8')
result.write(encoded_message)
result.close()
