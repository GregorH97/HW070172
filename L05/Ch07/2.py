def main():
    print("This program calculates the score of a student.")
    points = int(input("Please enter the amount of point the student reached (5-0). " ))
    if points == 5:
        print("The student will get an A")
    elif points == 4:
        print("The student will get a B")
    elif points == 3:
        print("The student will get a C")
    elif points == 2:
        print("The student will get a D")
    elif points == 1 or points == 0:
        print("The student will get a F")
    else:
        print("Please enter a number between 0 and 5")
    
    eval(input("Press any key to exit the program,"))

main()

