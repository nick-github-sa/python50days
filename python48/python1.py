list1 = [12, 34, 56, 78, 98, 22, 45, 13]
item = 22

def search_binary(list1, item):
    found = False
    first = 0
    sorted_list = sorted(list1)
    last = len(sorted_list) - 1

    while first <= last and found == False:
        midpoint = (first + last)//2

        if sorted_list[midpoint] == item:
            return sorted_list.index(item)+first
        else:
            if sorted_list[midpoint] < item:
                first = midpoint + 1
                print(first)
            else:
                last = midpoint - 1
                print(last)
    return found

func_result = search_binary(list1, item)
print(func_result)