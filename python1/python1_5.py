fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(a_dict):
    print(max(a_dict.values(), key=len))



longest_value(fruits)