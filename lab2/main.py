from encode import encode
from decode import decode

def Steganography(): 
    userinput = int(input("Text Steganography \n 1. Encode the data \n 2. Decode the data \n 3. Exit \nChoose mode: "))

    if userinput == 1:
      print("\nEncoding....")
      encode() 
          
    elif userinput == 2:
      print("\nDecoding....") 
      decode()

    elif userinput == 3:
    	print("\nBye!....")

    else: 
        raise Exception("Enter correct input \n 1. Encode the data \n 2. Decode the data \n 3. Exit") 
          
Steganography() 