def run():
    contador_externo = 0
    contador_interno = 0

    while contador_externo < 12:
        while contador_interno < 12:
            print(contador_externo ,contador_interno)
            contador_interno += 1 #contador = contador + 1

            if contador_interno >= 6:
                break

        contador_externo += 1
        contador_interno = 0


if __name__ == "__main__":
    run()