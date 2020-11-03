def main():
    import math
    print("This is a program to calculate the lenght of a ladder.")
    height = int(input("Please enter the height at which the ladder is leaned against the wall in meters: "))
    angle = int(input("Please enter the angle at which the ladder is leaned against the wall in degrees: "))
    radians = (math.pi / 180) * angle
    lenght = height / (math.sin(radians))
    print("The lenght of the ladder is", lenght, "meters.")
    eval(input("Press any key to exit the program"))
main()