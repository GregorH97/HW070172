def main():
    import math
    print("This program calculates the cost of a circular pizza.")
    cost = float(input("Please enter the cost of the pizza per square cm in euros: "))
    radius = float(input("Please enter the radius of the pizza in centimeters: "))
    area = math.pi * radius ** 2
    price = area * cost
    print("The total price for the pizza is: ", price, "euros.")
    eval(input("Press any key to exit the program"))

main()

