dots = "h.e.l.p."

def count_dots(in_param):
    counter = 0
    for char in in_param:
        if char == ".":
            counter += 1
    return f'There are {counter} dots! {"."*counter}'

print(count_dots(dots))