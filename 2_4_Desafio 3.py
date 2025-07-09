#Desafío 3: Convertidor de temperaturas
#Realizar conversiones de una temperatura dada en Celsius a Fahrenheit y Kelvin utilizando operaciones directas sobre las variables. Los cálculos se realizarán directamente al asignar los valores a las variables.

temperatura_c = float(input("Dame una temperatura en celcius: "))
print(f"La temperatura en celsius es {temperatura_c}")

temperatura_f = temperatura_c * (9/5) + 32

print(f"La temperatura en fahrenheit es {temperatura_f}")

temperatura_k= temperatura_c + 273.15

print(f"La temperatura en kelvin es {temperatura_k}")