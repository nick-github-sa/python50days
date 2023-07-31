students = ['Male', 'Female', 'female', 'male', 'male', 'male','female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

male = 0
female = 0
named_list = []

for name in students:
    if name == 'Male' or name == 'male':
        male += 1
    else:
        female += 1

male_new = ('Male', male)
female_new = ('Female', female)

named_list.append(male_new)
named_list.append(female_new)

print(named_list)