#Desafío 5: Calculadora de Módulo
#Escribe un programa que defina dos variables enteras a y b. Utiliza el operador de módulo (%) para calcular el residuo de la división de #a entre b, y luego imprime el resultado. Asegúrate de que el programa maneje adecuadamente el caso en que b sea cero, imprimiendo un #mensaje de error en ese caso.


print("A Continuación se solicitará dos enteros para dividir al primero entre el segundo")

i = 1
lista = []
while i > 0:
  primer_numero = int(input("Dame un entero: "))
  
  lista.append(primer_numero)
  
  segundo_numero = int(input("Dame un número: "))
  
  if segundo_numero != 0:
    lista.append(segundo_numero)
  else:
    print("El divisor no puede ser 0")
  
  i -= 1

if len(lista) == 2:
  a = lista[0]
  b = lista[1]
  c = a % b
  print(c)
  