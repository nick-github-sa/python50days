nest_list =  [[2, 4, 5, 6], [2, 3, 5, 6]]
new_list = []
def sum_list(func_list):
    for i in nest_list:
        for j in i:
            new_list.append(j)
    print(sum(new_list))

sum_list(new_list)