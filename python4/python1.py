test_float = (12, 12)

def only_floats(new_check):
    # for num in new_check:
    #     if isinstance(num, float):
    #         print("yes")
    if isinstance(new_check[0],float) and isinstance(new_check[1],float):
        print(2)
    elif isinstance(new_check[0],float) or isinstance(new_check[1],float):
            print(1)
    else:
        print(0)



only_floats(test_float)