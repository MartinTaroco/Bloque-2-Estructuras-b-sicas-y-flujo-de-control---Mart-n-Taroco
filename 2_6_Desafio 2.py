#Desafío 2: Mejora del cálculo
#Toma el ejemplo del cálculo del promedio de calificaciones y mejóralo. En lugar de pedir las calificaciones una por una, modifica el código para pedir todas las calificaciones al mismo tiempo (el estudiante puede ingresar las calificaciones separadas por comas) y luego calcular el promedio.


i = 1
sumatoria_notas= 0 

while i > 0:
  calificaciones = input("escribe tus calificaciones, separalas con una coma: ")

  lista_notas = calificaciones.split(",")  #Lista con notas, separandola teniendo en cuenta la coma
  for n in lista_notas:
    nota = int(n)     #Transforma cada nota de str a int
    sumatoria_notas += nota    #Las agrega a la variable
    
  print(f"Tu promedio es {sumatoria_notas / len(lista_notas)}")
  i -= 1  #Detiene el bucle