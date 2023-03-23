#!/usr/bin/python3

from PIL import Image, ImageFilter
im = Image.open("rat.png")
im2 = im.rotate(45, resample=Image.BICUBIC, expand=True)
im2.save("rat_rotated.png")
