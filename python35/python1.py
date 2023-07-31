import string

string_sent = 'the quick brown fox jumps over a lazy dog'

a = string.ascii_lowercase
new_list = []
for char in a:
    new_list.append(char)

def check_panagram(value, value1):
    c = value.replace(" ", "")
    b = set(c)
    d = list(sorted(b))
    if d == value1:
        return True
    else:
        return False
    
print(check_panagram(string_sent, new_list))