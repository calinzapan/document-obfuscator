# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import PIL, sys

# print sys.version, PIL.VERSION

img = Image.open("demo.jpg").convert('RGB')
draw = ImageDraw.Draw(img)
xCI = 0
yCI = 0
def crop(x1: int, y1: int, x2: int, y2: int, fileName: str):
    crp = img.crop((xCI + x1, yCI + y1, xCI + x2, yCI + y2))
    crp.save(fileName)
    draw.line((xCI + x1, (yCI * 2 + y1 + y2) / 2, xCI + x2, (yCI * 2 + y1 + y2) / 2), 0, y2 - y1)

def paste(x1: int, y1: int, fieldName: str):
    im1 = Image.open('result.jpg')
    im2 = Image.open(fieldName + '.jpg')
    back_im = im1.copy()
    back_im.paste(im2, (xCI + x1, yCI + y1))
    back_im.save('result.jpg')

crop(42, 250, 780, 1130, "photo.jpg")
crop(1483, 300, 1613, 371, "serial.jpg")
crop(1727, 300, 1980, 371, "number.jpg")
crop(900, 378, 1483, 450, "cnp.jpg")
crop(789, 518, 1980, 600, "lastName.jpg")
crop(789, 648, 1980, 730, "firstName.jpg")
crop(789, 778, 1980, 860, "nationality.jpg")
crop(789, 908, 1980, 990, "placeOfBirth.jpg")
crop(789, 1038, 2250, 1215, "address.jpg")
crop(789, 1260, 1483, 1350, "issuedBy.jpg")
crop(1727, 1258, 2470, 1348, "valability.jpg")
crop(100, 1380, 2430, 1680, "barCode.jpg")
img.save("result.jpg")

# TODO Obfuscare

# paste(238, 150, 'lastName')
# paste(238, 190, 'firstName')


# import cv2
  
# # function to display the coordinates of
# # of the points clicked on the image
# def click_event(event, x, y, flags, params):
 
#     # checking for left mouse clicks
#     if event == cv2.EVENT_LBUTTONDOWN:
 
#         # displaying the coordinates
#         # on the Shell
#         print(x, ' ', y)
 
#         # displaying the coordinates
#         # on the image window
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         cv2.putText(img, str(x) + ',' +
#                     str(y), (x,y), font,
#                     1, (255, 0, 0), 2)
#         cv2.imshow('image', img)
 
#     # checking for right mouse clicks    
#     if event==cv2.EVENT_RBUTTONDOWN:
 
#         # displaying the coordinates
#         # on the Shell
#         print(x, ' ', y)
 
#         # displaying the coordinates
#         # on the image window
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         b = img[y, x, 0]
#         g = img[y, x, 1]
#         r = img[y, x, 2]
#         cv2.putText(img, str(b) + ',' +
#                     str(g) + ',' + str(r),
#                     (x,y), font, 1,
#                     (255, 255, 0), 2)
#         cv2.imshow('image', img)
 
# # driver function
# if __name__=="__main__":
 
#     # reading the image
#     img = cv2.imread('demo.jpg', 1)
 
#     # displaying the image
#     cv2.imshow('image', img)
 
#     # setting mouse handler for the image
#     # and calling the click_event() function
#     cv2.setMouseCallback('image', click_event)
 
#     # wait for a key to be pressed to exit
#     cv2.waitKey(0)
 
#     # close the window
#     cv2.destroyAllWindows()
