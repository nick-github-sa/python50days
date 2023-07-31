numbers = "23569"

def biggest_odd(func_numbers):
        y = [int(x) for x in func_numbers]
        # newlist = []
        # newlist[:0] = func_numbers
        print(y)
        odd = [x for x in y if x % 2 == 1]
        print(max(odd))
    
biggest_odd(numbers)