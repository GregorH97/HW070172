def main():
    print("This is a program to calculate the future value of your deposit over time.")
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    period = eval(input("How many times is the interest rate compounded each year? "))

    for i in range(10*period):
        principal = principal * (1 + (apr/period))


    print("The value in 10 years is:", principal)

main()