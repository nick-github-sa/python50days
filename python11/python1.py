one_string = "love"
two_string = "evoly"

# def equal_strings(a, b):
#     print(a, b)
#     if len(a) == len(b):
#         for char in a:
#             if char in b:
#                 print("True")
#             else:
#                 break

#     else:
#         print("False")


# equal_strings(one_string,two_string)
if sorted(one_string) == sorted(two_string):
    print("True")
else:
    print("False")
print(sorted(one_string))
print(sorted(two_string))