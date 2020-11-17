import math

def Fibonacci(cycles):
    a = 1
    b = 0
    for i in range (cycles):
        c = a + b
        a = b
        b = c
    return c

def main():
    cycles = int(input("Please enter which value within the Fibonacci-sequence you want to have displayed: "))
    c = Fibonacci(cycles)

    print("The  Fibonacci-number at the", cycles, "place is:", c)
    eval(input("Press any key to exit the program"))
main()