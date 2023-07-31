

name = input("Please enter teachers name - \n")
periods = int(input("Please enter the number of periods - \n"))
rate = 20
overtime_rate = 25
print()
def your_salary():
    if periods > 100:
        period_diff = periods - 100
        print("Teacher:",name)
        print("Periods:",periods)
        print("Gross Salary:", (100*rate) + (period_diff * overtime_rate))
    else:
        print("Teacher:",name,)
        print("Periods:",periods)
        print("Gross Salary:", periods*rate)

your_salary()