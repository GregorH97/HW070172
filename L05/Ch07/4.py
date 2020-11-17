def main():
    print("This program shows the classification of a student based on his number of credits.")
    points = int(input("Please enter the amount of credits the student reached. " ))
    if points < 7 and points >= 0:
        print("The student is a Freshman.")
    elif points < 16 and points >= 7:
        print("The student is a Sophpormone.")
    elif points < 24 and points >= 16:
        print("The student is a Junior.")
    elif points < 24:
        print("The student is a Senior.")
    else:
        print("It is not possible to get a negative number of credits.")
    
    eval(input("Press any key to exit the program,"))

main()