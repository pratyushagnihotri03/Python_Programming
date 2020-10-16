from PIL import Image

wheel = Image.open("wheel.jpg")
wow = Image.open("wow.png")

area = (100, 100, 300, 300)
wheel.paste(wow, area)

wheel.show()