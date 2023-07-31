sentence = input("Please enter a string of words \n")

def count_words(func_sent):
    y = (func_sent.split())
    print(len(y))
    return y

def count_elements(func_y):
    count = 0
    print(func_y)
    for j in str(func_y):
        for k in j:
            if k == ' ' or k == "'" or k ==',' or k == "[" or k == "]":
                continue
            else:
                count += 1
    print(count)

y = count_words(sentence)
count_elements(y)