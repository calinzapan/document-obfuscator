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

def paste(x1: int, y1: int, fieldName: str):
    im1 = Image.open('result.jpg')
    im2 = Image.open(fieldName + '.jpg')
    back_im = im1.copy()
    back_im.paste(im2, (xCI + x1, yCI + y1))
    back_im.save('result.jpg')

crop(8, 73, 231, 398, "photo.jpg")
# crop(456, 95, 488, 111, "serial.jpg")
# crop(524, 95, 661, 111, "number.jpg")
# crop(273, 112, 451, 135, "cnp.jpg")
# crop(238, 150, 458, 172, "lastName.jpg")
# crop(238, 190, 650, 212, "firstName.jpg")
# crop(238, 230, 362, 252, "nationality.jpg")
# crop(238, 270, 568, 292, "placeOfBirth.jpg")
# crop(238, 308, 733, 353, "address.jpg")
# crop(238, 376, 479, 400, "issuedBy.jpg")
# crop(556, 375, 778, 402, "valability.jpg")
# crop(27, 411, 760, 498, "barCode.jpg")
img.save("result.jpg")

# TODO Obfuscare

# paste(238, 150, 'lastName')
# paste(238, 190, 'firstName')

