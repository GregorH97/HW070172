from math import sqrt

def getnumbers():
    nums = []
    xStr = input("Enter a number (<Enter> to quit)")
    while xStr != "":
        x = float(xStr)
        nums.append(x)
        xStr = input("Enter a number: ")
    return nums

def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total/len(nums)

def StdDev(nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = num - xbar
        sumDevSq = sumDevSq + dev*dev
    return sqrt(sumDevSq/len(nums) -1)

def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size//2
    if size%2 == 0:
        med = (nums[midPos] + nums[midPos -1]) /2.0
    else:
        med = nums[midPos]
    return med

def main():
    print("This program computes mean and standard deviation")
    data = getnumbers()
    xbar = mean(data)
    method = input(str("Please enter which method you want to use. Enter 'mean' if you want to get the mean, enter 'StdDev' if you want to get the Standard deviation, or enter 'meanStdDev' if you want to have both. "))
    if method == "mean":
        solution = mean(data)
        print("The mean is: ", solution)
    elif method == "StdDev":
        solution = StdDev(data, xbar)
        print("The solution is: ", solution)
    elif method == "meanStdDev":
        solution1= mean(data)
        solution2= StdDev(data, xbar)
        print("The solutions are:", solution1, "and", solution2)
    else:
        print("Please try again")

if __name__ == '__main__': main()