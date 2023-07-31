nested_list = [1, [2, [3, 4], 5], 6]


def sum_nested_list(list1):
    total_sum = []
    for element in list1:
        if isinstance(element, int):
            total_sum.append(element *2)
        elif isinstance(element, list):
            total_sum.append(sum_nested_list(element))
    return total_sum

print(sum_nested_list(nested_list))
