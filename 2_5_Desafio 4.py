#Desafío 4: Conversor de Moneda
#Escriba un programa que solicite al usuario que ingrese una cantidad en su moneda local y luego convierta esa cantidad a otra moneda usando una tasa de cambio proporcionada. El programa debe manejar la entrada de datos y formatear la salida adecuadamente.

cantidad_pesos = float(input("Que cantidad en pesos queres convertir: "))

cantidad_dolares = cantidad_pesos / 41

print(f"Tus {cantidad_pesos} $ equivalen a {cantidad_dolares} U$S")