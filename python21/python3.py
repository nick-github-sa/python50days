def even_or_average():
    # Ask the user to input five numbers
    numbers = []
    for i in range(5):
        number = int(input("Enter a number: "))
        numbers.append(number)

    # Find the largest even number in the inputted numbers
    even_numbers = [number for number in numbers if number % 2 == 0]
    if even_numbers:
        largest_even = max(even_numbers)
        return largest_even
    else:
        # If there are no even numbers, calculate and return the average
        average = sum(numbers) / len(numbers)
        return average

result = even_or_average()
print(result)
