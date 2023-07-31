import csv


def save_emails(): 
    email_dict = {}
    count = 1
    while True:
        user_input = input("Please type in emails or type 'done' if finished ")
        if user_input == "done":
            break
        else:            
            email_dict[count] = user_input
            count += 1
            with open('write_to_csv.csv', 'w') as file:
                writer = csv.writer(file)
                for key, value in email_dict.items():
                    writer.writerow([value])
    print(email_dict)
save_emails()



