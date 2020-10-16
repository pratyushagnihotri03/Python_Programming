from PIL import Image

mummy = Image.open("mummy.jpg")
family = Image.open("family.jpg")
r1, g1, b1 = mummy.split()#
r2, g2, b2 = family.split()
mummy_image = Image.merge("RGB", (b1, g1, r1))
family_image = Image.merge("RGB", (b2, g2, r2))
Comb_family_mummy = Image.merge("RGB", (b2, g2, r1))

mummy_image.show()
family_image.show()
Comb_family_mummy.show()


