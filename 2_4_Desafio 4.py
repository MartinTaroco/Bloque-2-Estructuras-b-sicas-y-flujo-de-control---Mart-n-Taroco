#Desafío 4: Verificar múltiplos de varios números
#Objetivo: Determinar si un número dado es múltiplo de 2, 3, 5, 7, 9, 10, y 11 utilizando comparaciones y operadores lógicos.


def es_multiplo(n):
  lista = [2,3,5,7,9,10,11]
  for i in lista:
    if n % i == 0:
      print(f"{n} es múltiplo de {i} ")
    else:
      print (f"{n} NO es multiplo de {i}")
      

es_multiplo(30)