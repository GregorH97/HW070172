from gpa import Student, makeStudent

def readStudents(filename):
    infile=open(filename, 'r')
    students=[]
    for line in infile:
        students.append(makeStudent(line))
    infile.close
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".
            format(s.getName(), s.getHours(), s.getQPoints),
            file = outfile)
    outfile.close()

def main():
    print("This program sorts students by grade, name or credits.")
    filename = input("Enter the name of the data file")
    data = readStudents(filename)
    method = input("Please enter by which criteria you want to sort: 'grade', 'name', or 'credits'")
    if method == "grade":
        data.sort(key=Student.gpa)
        filename = input("Enter a name for the output file: ")
    elif method == "name":
        data.sort(key=Student.getName)
        filename = input("Enter a name for the output file: ")        
    elif method == "credits":
        data.sort(key=Student.getQPoints)
        filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __main__ == '__main__': main()