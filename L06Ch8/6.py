def main():
    print("This program can find out whether a given number is a prime or not, if not than it will find the next-lowest prime number.")
    value = int(input("Please enter a number: "))
    i = value - 1
    while value%i != 0 and i >2:
        i = i - 1
        if value%i != 0:
            value = value
        else:
            value = value - 1
    if value%i != 0:
        print("This number ", value, "is a prime number")

    eval(input("Press any key to exit the program"))
main()