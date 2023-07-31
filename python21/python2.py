


def  even_or_average():
    list_new = []
    list_two = []
    print("Please enter 5 numbers - \n")
    count = 0
    while len(list_new) < 5: 
        user_input = input(f'Please input number {count + 1} - ')
        list_new.append(int(user_input))
        count += 1
        continue
    print(list_new)
    for i in list_new:
        if i % 2 == 0:
            list_two.append(i)
            print(max(list_two))
        else:
            print(sum(list_new) / len(list_new))

even_or_average()