def main():
    import math
    cycles = int(input("Please enter which value within the Fibonacci-sequence you want to have displayed: "))
    a = 1
    b = 0
    for i in range (cycles):
        c = a + b
        a = b
        b = c

    print("The  Fibonacci-number at the", cycles, "place is:", c)
    eval(input("Press any key to exit the program"))
main()