def count_the_vowels(string):
    vowels = set('aeiouAEIOU')
    count = 0
    for char in string:
        if char in vowels:
            count += 1
            vowels.discard(char)
    return count
