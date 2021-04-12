import cv2
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


def showData(image):

  binary_data = ""
  for values in image:
      for pixel in values:
          r, g, b, a = messageToBinary(pixel) 
          binary_data += r[-1] 
          binary_data += g[-1] 
          binary_data += b[-1] 
          binary_data += a[-1] 
 
  all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]

  decoded_data = ""
  for byte in all_bytes:
      decoded_data += chr(int(byte, 2))
      if decoded_data[-5:] == "#####": 
          break
  return decoded_data[:-5] 

def decode_text():
  image_name = input("Enter the name of the steganographed image that you want to decode (with extension) :") 
  image = cv2.imread(image_name, cv2.IMREAD_UNCHANGED)
    
  text = showData(image)
  return text