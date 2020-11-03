
def main():
    import math
    print("This is a program to calculate the volume and surface area of a sphere.")
    r = float(input("Please enter the radius in centimeters: "))
    volume = 4/3 * math.pi * r ** 3
    area = 4 * math.pi * r ** 2
    print("The volume of the sphere is:", volume, "cm**3")
    print("The area of the sphere is:", area, "cm**2")
    eval(input("Press any key to exit the program,"))

main()