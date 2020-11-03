def main():
    import math
    print("This is a program to calculate the epact of the gregorian calendar.")
    year = int(input("Please enter the year: "))
    c = year // 100
    epact = (8 + (c // 4) - c + ((8*c + 13) // 25) + 11 * (year % 19))%30
    print("The gregorian impact for the year", year, "is", epact)
    eval(input("Press any key to exit the program"))
main()