def main():
    print("This is program computes the average of three exam scores.")
    score1, score2, score3 = eval(input("Enter three scores seperated by a comma: "))
    average = (score1 + score2 + score3)/3
    print("The average is:", average)
main()