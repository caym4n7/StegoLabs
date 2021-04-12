import cv2
import numpy as np
import types
from encode import *
from decode import *


def Steganography(): 
    a = input("Image Steganography \n 1. Encode the data \n 2. Decode the data \n 3. Exit \n Choose mode (1 or 2): ")
    userinput = int(a)
    if (userinput == 1):
      print("\nEncoding....")
      encode_text() 
          
    elif (userinput == 2):
      print("\nDecoding....") 
      print("Decoded message is " + decode_text()) 
    
    elif (userinput == 3):
      break

    else: 
        raise Exception("Enter correct input") 
          
Steganography()