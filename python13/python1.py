
def your_vat():
    
    while True:
        try:
            c = int(input("Please enter price of item \n"))
   
            d = int(input("Please enter vat % \n"))

            e = (c / 100) * d
            f = e + c
            print(f)
            break
        except ValueError:
            print("That is not a valid number!")
your_vat()