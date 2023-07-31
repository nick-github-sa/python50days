
import string
import re

alpha = string.ascii_lowercase
string = 'Python has a string format operator %%. This functions analogously to printf format strings in C, e.g. "spam=%%s eggs=%%d" %% ("blah", 2) evaluates to "spam=blah eggs=2"'
string1 = string.lower()

list_of_symbols = ['(', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ')']

def analyze_string(string1):
    count = 0
    new_dict = {"special character" : 0, "words" : 0, "total characters" : 0}

    pattern = r'\b[a-zA-Z]{3,}\b'
    matches = re.findall(pattern, string1)
    for word in matches:
        new_dict["words"] += 1

    for char in string1:
            if char in list_of_symbols:
                new_dict['special character'] += 1
    
    for char in string1:
         if char == ' ':
              continue
         else:
              count += 1
    
    new_dict['total characters'] = count
    print(new_dict)

analyze_string(string1)