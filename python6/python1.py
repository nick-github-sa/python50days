

email_add = input("Please type in your email address - \n")

for char in email_add:
        if char == '@':
            break
        else:
            print(char, end = '')
print('')

