list = ['Java', 'JavaScript', 'Python']

def longest_word(func_list):
    names_dict = {}
    new_list = []
    for item in func_list:
        names_dict[item] = len(item)
    max_value = max(names_dict.values())
    value = [i for i in names_dict if names_dict[i]==max_value]
    newvalue = ''.join(value)
    new_list.extend((max_value, newvalue))
    print(new_list)

longest_word(list)