def main():
    print("This program calculates the wage of the babysitter.")
    start = float(input("Please enter the start hour of the babysitter.(in an timeframe of 0.0 - 24.0) " ))
    end = float(input("Please enter the ending hour of the babysitter.(in an timeframe of 0.0 - 24.0) " ))
    if end < start:
        end = end + 24
        if end <= 21 and start < 21:
            time = end - start
            wage = time * 2.5
            print("The wage is:", wage)
        elif end > 21 and start < 21:
        

    else:
        time = finish -start



    elif BMI <= 25 and BMI >= 19:
        print("Your BMI is considered to be normal.")
    elif BMI < 19 and BMI >= 0:
        print("You are considered to be underweight.")
    else:
        print("Please enter positive numbers.")
    
    eval(input("Press any key to exit the program,"))

main()