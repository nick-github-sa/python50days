list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [ 42, 30, 80, 65, 68, 88, 95]

def inter_section():

    # a = [num for (num) in list1 if num in list2]
    # b = [num for num in list2 if num in list1]
    # print(a, b)

    a = tuple([x for x in list1 for y in list2 if x == y])
    print(a)



inter_section()

