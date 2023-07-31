new_list = [2, 5, 7, 8, 9,10,11,12]

def zeroed(list_func):
    list_func[-1] = 0
    list_func[0] = 0
    
    return list_func

print(zeroed(new_list))