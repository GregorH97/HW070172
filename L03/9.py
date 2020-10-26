print("This is a program to convert degrees Fahrenheit into degrees Celsius. Please enter the degrees Fahrenheit below and you will get the degrees Celsius as a result.")

def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit -32) * 5/9
    print("The temperature is", celsius, "degrees Celsius")

main()

input("Press enter to quit")