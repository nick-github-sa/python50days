names = [ "aBc", "ab", "A"]

def sort_length(argu):
    for i in range(len(argu)):
        for j in range(len(argu) - 1):
            if len(argu[j]) > len(argu[j + 1]):
                argu[j], argu[j + 1] = argu[j + 1], argu[j]
    return argu

print(sort_length(names))
