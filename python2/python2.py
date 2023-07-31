fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
dupes = []

def check_duplicates(list_to_check):
    set_fruits = set(list_to_check)
    if len(set_fruits) == len(list_to_check):
        return "No Duplicates"
    else:
        for x in list_to_check:
            if x in set_fruits:
                dupes.append(x)
                print(dupes)
            else:
                set_fruits.add(x)
            


print(check_duplicates(fruits))
