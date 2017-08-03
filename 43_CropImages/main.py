'''
Pillow lib for playing with images
'''
from PIL import Image


img = Image.open("mummy.jpg")
print(img.size)
print(img.format)

area = (100,100, 300, 375)
cropped_img = img.crop(area)

img.show()
cropped_img.show()