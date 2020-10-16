from PIL import Image


wow = Image.open("WoW.png")
r, g, b = wow.split()

r.show()
g.show()
b.show()
