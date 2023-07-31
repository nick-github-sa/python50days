import math

def divide_or_square(a_number):
    if a_number % 5 == 0:
        return(math.sqrt(a_number))



print(divide_or_square(10))