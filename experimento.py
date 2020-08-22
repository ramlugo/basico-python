def run():
    name = input('Escribe tu nombre: ')
    saludo = '¡Hola ' + name + '!, el número de caracteres de este enunciado es'
    print(saludo, len(saludo))


if __name__ == "__main__":
    run()