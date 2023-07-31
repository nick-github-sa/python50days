a = [1,2,3,4]
b = [5,6,7,8]


def make_tuples(c,d):
    mergedlist = [(c[i], d[i]) for i in range(len(a))]
    print(mergedlist)
    
    

make_tuples(a,b)