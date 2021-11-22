# importing the module
import sys
from PIL import Image
import numpy as np
import cv2

from scipy import ndimage
# a = np.arange(12.).reshape((4, 3))
# print(ndimage.map_coordinates(a, [[0.5, 2], [0.5, 1]], order=1))
# MODE = sys.argv[1].lower()
IMAGE_SOURCE = Image.open("./demo.png")

img_arr = np.array(IMAGE_SOURCE)
print(img_arr)
print(ndimage.map_coordinates(img_arr, [[430, 656], [354, 367], [2,5]], order=1))
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
# 	img = cv2.imread('./demo.png', 1)
# 	cv2.imshow('image', img)
# 	cv2.setMouseCallback('image', click_event)
# 	cv2.waitKey(0)
# 	cv2.destroyAllWindows()

