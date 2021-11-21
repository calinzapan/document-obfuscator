from flask import Flask, request
from PIL import Image
import numpy as np
import io
import base64
import random, sys
app = Flask(__name__)

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
    buff.seek(0)
    IMAGE_ENCRYPTED.save(buff, format="PNG")
    B64_IMAGE_ENCRYPTED = base64.b64encode(buff.getvalue()).decode("utf-8")

    buff.flush()
    IMAGE_KEY = Image.fromarray(arrays[1])
    buff.seek(0)
    IMAGE_KEY.save(buff, format="PNG")
    B64_IMAGE_KEY = base64.b64encode(buff.getvalue()).decode("utf-8")

    return {
      'pictureUrl': B64_IMAGE_ENCRYPTED,
      'key': B64_IMAGE_KEY
    }
  return wrapper

@encode
@isBase64
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
  return obfuscateImage(pictureUrl)
  
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
