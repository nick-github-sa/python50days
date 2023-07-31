day27 = [1, 2, 4, 5, 6, 7, 8, 9] 

def  unique_numbers(func_arg):
    test = set(func_arg)
    unique = sum(list(test))
    original = sum(func_arg)
    sumtotal = original - unique
    if sumtotal % 2 == 0:
        return func_arg
    else:
        return list(test)

print(unique_numbers(day27))