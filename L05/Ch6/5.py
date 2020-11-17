import math

def ar(i):
    area = math.pi * i ** 2
    return area

def pri(x, y):
    price = x * y
    return price

def main():
    print("This program calculates the cost of a circular pizza.")
    cost = float(input("Please enter the cost of the pizza per square cm in euros: "))
    radius = float(input("Please enter the radius of the pizza in centimeters: "))
    area = ar(radius)
    price = pri(area, cost)
    print("The total price for the pizza is: ", price, "euros.")
    eval(input("Press any key to exit the program,"))

main()