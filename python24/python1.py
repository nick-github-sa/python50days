
def average_calories():
    calories = []
    while True:
        calorie_input = input("Enter your calories intake for a day (Type 'done' to finish: ) \n")
        if calorie_input == "done":
            break
        try:
            calorie = float(calorie_input)
            calories.append(calorie)
        except ValueError:
            print("Invalid input, Please type a number or type 'done' to finish")

    if len(calories) == 0:
        print("No data returned.")
        return 0
    average = sum(calories) / len(calories)

    return average 

print("Your average calories intake is:", average_calories())

