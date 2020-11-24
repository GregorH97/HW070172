def getthings():
    nums = []
    xStr = input("Enter numbers you want to have in your listing (<Enter> to quit)")
    while xStr != "":
        x = int(xStr)
        nums.append(x)
        xStr = input("Enter numbers you want to have in your listing (<Enter> to quit)")
    return nums

def main():
    print("This program calculates the inner product of two lists.\n Please enter two lists of the same size.")
    list1 = getthings()
    list2 = getthings()
    productlist = []
    if len(list1) != len(list2):
        print("Please enter two lists of the same size.")
    else:
        for i in range(len(list1)):
            product = list1[i]*list2[i]
            productlist.append(product)
        print("The inner product of the given lists is: ", productlist)

main()