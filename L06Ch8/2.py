def main():
    v = 0
    while v <= 50:
        t = -20
        indexlist = []
        while t <= 60:
            index = 35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)
            indexlist.append(str(index))
            t = t + 10
        print(indexlist)
        v = v + 5
    eval(input("Press any key to exit the program,"))

main()

