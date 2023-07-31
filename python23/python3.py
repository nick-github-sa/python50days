
s = "love live and laugh"
s1 = "Hate war love Peace"

def multiply_words(def_s):
    count = 1
    list_test = []
    list_test1 = []
    list = def_s.split(" ")
    for word in list:
        if not word.istitle():
            list_test1.append(word)       
    for i in range(len(list_test1)):
        x = len(list_test1[i])
        list_test.append(x)
    for y in list_test:
        count = y * count
    print(count)
  
multiply_words(s1)