list = ['Java', 'JavaScript', 'Python']

count = 0
names = ""

for char in list:
    if len(char) > count:
        count = len(char)
        names = char
new_list = [count, names]
print(new_list)
