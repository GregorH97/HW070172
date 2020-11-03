def main():
    import math
    print("This is a program to calculate the average of numbers entered by the user.")
    a = int(input("Please enter the amount of numbers that you want to average: "))
    sum = 0
    for i in range(a):
        entry = float(input("Please enter a number that you want to enter to the calculation "))
        sum = sum + entry
    average = sum / a
    print("The  average of your numbers is", average)
    eval(input("Press any key to exit the program"))
main()