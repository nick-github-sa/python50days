

price = input('Please input a price\n')
discount = input('Please input a discount\n')

def my_discount(func_price, func_discount):
    discounted_value = (int(func_price) * int(func_discount)) / 100
    return int(func_price) - float(discounted_value)

print(my_discount(price, discount))
