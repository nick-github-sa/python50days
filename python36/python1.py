
def count(word):
    
    test = {}
    
    for letter in word:
        if letter in test:
            test[letter] += 1
        else:
            test[letter] = 1
    print(test)


count("hello")