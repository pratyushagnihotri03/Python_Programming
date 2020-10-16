from PIL import Image
from PIL import ImageFilter


baby = Image.open("baby.jpg")
colored = baby.convert("RGB")
black_white = baby.convert("L")  # L stands for black and white
blur = baby.filter(ImageFilter.BLUR)
detail =  baby.filter(ImageFilter.DETAIL)
edges =  baby.filter(ImageFilter.FIND_EDGES)


colored.show()
black_white.show()
blur.show()
detail.show()
edges.show()
