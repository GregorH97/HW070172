def getthings():
    nums = []
    xStr = input("Enter numbers you want to have in your listing (<Enter> to quit)")
    while xStr != "":
        x = int(xStr)
        nums.append(x)
        xStr = input("Enter numbers you want to have in your listing (<Enter> to quit)")
    return nums

def count(listing):
    x = 0
    for i in range(len(listing)):
        x = x + 1
    print("There are", x, "items in your listing.")

def isin(listing):
        search = input(int("Please enter which number you want to check to be in this listing."))
#
#   	for i in range(len(listing)):
#            x =1
#            if i == search:
#                print("The your entered number is in the listing.")
#            else:
#                print("Your searched number is not in the listing.")

def index(listing):
    search = input(int("Please enter which number you want to check the place in this listing."))
    for i in range(len(listing)):
        if listing[i] == search:
            print("The searched for number is at the", i +"th place in the listing.")
        else:
            print("Your searched number is not in the listing.")

def reverse(listing):
    reverselisting = []
    for i in range(len(listing)):
        x = listing[(i + 1)* (-1)]
        reverselisting.append(x)
    print("The reversed listing is: ", reverselisting)

def sort(listing):
    sortedlisting = []
    order = eval("Which order do you want your listing to have? Enter 'descending' or 'ascending'.")
    if order == "descending":
        for i in range(len(listing)):
            x = min(listing)
            sortedlisting.append(x)
            print("The newly ordered listing is:", sortedlisting)
    elif order == "ascending":
        for i in range(len(listing)):
            x = max(listing)
            sortedlisting.append(x)
            print("The newly ordered listing is:", sortedlisting)
    else:
        print("Please try again")

def main():
    print("This program can do a lot of operations with listings.")
    listing = getthings()
    method = input("Please enter what you want to do with that listing: 'count', 'isin', 'index', 'reverse', or 'sort'")
    if method == "count":
        count(listing)
    elif method == "isin":
        isin(listing)
    elif method == "index":
        index(listing)
    elif method == "reverse":
        reverse(listing)
    elif method == "sort":
        sort(listing)
    else:
        print("Please try ahain")
    
    
main()