from random import random

def getthings():
    nums = []
    xStr = input("Enter numbers you want to have in your listing (<Enter> to quit)")
    while xStr != "":
        x = int(xStr)
        nums.append(x)
        xStr = input("Enter numbers you want to have in your listing (<Enter> to quit)")
    return nums

def main():
    print("This program rearranges numbers into a random order.")
    list = getthings()
    randomlist = []
    for i in range(len(list)):
        randomnumber = int(random() * len(list)) - 1
        randomlist.append(list[randomnumber])
        list.remove(list[randomnumber])
    print("The random list is: ", randomlist)
main()