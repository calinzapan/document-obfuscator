# # -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import PIL, sys

# print sys.version, PIL.VERSION

img = Image.open("demo.jpg")
draw = ImageDraw.Draw(img)
xCI = 58
yCI = 140
def crop(x1: int, y1: int, x2: int, y2: int, fileName: str):
    crp = img.crop((xCI + x1, yCI + y1, xCI + x2, yCI + y2))
    crp.save(fileName)
    draw.line((xCI + x1, (yCI * 2 + y1 + y2) / 2, xCI + x2, (yCI * 2 + y1 + y2) / 2), 0, y2 - y1)

crop(8, 73, 231, 398, "photo.jpg")
crop(456, 95, 488, 111, "serial.jpg")
crop(524, 95, 661, 111, "number.jpg")
crop(273, 112, 451, 135, "cnp.jpg")
crop(238, 150, 458, 172, "lastName.jpg")
crop(238, 190, 650, 212, "firstName.jpg")
crop(238, 230, 362, 252, "nationality.jpg")
crop(238, 270, 568, 292, "placeOfBirth.jpg")
crop(238, 308, 733, 353, "address.jpg")
crop(238, 376, 479, 400, "issuedBy.jpg")
crop(556, 375, 778, 402, "valability.jpg")
crop(27, 411, 760, 498, "barCode.jpg")
img.save("test.jpg")

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