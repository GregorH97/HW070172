import math

def area(a, b, c):
    s = (a + b + c) / 2
    a = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return a

def main():
    print("This is a program to calculate the area of a triangle.")
    a = int(input("Please enter the side a in cm: "))
    b = int(input("Please enter the side b in cm: "))
    c = int(input("Please enter the side c in cm: "))
    a = area(a, b, c)
    print("The area of the triangle is", a, "square centimeters.")
    eval(input("Press any key to exit the program"))
main()