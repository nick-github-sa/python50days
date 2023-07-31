string1 = "love life"

def sort_words(func_str):
    comma = ','
    test_list = []
    test_list1 = []
    new_list = func_str.split()
    for i in new_list:
        for j in i:
            test_list.append(j)
    test_list1 = sorted(set(test_list))
    print(f"[{','.join(test_list1)}]")


sort_words(string1)