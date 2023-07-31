list = ['1', '2', '3', '4']

def convert_add(numbers):
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    print(sum(numbers))



convert_add(list)