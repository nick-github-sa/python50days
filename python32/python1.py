import re

emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']
# com = ".com"

# b = [s for s in emails if com in s]
# print(b)
# for x in range(len(b)):
#     if b[x][:1] =="@":
#         b.pop(x)
# print(b)

import re

def email_validator(emails):
    valid_emails = []
    for email in emails:
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            valid_emails.append(email)
    com = ".com"
    valid_emails = [s for s in emails if com in s]
    if valid_emails:
        return valid_emails
    else:
        return "all emails are invalid"

print(email_validator(emails))