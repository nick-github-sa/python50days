import time
a = range(10000000)
x = set(a)
y = list(a)

number_find = 9999999

t0 = time.time()
if number_find in x:
    print(True)
t1 = time.time()
total = t1-t0
print("This is the set search time", total)

t2 = time.time()
if number_find in y:
    print(True)
t3 = time.time()    
total1 = t3-t2
print("This is the list search time", total1)




