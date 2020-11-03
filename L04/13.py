def main():
    import math
    print("This is a program to calculate a sum of numbers entered by the user.")
    a = int(input("Please enter the amount of numbers that you want to sum up: "))
    sum = 0
    for i in range(a):
        entry = float(input("Please enter a number that you want to enter to the calculation "))
        sum = sum + entry
    print("The total sum of your numbers is", sum)
    eval(input("Press any key to exit the program"))
main()