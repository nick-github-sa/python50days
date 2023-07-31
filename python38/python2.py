list1 = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17, 
 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]

def missing_numbers(list1):
    x = str((list1[-1] + 1))
    test_list = []

    for num in range(1,int(x)):
        test_list.append(num)
    k = [item for item in test_list if item not in list1]

    print(k)
        
missing_numbers(list1)