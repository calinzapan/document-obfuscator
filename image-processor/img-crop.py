# # -*- coding: utf-8 -*-

from PIL import Image
import PIL, sys

# print sys.version, PIL.VERSION

im = Image.open("demo.jpg")
xCI = 58
yCI = 140
photo = im.crop((xCI + 8, yCI + 73, xCI + 231, yCI + 398))
photo.save("photo.jpg")
cnp = im.crop((xCI + 273, yCI + 112, xCI + 451, yCI + 135))
cnp.save("cnp.jpg")
lastName = im.crop((xCI + 238, yCI + 154, xCI + 458, yCI + 172))
lastName.save("lastName.jpg")
firstName = im.crop((xCI + 238, yCI + 194, xCI + 650, yCI + 212))
firstName.save("firstName.jpg")
nationality = im.crop((xCI + 238, yCI + 234, xCI + 362, yCI + 252))
nationality.save("nationality.jpg")
placeOfBirth = im.crop((xCI + 238, yCI + 274, xCI +  568, yCI + 292))
placeOfBirth.save("placeOfBirth.jpg")
address = im.crop((xCI + 238, yCI + 308, xCI + 733, yCI + 353))
address.save("address.jpg")
issuedBy = im.crop((xCI + 238, yCI + 376, xCI + 479, yCI + 400))
issuedBy.save("issuedBy.jpg")
valability = im.crop((xCI + 556, yCI + 365, xCI +  778, yCI + 402))
valability.save("valability.jpg")
barCode = im.crop((xCI + 27, yCI + 411, xCI + 760, yCI + 498))
barCode.save("barCode.jpg")




# # importing the module
# import sys
# from PIL import Image
# import numpy as np
# import cv2

# from scipy import ndimage
# # a = np.arange(12.).reshape((4, 3))
# # print(ndimage.map_coordinates(a, [[0.5, 2], [0.5, 1]], order=1))
# # MODE = sys.argv[1].lower()
# IMAGE_SOURCE = Image.open("./demo.jpg")

# img_arr = np.array(IMAGE_SOURCE)
# # print(img_arr)
# # print(ndimage.map_coordinates(img_arr, [[430, 656], [354, 367], [2,5]], order=1))
# def click_event(event, x, y, flags, params):
# 	if event == cv2.EVENT_LBUTTONDOWN:
# 		print(x, ' ', y)
# 		font = cv2.FONT_HERSHEY_SIMPLEX
# 		cv2.putText(img, str(x) + ',' +
# 					str(y), (x,y), font,
# 					1, (255, 0, 0), 2)
# 		cv2.imshow('image', img)
# 	if event==cv2.EVENT_RBUTTONDOWN:
# 		print(x, ' ', y)
# 		font = cv2.FONT_HERSHEY_SIMPLEX
# 		b = img[y, x, 0]
# 		g = img[y, x, 1]
# 		r = img[y, x, 2]
# 		cv2.putText(img, str(b) + ',' +
# 					str(g) + ',' + str(r),
# 					(x,y), font, 1,
# 					(255, 255, 0), 2)
# 		cv2.imshow('image', img)
# if __name__=="__main__":
# 	img = cv2.imread('./demo.jpg', 1)
# 	cv2.imshow('image', img)
# 	cv2.setMouseCallback('image', click_event)
# 	cv2.waitKey(0)
# 	cv2.destroyAllWindows()