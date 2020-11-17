def main():
    print("This is a program that calculates the syracuse value of a given number.")
    value = int(input("Please enter a number. "))
    inval = value
    listval = []
    while value != 1:
        if value%2 == 0:
            value = value/2
            listval.append(int(value))
        else:
            value = value*3 + 1
            listval.append(int(value))
    print("The syracuse sequence for", inval, "is", listval)

    eval(input("Press any key to exit the program,"))
main()