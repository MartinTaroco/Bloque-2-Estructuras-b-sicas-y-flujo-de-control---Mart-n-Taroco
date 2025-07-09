#Desafío 2: Número de elementos pares en una lista
#Descripción: Escribe un algoritmo que cuente el número de elementos pares en una lista de números.

def pares(lista):
  pares = 0   #Cuenta inicia en 0
  for i in lista: #Iteramos en la lista de números dada
    if i % 2 == 0:   #Verificamos que el número sea par
      pares += 1      #Si identifica que el número es par suma 1 al contador.
  return pares


resultado = pares([1, 0, 4, 6, 8, 5, 9])

print(resultado)