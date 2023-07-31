
while True:

    try:
        number1 = float(input("Please enter first number - \n"))
        operation = input("Please enter operation type - \n")
        number2 = float(input("Please enter second number - \n"))
        
        if operation == "+":
            print("The answer is", number1 + number2)
        elif operation == "-":
            print("The answer is", number1 - number2)
        elif operation == "*":
            print("The answer is", number1 * number2)
        elif operation == "/":
            print("The answer is", number1 / number2)
        
        choice = input("Type q to quit or enter to try again \n")
        
        if choice == "q":
            break

    except (ValueError, ZeroDivisionError, NameError) as error:
        print(error)