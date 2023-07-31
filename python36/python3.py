norm_word = "hello"
lower_word = norm_word.lower()
vowel = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
def count_the_vowels(word):
    test = {}
    for x in word:
        for y in vowel:
            if y == x:
                test[x] = 1
    return sum(test.values())

print(f' The number of vowels is', count_the_vowels(lower_word))
