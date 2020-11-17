def main():
    print("This is a program to calculate how long it takes for an investment to double.")
    investment = float(input("Please enter your investment: "))
    rate = float(input("Please enter the interest rate: "))
    ininvest = investment
    years = 0
    while ininvest*2 > investment:
        investment = investment * (1+rate)
        years = years + 1
    print("It will take", years, "years for your invesment to double.")
    eval(input("Press any key to exit the program,"))

main()