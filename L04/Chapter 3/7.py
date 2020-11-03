def main():
    import math
    print("This is a program to calculate the distance between two coordinates")
    x1 = float(input("Please enter the coordinates for x1: "))
    y1 = float(input("Please enter the coordinates for y1: "))
    x2 = float(input("Please enter the coordinates for x2: "))
    y2 = float(input("Please enter the coordinates for y2: "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("The distance between the points is: ", distance)
    eval(input("Press any key to exit the program"))
main()