print("this is a calculator progrme")

def main():
    for i in range(999999):
        calculation = eval(input("Type your calculation, it should consist out of a number, a mathematical expression, followed by another number "))
        if calculation > 100:
            print("The calculation should be below 100, please try again")
        if calculation < 100:
            print("The outcome is:", calculation)

main()

input("Press enter to quit")