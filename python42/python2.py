

def student_marks():
    x = ""
    dict_names = {}
    while True:
        x = input("Type 'done' if complete or any key to continue - ")
        if x == "done":
            break
        else:
            student_name = input("Please enter student name - ")
            student_marks = input("Please enter student marks - ")
            dict_names[student_name] = student_marks
    return dict_names   

print(student_marks())