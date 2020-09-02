def run():
    name1 = input("Escribe tu nombre: ")
    age1 = int(input("Escribe tu edad: "))
    name2 = input("Escribe tu nombre: ")
    age2 = int(input("Escribe tu edad: "))


    if age1 > age2:
        print(name1 + " es más grande que " + name2)
    elif age1 < age2:
        print(name2 + " es más grande que " + name1)
    else:
        print(name1 + " y " + name2 + " tienen la misma edad")




if __name__ == "__main__":
    run()