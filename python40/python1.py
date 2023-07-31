
def translate():
    vowels = ['a', 'e', 'i', 'o', 'u']
 
    a = ' i love python'
    word_list = a.split()
    new_word_list = []

    for word in word_list:
        if word[0] in vowels:
            new_word_list.append(word + "yay")
        else:
            new_word_list.append(word[1:] + word[0] + "ay")

    print(' '.join(new_word_list))


translate()