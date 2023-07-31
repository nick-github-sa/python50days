import string
import random


def generate_password():
    
    a = string.printable
    weak = []
    print(a)
    password_strength = input("Please choose a 'weak', 'strong', or 'very strong' password - ")
    if password_strength == 'weak':
        strength = 5
    elif password_strength == 'strong':
        strength = 8
    else: 
        strength = 12
    
    for i in range(strength):
        if i == "/" or i == "' '" or i == "'\'" or i == '\n' or i == "\t":
            continue
        else:
            weak.append(random.choice(a))
    print(weak)
    print(''.join(weak))

generate_password()