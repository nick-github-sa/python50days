# Python 3.x code to demonstrate star pattern
import emoji
# Function to demonstrate printing pattern triangle

user_num = int(input("Please enter a number between 5 and 10 \n"))

def triangle(number):
     
    # number of spaces
    k = number - 1
 
    # outer loop to handle number of rows
    for i in range(0, number):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print(emoji.emojize(':snake: '), end="")
     
        # ending line after each row
        print("\r")
 
# Driver Code

triangle(user_num)