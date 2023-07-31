# import pdb

# num_check = input("Please type a number between 1 and 20 \n")


# def prime_numbers(func_num_check):
#     prime_list = []
#     if func_num_check > 1:
#         for num in range(2,func_num_check+1):
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     pdb.set_trace()
#                     break
#             else:
#                 prime_list.append(num)
#     print(prime_list)   
# 

# for i in range(0,5):
#     print('*')
#     for j in range(0,i):
#         print('#',end='') 
#         for k in range(0, 4):
#             print('&',end='')   
# print()



# prime_numbers(int(num_check))





for i in range(2):
    print("*",end='')
    print()
    for j in range(4):
        print("x")
        print()
        for z in range(6):
            print("z", end='')
            for k in range(8):
                print("#", end='')
print()