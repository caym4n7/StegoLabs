# -*- coding: utf-8 -*-

f = open("container.txt", "r" , encoding='utf-8')
text_container = f.read()
f.close()	

ukrLet = "асеіорхАВСЕНІКОРТХ"
engLet = "aceiopxABCEHIKOPTX"

secret_message = "Its a me Mario"

def str2bin():
	binary_secret = ''.join(format(ord(x), '08b') for x in secret_message)	
	return binary_secret


binary_secret = str2bin()
print(binary_secret)

i = 0
letter = ''
encoded_message = ''

#for i in range(len(text_container)):
for char in text_container:
	if char in ukrLet:
		if i < len(binary_secret):
			if str(binary_secret[i]) == "1":
				index = ukrLet.index(char)
				print(index, char)
				letter = str(engLet[index])
			elif str(binary_secret[i]) == "0":
				letter = char
			
			i += 1

		else:
			letter = char
	else:
		letter = char
	
	encoded_message += letter

print(encoded_message)

result = open("encoded_message.txt", "w")
result.write(encoded_message)
result.close()
