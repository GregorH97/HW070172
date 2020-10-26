print("This is a program to convert degrees Celsius into degrees Fahrenheit. Please enter the degrees Celsius below and you will get the degrees Fahrenheit as a result.")

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit")

main()

input("Press enter to quit")