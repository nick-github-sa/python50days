nested_list = [[12, 34, 56, 67], [34, 68, 78]]

new_list = []
for test_list in nested_list:
    for number in test_list:
        if number == 34 or number == 67 or number == 78:
            new_list.append(number)

new_set = set(new_list)
b = list(new_set)
print(b)

