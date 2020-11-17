def main():
    print("This program calculates whether you are eligable to be elected for the house of representatives or the senate.")
    age = float(input("Please enter your age: " ))
    citizenship = float(input("Please enter how many years you are a US citizen " ))
    if age < 30 or citizenship < 9:
        if age < 25 or citizenship < 7:
            print("You  are neither able to become Senator or Representative.")
        else:
            print("You cannot become Senator, but you can become Representative.")
    else:
        print("You can become both Representative and Senator.")

main()