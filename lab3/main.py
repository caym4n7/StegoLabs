import cv2
import numpy as np
import types
from encode import encode_text 
from decode import decode_text


def Steganography(): 
    userinput = int(input("Image Steganography \n 1. Encode the data \n 2. Decode the data \n 3. Exit \n Choose mode: "))
    
    if userinput == 1:
      print("\nEncoding....")
      encode_text() 
          
    elif userinput == 2:
      print("\nDecoding....") 
      print("Decoded message is " + decode_text()) 
    
    elif userinput == 3:
      print("Bye!....")

    else: 
        raise Exception("Enter correct input \n 1. Encode the data \n 2. Decode the data \n 3. Exit") 
          
Steganography() 