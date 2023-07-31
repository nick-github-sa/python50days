list_1 = [10, 12, 34]
List_2 = [12, 56, 78]

def add_reverse(x_1,y_2):
    new_list = []
    if len(list_1) == len(List_2):
        for i in range(len(x_1)):
            new_list.append(x_1[i] + y_2[i])
        # reverse_list = new_list[::-1]
        print(new_list[::-1])
    else:
        print("The lists are not equal length")

add_reverse(list_1, List_2)