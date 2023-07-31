string = "i like learning"

def capitalize(func_string):
    empty_string = []
    list_string = func_string.split()
    for i in list_string:
        empty_string.append(i.capitalize())
    con_string = ' '.join(empty_string)
    print(con_string)


capitalize(string)