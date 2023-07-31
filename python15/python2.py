names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}

def your_age():
    user_input = input("Please type in your name - \n").lower()
    if user_input in names_age:
        age = names_age[user_input]
        print("Hi", user_input.capitalize(), "you are", age, "years old!")
    else:
        print("Your name is not in the dictionary")
        user_age = int(input("Please enter your age - \n"))
        names_age.update({user_input : user_age})
        if user_input in names_age:
            age = names_age[user_input]
            print("Hi", user_input.capitalize(), "you are", age, "years old!")

your_age()
