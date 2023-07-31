list1 = [3, 67, 87, 9, 2]

def largest_number(func_input):
    new_list = []
    for num in list1:
        for x in str(num):
            new_list.append(x)
    a = sorted(new_list)
    b = a[::-1]
    test = int("".join(b))
    print((f"{test:,d}"))

largest_number(list1)