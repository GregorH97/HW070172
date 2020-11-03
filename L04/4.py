def main():
    print("This is a program that calculates the distance to a lightning strike based on the time between the lightnig and the tunder.")
    time = float(input("Please enter the amount of time passed between the lightning and the thunder in seconds: "))
    distance = 4.8*time
    print("The distance between you and the lightning strike is", distance, "miles.")
    eval(input("Press any key to exit the program"))
main()