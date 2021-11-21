from PIL import Image

import numpy as np

import random, sys
import io
import base64

MODE = sys.argv[1].lower()
IMAGE_SOURCE = Image.open(sys.argv[2])

img_arr = np.array(IMAGE_SOURCE)
img_rows = img_arr.shape[0]
img_cols = img_arr.shape[1]

buff = io.BytesIO()
b64 = Image.fromarray(img_arr)
b64.save(buff, format="PNG")
print(base64.b64encode(buff.getvalue()).decode("utf-8"))

original_stdout = sys.stdout # Save a reference to the original standard output

with open('filename.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(base64.b64encode(buff.getvalue()).decode("utf-8"))
    sys.stdout = original_stdout # Reset the standard output to its original value

if MODE == "e" or MODE == "encrypt":
	IMAGE_KEY = Image.new("RGB", (img_cols, img_rows), "white")
	key_arr = np.array(IMAGE_KEY)
	for i in range(img_rows):
		for j in range(img_cols):
			for k in range(3):
				key_arr[i][j][k] = random.randint(0, 255)
				img_arr[i][j][k] = int(img_arr[i][j][k]) ^ int(key_arr[i][j][k])
				
	IMAGE_ENCRYPTED = Image.fromarray(img_arr)
	IMAGE_KEY = Image.fromarray(key_arr)
	IMAGE_ENCRYPTED.save("encrypted.png")
	IMAGE_KEY.save("key.png")

if MODE == "d" or MODE == "decrypt":
  IMAGE_KEY = Image.open(sys.argv[3])
  key_arr = np.array(IMAGE_KEY)

  for i in range(img_rows):
    for j in range(img_cols):
      for k in range(3):
        img_arr[i][j][k] = int(img_arr[i][j][k]) ^ int(key_arr[i][j][k])
				
  IMAGE_DECRYPTED = Image.fromarray(img_arr)
  IMAGE_DECRYPTED.show()
  IMAGE_DECRYPTED.save("decrypted.png")
