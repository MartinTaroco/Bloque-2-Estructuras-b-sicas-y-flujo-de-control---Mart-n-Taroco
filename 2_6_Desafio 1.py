#Desafío 1: Calificaciones aprobadas
#Supón que estás analizando las calificaciones de los estudiantes y quieres saber cuántos aprobaron y cuántos desaprobaron. Se considera que una calificación de 7 o superior es aprobatoria y cualquier calificación menor a 7 es desaprobatoria. Utiliza lo que aprendiste sobre bucles y condicionales para resolver este problema.



calificaciones = [1, 4, 8, 10, 12, 4, 7, 11, 10, 8, 3, 9, 9]

aprobados = 0
reprobados = 0

for i in calificaciones:
  if i >= 7:
    aprobados += 1
  else:
    reprobados +=1

print(f"Se constata un total de {aprobados} aprobados y {reprobados} reprobados")