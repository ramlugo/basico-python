numero_1 = """Un número primo debe ser divisible entre dos números: 
entre el número 1 y entre sí mismo; por lo tanto, 
el número 1 no es un número primo. """


bienvenida = """¡Hola! Me llamo Joaquín y puedo ayudarte 
a saber si un número es primo o no"""


def es_primo(numero):
    if numero == 1:
        return False    
    else:
        contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    print(bienvenida)
    numero = int(input("Para continuar, escribe un número: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()