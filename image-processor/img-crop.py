# -*- coding: utf-8 -*-

from PIL import Image
import PIL, sys

# print sys.version, PIL.VERSION

im = Image.open("demo.jpg")
region = im.crop((200, 200, 300, 300))
region.save("region.sample3.jpg")
