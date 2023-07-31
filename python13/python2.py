import emoji

while True:

    user_num = int(input("Please enter a number between 5 and 10 \n"))
    
    def Python_snakes(func_user_num):
        k = 0
        for i in range(1, func_user_num+1):
            for space in range(1, (func_user_num-i)+1):
                print(end="  ")
   
            while k!=(2*i-1):
                print(emoji.emojize(':snake: '), end="")
                k += 1
   
            print()
        # for i in range(func_user_num):
        #     print(emoji.emojize(':snake: ') * i)


    Python_snakes(user_num)





