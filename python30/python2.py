names = ['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown','Tom Cruise']


def sorted_names(func_names):
    test_list = []
    new_test_list = []
    for name in range(len(func_names)):
        a = func_names[name].split()
        test_list.append(a[::-1])
    for new_name in test_list:
        b = " ".join(new_name)
        new_test_list.append(b)
    print(sorted(new_test_list))



sorted_names(names)