def add_hash(hash):
    list = []
    for i in hash[:-1]:
        list.append(i+"#")
    list.append(hash[-1:])
    print(list)
    return list

def add_underscore(under):
    under_list = []
    for char in under:
        for newchar in char:
            under_list.append(newchar)
    for x in range(len(under_list)):
        if under_list[x] == '#':
            under_list[x] = "_"
    print(under_list)
    return under_list

def remove_underscore(score):
    newstr = ''.join(score)
    charac = "_"
    return (newstr.replace(charac, ""))

print(remove_underscore(add_underscore(add_hash('Python'))))