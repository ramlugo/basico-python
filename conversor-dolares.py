dolares = input("¿Cuántos dólares tienes?:")
dolares = float(dolares)
valor_dolar = 22.547
pesos_mx = dolares * valor_dolar
pesos_mx = round(pesos_mx, 2)
pesos_mx = str(pesos_mx)
print("Tienes $" + pesos_mx + " pesos mexicanos")