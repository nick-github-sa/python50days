list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]

def difference(a,b):
    # new_list = list(set(a) - set(b)) + list(set(b) - set(a))
    # # new_list1 = list(set(b) - set(a))
    s = set(list2)
    s1 = set(list1)
    temp3 = [x for x in list1 if x not in s]
    temp4 = [x for x in list2 if x not in s1]
    print(temp3 + temp4)




difference(list1,list2)