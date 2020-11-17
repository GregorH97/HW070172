def main():
    print("This program can find the Greatest Common Denominator (GMD) for two given numbers")
    m = int(input("Please enter the first number: "))
    n = int(input("Please enter the second number: "))

    if m < n:
        x = n
        n = m
        m = x
            
    while m != 0:
        x = m
        m = n % m
        n = x

    print("The GCD is:", n)

    eval(input("Press any key to exit the program"))
main()