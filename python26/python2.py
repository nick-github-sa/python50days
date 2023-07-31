s = 'Hi my name is Richard'

def string_length(func_str):
    count = 0
    dict_new = {}
    test = list(func_str.split(" "))
    for word in test:      
        count += 1
        dict_new[word] = len(word)
    print(dict_new)

string_length(s)