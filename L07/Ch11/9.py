def gettuples():
    tuples = []
    gpa = input("Enter the gpa of the student (<Enter> to quit)")
    student = input("Enter the name of the student with this gpa (<Enter> to quit) ")
    while gpa != "":
        x = int(gpa)
        tuples.append((x, student))
        gpa = input("Enter numbers you want to have in your listing (<Enter> to quit) ")
        student = input("Enter the name of the student with this gpa (<Enter> to quit) ")
    return tuples

def main():
    print("This program orders students according to their gpa.")
    list = gettuples()
    list.sort()
    print(list)

main()