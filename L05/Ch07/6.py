def main():
    print("This program calculates whether you were over the speed limit and if so, how high your fine is.")
    speedlimit = float(input("Please enter the speed limit.(in mph) But under 90 mph " ))
    speed = float(input("Please enter your speed.(in mph) " ))
    if speedlimit >= 90:
        print("Please enter a speed limit below 90 mph.")
    elif speedlimit < 90 and speedlimit > 0:
        speeding = speed - speedlimit
        if speeding <= 0:
            print("You have driven under the speed limit")
        elif speeding > 0 and speed < 90:
            fine = 50 + speeding*5
            print("Your fine is:", fine, "dollars.")
        else:
            fine = 250 + speeding*5
            print("Your fine is:", fine, "dollars.")
    else:
        print("Please enter positive numbers.")
    
    eval(input("Press any key to exit the program,"))

main()