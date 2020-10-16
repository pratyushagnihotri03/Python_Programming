'''
Pillow lib for playing with images
'''
from PIL import Image


img = Image.open("mummy.jpg")
print(img.size)
print(img.format)

img.show()