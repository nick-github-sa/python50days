import random
import string

def generate_password():
    strength = input("How strong do you want your password to be? (weak/strong/very strong) ")
    if strength == "weak":
        length = 5
    elif strength == "strong":
        length = 8
    elif strength == "very strong":
        length = 12
    else:
        print("Invalid input. Please choose from 'weak', 'strong', or 'very strong'.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_password())