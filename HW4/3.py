def main():
    print("This is a program to calculate the weight of carbohydrates in grams per mole.")
    H = 1.00794
    C = 12.0107
    O = 15.9994
    NH = int(input("Please enter the number of Hydrons: "))
    NC = int(input("Please enter the number of Carbons: "))
    NO = int(input("Please enter the number of Oxygens: "))
    weight = H*NH + C*NC + O*NO
    print("The molecular weight is: ", weight)
    eval(input("Press any key to exit the program"))

main()