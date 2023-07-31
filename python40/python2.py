

def word_frequency(sentence):
    word_dict = {}
    test_sentence = sentence.lower()
    list_sentence = test_sentence.split()
    for words in list_sentence:
        if words in word_dict:
            word_dict[words] += 1
        else:
            word_dict[words] = 1
    print(word_dict)



word_frequency("The quick brown fox jumps over the lazy dog")