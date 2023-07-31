while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Cannot divide by zero!")
                continue
            else:
                result = num1 / num2
        else:
            print("Invalid operator!")
            continue
        
        print("Result: ", result)
        
    except ValueError:
        print("Please enter valid numbers!")
        
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        
    except NameError:
        print("Invalid input!")
        
    else:
        break
