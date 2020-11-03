def main():
    import math
    print("This is a program to calculate the sum of the first natural numbers.")
    n = int(input("Please enter a natural number: "))
    fact = 1
    for i in range (n, 1, -1):
        fact = fact + i
    print("The sum of the natural numbers is: ", fact,".")
    eval(input("Press any key to exit the program"))
main()