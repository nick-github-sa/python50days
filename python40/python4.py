string_1 = "abcd"
string_2 = "dbca"

def list_test(string1, string2):
    list_1 = []
    list_2 = []
    for char in string1:
        list_1.append(char)
    for char in string2:
        list_2.append(char)
    list_2.sort()

    if list_1 == list_2:
        return True
    else:
        return False

print(list_test(string_1, string_2))






