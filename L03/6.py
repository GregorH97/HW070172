def main():
    print("This is a program to calculate the future value of your deposit over time.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    lenght = eval(input("Enter the number of years "))

    for i in range(lenght):
        principal = principal * (1 + apr)

    print("The value in", lenght, "years is:", principal)

main()