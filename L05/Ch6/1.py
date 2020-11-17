def sing(animal, expression):
    print("Old MacDonald had a farm Ee-igh, Ee-igh, Oh!\nand on that farm he had a", animal,"Ee-igh, Ee-igh, Oh!\nwith a", expression +"-"+expression,"here and a", expression +"-"+expression, "there.\nHere a", expression, "there a", expression, "everywhere a", expression +"-"+expression, "\nOld MacDonald had a farm Ee-igh, Ee-igh, Oh!\n")


def main():
    sing("cow", "moo")
    sing("chicken", "cluck")
    sing("sheep", "baa")
    sing("pig", "oink")
    sing("duck", "quack")

    eval(input("Press any key to exit the program,"))
   
main()    