def main():
    print("This is a program to calculate the future value of your deposit over time.")
    principal = eval(input("Enter your annual investment: "))
    amount = principal
    apr = eval(input("Enter the annual interest rate: "))
    lenght = eval(input("Enter the number of years "))

    for year in range(lenght):
        amount = amount * (1 + apr)
        print("The amount of money on your account after", year + 1, "year(s) is", amount)
        amount = amount + principal


main()