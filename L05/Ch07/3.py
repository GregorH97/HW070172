def main():
    print("This program calculates the score of a student.")
    points = int(input("Please enter the amount of point the student reached (100-0). " ))
    if points <= 100 and points >=90:
        print("The student will get an A")
    elif points < 90 and points >= 80:
        print("The student will get a B")
    elif points < 80 and points >= 70:
        print("The student will get a C")
    elif points < 70 and points >= 60:
        print("The student will get a D")
    elif points < 60 and points >= 0:
        print("The student will get a F")
    else:
        print("Please enter a number between 0 and 100")
    
    eval(input("Press any key to exit the program,"))

main()