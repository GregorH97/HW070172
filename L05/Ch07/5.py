def main():
    print("This program calculates your BMI and shows whether you are considered healthy.")
    weight = float(input("Please enter your weight.(in pounds) " ))
    height = float(input("Please enter your height.(in inches) " ))
    BMI = weight * 720 / height
    if BMI > 25:
        print("You are considered overweight.")
    elif BMI <= 25 and BMI >= 19:
        print("Your BMI is considered to be normal.")
    elif BMI < 19 and BMI >= 0:
        print("You are considered to be underweight.")
    else:
        print("Please enter positive numbers.")
    
    eval(input("Press any key to exit the program,"))

main()