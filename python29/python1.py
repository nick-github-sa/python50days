def middle_figure(a,b):
    test1,test2 = "".join(a),"".join(b)
    word = test1.replace(" ", "") + test2.replace(" ", "")
    if len(word) % 2 == 0:
        letter = len(word) / 2
        print(word[int(letter)])
    else:
        print('No middle figure')

middle_figure('make love', 'not war')