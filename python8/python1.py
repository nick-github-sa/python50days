numbers = [3,4,6,7,8,11,12]

def odd_even(function_numbers):
    odd_list = []
    even_list = []
    for number in function_numbers:
        if (number % 2) == 0:
            even_list.append(number)
            max_even_list = max(even_list)
        else:
            odd_list.append(number)
            min_odd_list = min(odd_list) 
    print(max_even_list - min_odd_list)

odd_even(numbers)

