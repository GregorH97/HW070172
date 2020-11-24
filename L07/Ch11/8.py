def getthings():
    nums = []
    xStr = input("Enter numbers you want to have in your listing (<Enter> to quit)")
    while xStr != "":
        x = int(xStr)
        nums.append(x)
        xStr = input("Enter numbers you want to have in your listing (<Enter> to quit)")
    return nums

def removeduplicates(list):
    removelist = []
    for i in list:
        if list.count(i) == 1:
            removelist.append(i)
    return removelist

def main():
    print("This program removes duplicates from a given list.")
    list = getthings()
    removelist = removeduplicates(list)
    print("The list with all duplicates removed is: ", removelist)

    

main()