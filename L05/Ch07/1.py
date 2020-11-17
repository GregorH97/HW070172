
def main():
    print("This program calculates your wage")
    hours = float(input("How many hours have you worked this week? "))
    rate = float(input("How much is your hourly payment rate? "))
    if hours <= 40 and hours > 0:
        payment = hours * rate
        print("Your payment is:", payment)
    elif hours == 0:
        print("Time to get a job then.")
    elif hours < 0:
        print("This is impossible, try again")
    else:
        overtime = hours - 40
        payment = hours * rate + overtime * rate * 1.5
        print("Your payment is: ", payment)
    eval(input("Press any key to exit the program,"))

main()