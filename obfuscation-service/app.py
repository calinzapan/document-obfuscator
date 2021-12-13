from flask import Flask, request
from PIL import Image
import numpy as np
import io
import base64
import random, sys
app = Flask(__name__)

labels = {
  "photo": [42, 250, 780, 1130],
  "serial": [1483, 300, 1613, 371],
  "number": [1727, 300, 1980, 371], 
  "cnp": [900, 378, 1483, 450],
  "lastName": [789, 518, 1980, 600], 
  "firstName": [789, 648, 1980, 730],
  "nationality": [789, 778, 1980, 860], 
  "placeOfBirth": [789, 908, 1980, 990],
  "address": [789, 1038, 2250, 1215], 
  "issuedBy": [789, 1260, 1483, 1350],
  "valability": [1727, 1258, 2470, 1348],
  "barCode": [100, 1380, 2430, 1680]
}

def isBase64(function):
  def wrapper(arg1):
    try:
      if isinstance(arg1, str):
        sb_bytes = bytes(arg1, 'ascii')
      elif isinstance(arg1, bytes):
        sb_bytes = arg1
      else:
        raise ValueError("Argument must be string or bytes")

      decoded = base64.b64decode(sb_bytes)
      if base64.b64encode(decoded) == sb_bytes:
        return function(decoded)
    except Exception:
      return False
  return wrapper

def encode(function):
  def wrapper(arg1):
    arrays = function(arg1)
    buff = io.BytesIO()
    IMAGE_ENCRYPTED = Image.fromarray(arrays[0].astype("uint8"))

    buff.flush()
    IMAGE_KEY = Image.fromarray(arrays[1])
    buff.seek(0)
    IMAGE_KEY.save(buff, format="PNG")
    B64_IMAGE_KEY = base64.b64encode(buff.getvalue()).decode("utf-8")

    return {
      'pictureUrl': IMAGE_ENCRYPTED,
      'key': B64_IMAGE_KEY
    }
  return wrapper

@encode
def obfuscateImage(image):
  img_arr = np.array(Image.open(io.BytesIO(image)))
  img_rows = img_arr.shape[0]
  img_cols = img_arr.shape[1]
  IMAGE_KEY = Image.new("RGB", (img_cols, img_rows), "white")
  key_arr = np.array(IMAGE_KEY)
  for i in range(img_rows):
    for j in range(img_cols):
      for k in range(3):
        key_arr[i][j][k] = random.randint(0, 255)
        img_arr[i][j][k] = int(img_arr[i][j][k]) ^ int(key_arr[i][j][k])
    
  return [img_arr, key_arr]
  

@app.route('/')
def index():
  return 'Server Works!'

@app.route('/obfuscate', methods=['POST'])
def obfuscate():
  json_data = request.get_json(force=True)
  pictureUrl = json_data['pictureUrl']
  if isinstance(pictureUrl, str):
    sb_bytes = bytes(pictureUrl, 'ascii')
  elif isinstance(pictureUrl, bytes):
    sb_bytes = pictureUrl
  
  decoded_image = base64.b64decode(sb_bytes)
  img = Image.open(decoded_image).convert('RGB')
  # left corner of the photo
  xCI = 0
  yCI = 0
  labelKeys = {}
  for key, value in labels.items():
    crpImg = img.crop((xCI + value[0], yCI + value[1], xCI + value[2], yCI + value[3]))
    obfuscateResult = obfuscateImage(crpImg)
    img.paste(obfuscateResult[0], (xCI + value[0], yCI + value[1]))
    labelKeys[key] = obfuscateResult[1]

  # go through dictionary of coordinates here and call obfuscateImage for every zone
  # paste the the encrypted zone back to the original photo
  # save the key in a object, associated with the label
  return [labelKeys, img]
  
@app.route('/deobfuscate', methods=['POST'])
def deobfuscate():
  json_data = request.get_json(force=True)
  imgdata = base64.b64decode(json_data['pictureUrl'])
  keydata = base64.b64decode(json_data['key'])
  img_arr = np.array(Image.open(io.BytesIO(imgdata)))
  key_arr = np.array(Image.open(io.BytesIO(keydata)))
  
  img_rows = img_arr.shape[0]
  img_cols = img_arr.shape[1]
  for i in range(img_rows):
    for j in range(img_cols):
      for k in range(3):
        img_arr[i][j][k] = int(img_arr[i][j][k]) ^ int(key_arr[i][j][k])

  buff = io.BytesIO()
  IMAGE_DECRYPTED = Image.fromarray(img_arr)
  IMAGE_DECRYPTED.show()
  IMAGE_DECRYPTED.save(buff, format="PNG")
  B64_IMAGE_DECRYPTED = base64.b64encode(buff.getvalue()).decode("utf-8")
  return {
    'pictureUrl': B64_IMAGE_DECRYPTED,
  }
