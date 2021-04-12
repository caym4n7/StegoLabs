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

def hideData(image, secret_message):
  n_bytes = image.shape[0] * image.shape[1] * 3 // 8
  print("Maximum bytes to encode:", n_bytes)

  if len(secret_message) > n_bytes:
      raise ValueError("Error encountered insufficient bytes, need bigger image or less data !!")
  
  secret_message += "#####"

  data_index = 0
  
  binary_secret_msg = messageToBinary(secret_message)
  data_len = len(binary_secret_msg)
  
  for values in image:
      for pixel in values:
          r, g, b, a = messageToBinary(pixel)

          if data_index < data_len:
              pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
              data_index += 1
          
          if data_index < data_len:
              pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
              data_index += 1
          
          if data_index < data_len:
              pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
              data_index += 1
          
          if data_index < data_len:
              pixel[3] = int(a[:-1] + binary_secret_msg[data_index], 2)
              data_index += 1

          if data_index >= data_len:
              break

  return image

def encode_text(): 
  image_name = input("Enter image name (with extension): ") 
  image = cv2.imread(image_name, cv2.IMREAD_UNCHANGED)
   
  data = input("Enter data to be encoded : ") 
  if (len(data) == 0): 
    raise ValueError('Data is empty')
  
  filename = input("Enter the name of new encoded image (with extension): ")
  encoded_image = hideData(image, data)
  cv2.imwrite(filename, encoded_image)