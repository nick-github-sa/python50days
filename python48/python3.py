def search_binary_recursive(lst, item, low, high):
    if low > high:
        return -1  # Item not found

    mid = (low + high) // 2

    if lst[mid] == item:
        return mid
    elif lst[mid] < item:
        return search_binary_recursive(lst, item, mid + 1, high)
    else:
        return search_binary_recursive(lst, item, low, mid - 1)


# Test the function
list1 = [12, 34, 56, 78, 98, 22, 45, 13]
search_item = 22
index = search_binary_recursive(list1, search_item, 0, len(list1) - 1)
print("Index of", search_item, "in the list:", index)
