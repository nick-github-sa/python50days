import random

def user_name():
    name = input("Please enter your name - \n")
    name_rev = (name[::-1].lower() + str(random.randint(0,10)))
    return name_rev

print(user_name())