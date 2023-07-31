test = "boob"

def same_in_reverse(string):
    reverse_test = []
    for i in string[::-1]:
        reverse_test.append(i)
    if reverse_test == list(test):
        return True
    else:
        return False

print(same_in_reverse(test))
