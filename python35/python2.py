list_1 =  [1, 2, 4, 6, 7, 7]
int_1 = 8

def find_index(int_1, list_1):
        list_new = []
        for index,num in enumerate(list_1):
            if num == int_1:
                  list_new.append(index)
            elif int_1 not in list_1:
                    list_new.append(int_1)
        return list_new
   
print(find_index(int_1, list_1))