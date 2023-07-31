names = [ "Peter", "Jon", "Andrew"]

def sort_length(strings):
    for i in range(len(strings)):
        print(len(strings))
        for j in range(len(strings) - 1):
            print(i*"y")
            if len(strings[j]) > len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
    return strings

print(sort_length(names))