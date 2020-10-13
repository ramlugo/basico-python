def run():
    obejtivo = int(input("Escoge un entero: "))
    respuesta = 0


    while respuesta**2 < obejtivo:
        respuesta+= 1
    

    if respuesta**2 == obejtivo:
        print(f"La raíz cuadrada de {obejtivo} es {respuesta}")
    else:
        print(f"{obejtivo} no tiene raíz cuadrada exacta")


if __name__ == "__main__":
    run()