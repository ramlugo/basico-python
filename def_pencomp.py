def run():
    def suma(a, b):
        total = a + b
        return total

    var_a = int(input("Escribe un número entero: "))
    var_b = int(input("Escribe otro número entero: "))
    print("La suma de estos dos números es: ")
    print(suma(var_a, var_b))


if __name__ == "__main__":
    run()