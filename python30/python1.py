name = ["John", "Peter", "John", "Peter", "Jones", "Peter", "John", "John"]

def repeated_name(func_list):
    counter = 0
    # num = func_list[0]

    for i in func_list:
        frequency = func_list.count(i)
        # print(frequency)
        if(frequency > counter):
            counter = frequency
            print(i)
            num = i
    
    return num

print(repeated_name(name))


# def repeated_name(func_list):
#     # a = max(set(func_list), key=func_list.count)
#     b = max(set(func_list))
#     print(b)

# repeated_name(name)