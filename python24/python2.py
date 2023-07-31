def nested_lists(*lists):
    nested_list = []
    for lst in lists:
        nested_list.append(lst) 
    return nested_list
    
list1 = [1, 2, 3, 5] 
list2 = [1, 2, 3, 4] 
list3 = [1, 3, 4, 5]

nested_list = nested_lists(list1, list2, list3)
print(nested_list)





