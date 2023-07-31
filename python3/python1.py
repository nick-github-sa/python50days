register = {'Michael':'yes', 'John':'yes','Peter':'yes', 'Mary':'yes'}


def register_check(new_dict):
    count = 0
    for x in new_dict.values():
        if x == 'yes':
            count += 1
    print(count)


register_check(register)
