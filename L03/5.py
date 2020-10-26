print("This program prints a table of Celsius temperatures and their Fahrenheit equivalent from 0 to 100.")

def main():
    celsius = 0
    for i in range(11):
        fahrenheit = 9/5 * celsius + 32
        print(celsius, "degrees Celsius equals", fahrenheit, "degrees Fahrenheit")
        celsius = celsius + 10

main()