def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

my_dating_limit = allowed_dating_age(27)
print("Pratyush can date girls", my_dating_limit, "or older")

my_brother_dating_limit = allowed_dating_age(25)
print("Brother can date girls", my_brother_dating_limit, "or older")