str1 = "the love is real"

def read_backwards(func_arg):
    new_list = func_arg.split()
    return (' '.join(new_list[::-1]))

print(read_backwards(str1))
