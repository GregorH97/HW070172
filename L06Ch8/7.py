def primenumberfinder(pr):
        number = pr//2
        x = 2
        while x <= number:
            value = pr % x
            if value == 0:
                return None
            else:
                x = x + 1
        return pr
def main():
    print("This program claculates two prime numbers, which add up to the given number")
    number = eval(input("Please enter an even positive number: "))
    if number % 2 != 0 or number < 0:
        print("Please enter an even positive number")
    else:
        calcnumb = number
        while calcnumb > 0:
                prime1 = primenumberfinder(calcnumb+1)
                if prime1 != None:
                        prime2 = number - prime1
                        test = primenumberfinder(prime2)
                        if test != None:
                            print("The searched prime numbers that add to", number, "are", prime1, "and", prime2)
                calcnumb = calcnumb - 1 
                
main()
