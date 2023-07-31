first_pass = [1, 4, 6, 0, 7, 0, 9]
second_pass = [2, 1, 4, 7, 6]


def zeros_last(input_argument):
    test = []
    result = input_argument.count(0)
    if result > 0:
        print(result)
        for i in input_argument:
            if i == 0:
                input_argument.append(i)
                del input_argument[input_argument.index(i)]

        print(input_argument)
    
    else:
        test = sorted(input_argument)
        print(test)

zeros_last(first_pass)