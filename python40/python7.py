

list1 = [1, [2, [3, 4], 5], 6]

def sum_nested_list(list1):
    total_sum = 0
    for element in list1:
        if isinstance(element, int):
            total_sum += element
        elif isinstance(element, list):
            total_sum += sum_nested_list(element)
    return total_sum

print(sum_nested_list(list1))
