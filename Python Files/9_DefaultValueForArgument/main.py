'''
Author: Pratyush
Description: Passing default argument
'''

def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = 'Female'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()