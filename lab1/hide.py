f = open("container.txt", "r")
text = f.read()

secret = "hello"

onespace = " "
twospace = "  "

result = ""

# str to bin
a = ' '.join(format(ord(x), 'b') for x in secret)
binc = "".join(a.split()) # remove whitespaces
print(binc)

# list of words
wordList = text.split() 


for i in range(len(binc)):
	if binc[i] == '1':
		result += wordList[i] + twospace
	else:
		result += wordList[i] + onespace

print(result)

