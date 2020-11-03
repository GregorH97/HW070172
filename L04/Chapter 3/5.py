def main():
    print("This is a program that calculates shipping cost for the 'Konditorei' coffee shop")
    pound = float(input("How many pounds do you want to order? "))
    price = 0.86*pound + 1.5
    price = round(price, 2)
    print("The price for the order is", price, "dollars.")
    eval(input("Press any key to exit the program"))
main()