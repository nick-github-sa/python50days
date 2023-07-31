from textblob import TextBlob

def spelling_checker(inputted_word):
    a = TextBlob(inputted_word)
    if a.correct() == inputted_word:
        print("that is correct spelling")
    else:
        print("spelling is incorrect, do you mean", a.correct())

spelling_checker(input("Please input a word - "))