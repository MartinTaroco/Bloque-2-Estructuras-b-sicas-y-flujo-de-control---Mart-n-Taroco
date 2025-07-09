#Desafío 2: Calcular promedio
#Crear un programa que lea 5 calificaciones y calcule su promedio


i = 5

suma = 0

while i >0:
  nota = int(input("Tu nota fue: "))
  suma += nota
  i -= 1  
promedio = suma / 5

print(promedio)


  