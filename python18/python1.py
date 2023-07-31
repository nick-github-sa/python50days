

new_name = ''
list_new = []

while new_name != 'q':
    new_name = input("Please type in a random number, or else 'quit' to see average - ")
        
    if new_name != 'q':
        list_new.append(int(new_name))
        
print(sum(list_new) / len(list_new))

