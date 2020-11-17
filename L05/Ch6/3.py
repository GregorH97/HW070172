import math

def spherevolume(radius):
    volume = 4/3 * math.pi * radius ** 3
    return volume

def sphereArea(radius):
    area = 4 * math.pi * radius ** 2
    return area

def main():
    print("This is a program to calculate the volume and surface area of a sphere.")
    radiusinput = float(input("Please enter the radius in centimeters: "))
    volume = spherevolume(radiusinput)
    area = sphereArea(radiusinput)
    print("The volume of the sphere is:", volume, "cm**3")
    print("The area of the sphere is:", area, "cm**2")
    eval(input("Press any key to exit the program,"))

main()