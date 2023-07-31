import timeit
a = range(10000000)
x = set(a)
y = list(a)

number_find = 9999999

def time_function(num_to_find):
    if num_to_find in x:
        print(True)

duration1 = timeit.timeit(time_function, number_find)
print(duration1)