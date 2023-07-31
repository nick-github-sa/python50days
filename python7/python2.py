import pdb
from collections import Counter

names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]

res=[]
for name in names:
    for letter in name:
        if letter == "S":
            res.append(name)

print(res)
res_dict = {x:res.count(x) for x in res}

print(res_dict)
    





