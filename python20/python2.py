str1 = 'leArning is hard, bUt if You appLy youRself ' \
 'you can achieVe success'

list1 = str1.split()
new_list = []
for char in list1:
    for letter in char:
        if letter.isupper():
            new_list.append(char[::-1])

print(new_list)


