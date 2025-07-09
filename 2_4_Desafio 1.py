#Desafío 1: Clasificar numeros
#Dado tres números distintos, clasificarlos en orden ascendente utilizando comparaciones encadenadas y operadores lógicos.


i = 3
lista = []
while i > 0:
  numero = int(input("Dame un número: "))
  i -= 1
  lista.append(numero)

a = lista[0]
b = lista[1]
c = lista[2]

if a<b and a<c:
  print(f"{a} es el mas pequeño")

if (a > b and a < c) or (a > c and  b<c):
  print(f"{a} es el del medio")
  
if a > b and a > c:
  print(f"{a} es el mas grande")

print("-"*20) 
  
if b<a and b<c:
  print(f"{b} es el mas pequeño")

if (b > a and b < c) or (b < a and b > c):
  print(f"{b} es el del medio")
  
if b > a and b > c:
  print(f"{b} es el mas grande")

print("-"*20) 
  
if c<b and c<a:
  print(f"{c} es el mas pequeño")

if (c > b and c < a) or (c > a and  c<b):
  print(f"{c} es el del medio")
  
if c > b and c > a:
  print(f"{c} es el mas grande")