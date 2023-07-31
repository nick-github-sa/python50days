values =  [1, 2, 4,67, 7, 10]

def swap_values(swap_list_values):
    swap_list_values[0],swap_list_values[-1] = swap_list_values[-1], swap_list_values[0]
    print(swap_list_values)


swap_values(values)