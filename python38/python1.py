import random

def guess_a_number():
    number_to_guess = random.randint(1, 10)
    print(number_to_guess)
    num_guesses = 0

    while num_guesses < 3:
        guess = int(input("Guess a number between 1 and 10: "))
        num_guesses += 1

        if guess == number_to_guess:
            print("Congratulations! You guessed the number.")
            return

        elif guess < number_to_guess:
            print("Your guess is too low.")

        else:
            print("Your guess is too high.")

    print("Sorry, you've run out of guesses. The number was", number_to_guess)

guess_a_number()
             
        
    

              
guess_a_number()
