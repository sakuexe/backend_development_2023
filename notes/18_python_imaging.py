"""
    Python Imaging Library (Pillow)
    ---
    A free and open-source library, initially released in 1995
    - Supports loading and saving into lots of different image formats
    - Per-pixel manipulations, masking, transparency
    - Image filtering, such as blurring or edge finding
    - Image enhancing, such as sharpening or adjusting brightness, contrast
    - Add text to images
    - Drawing
    - Never versions known as Pillow
    ---
    - Pillow (= latest Python Imaging Library) documentation
    https://pillow.readthedocs.io/en/stable/
    - Pillow Handbook
    https://pillow.readthedocs.io/en/latest/handbook/index.html
"""

# pip3 install pillow
from PIL import Image, ImageFilter

# Open an image and save it in another format
im = Image.open("./assets/rat.gif")  # open a GIF file
im.save("./assets/rat-2.png")  # PNG supports both P and RGB mode
im2 = im.convert("RGB")  # convert P mode image to RGB mode
im2.save("./assets/rat.jpg", quality=90, optimize=True)

# Resizing an image
im = Image.open("./assets/rat.png")
width, height = im.size
ratio = width / height
new_width = 640
new_height = new_width/ratio
im2 = im.resize((round(new_width), round(new_height)), Image.ANTIALIAS)
im2 = im.convert("RGB")  # convert RGBA to RGB
im2.save("./assets/rat_converted.jpg", quality=90, optimize=True)

from PIL import ImageFont, ImageDraw
# add text to an image
im = Image.open("./assets/rat.png")
draw = ImageDraw.Draw(im)
# use a ttf type font
font = ImageFont.truetype("./assets/Lollypop Free.ttf", 40)
draw.text((50, 25), "RAT MODE ACTIVATED", font=font, fill=(150, 0, 0))
im.save("./assets/rat_mode_active.png")

from PIL import ImageEnhance
# Enhance pictures
im = Image.open("./assets/rat.png")
enhancer = ImageEnhance.Contrast(im)
# im2 = enhancer.enhance(0.5)  # low contrast
im2 = enhancer.enhance(1.5)  # high contrast
enhancer = ImageEnhance.Color(im2)
im2 = enhancer.enhance(0)  # turn into black & white
# im2 = enhancer.enhance(1.5)  # 50 % more colorful
im2.save("./assets/rat_enhanced.png")

# Rotate the image
im = Image.open("./assets/rat.png")
im2 = im.rotate(45, resample=Image.BICUBIC, expand=True)
im2.save("./assets/rat_rotated.png")

# Filters
im = Image.open("./assets/rat.png")
# im2 = im.filter(ImageFilter.FIND_EDGES)  # Give "outlines"
# im2 = im.filter(ImageFilter.BLUR)  # Blurs the image
im2 = im.filter(ImageFilter.DETAIL)  # Sharpen the details, making them pop
# im2 = im.filter(ImageFilter.SHARPEN)  # More simplified sharpen (not as good)
im2.save("./assets/rat_filtered.png")

# Filter matrixes using Kernel
# kernel = ImageFilter.Kernel((3,3), [-2, -1, 0, 1, 1, 1, 0, 1, 2], 1)  # emboss (hand drawn)
# kernel = ImageFilter.Kernel((3,3), [0, 1, 0, 1, -4, 1, 0, 1, 0], 1)  # find edges
# kernel = ImageFilter.Kernel((3,3), [1, 1, 1, 1, 1, 1, 1, 1, 1], 1)  # blur
kernel = ImageFilter.Kernel((3,3), [1, 2, 1, 2, 4, 2, 1, 2, 1], 1)  # gaussian blur
im = Image.open("./assets/rat.png")
im2 = im.filter(kernel)
im2.save("./assets/rat_kerneled.png")
