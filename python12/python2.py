while True:

    year_age = input("Please enter your year age in format yyyy - \n")
  
    if len(year_age) < 4 or len(year_age) > 4 or (int(year_age) < 1900) or (int(year_age) > 2023):
        print("Please try again, that number is incorrect format")
    else:
        num = (2023-int(year_age))*525600
        print(f"You are this old - {num:,} in minutes!")
        break

