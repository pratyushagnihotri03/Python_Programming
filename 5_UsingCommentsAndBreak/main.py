# Single Line Comment
print('using Comments and Break:')
magicNumber = 26
'''
Multiline comments
author: Pratyush
'''

for n in range(101):
    if n is magicNumber:
        print(n, "is the magic number !")
        break
    else:
        print(n)


for n in range(100):
    if n%4:
        print(n, "is divisible by 4 :)")
    else:
        print(n, "is not divisible by 4 :(")