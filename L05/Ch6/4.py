def natural(i):
    naturalnumlist = []
    while i > 0:
        naturalnumlist.append(i)
        i = i-1
    print("The list of natural numbers is:", naturalnumlist)

def square(i):
    squarelist = []
    while i > 0:
        squarelist.append(i**2)
        i = i-1
    print("The list of the squares of those numbers is:", squarelist)

def main():
    n = int(input("Please enter a natural number: "))
    natural(n)
    square(n)

    eval(input("Press any key to exit the program,"))
main()