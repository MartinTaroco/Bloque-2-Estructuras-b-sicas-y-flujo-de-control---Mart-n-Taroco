## Desafío 3: Simulación de una carrera de autos

#Vas a simular una carrera de autos. Cada auto tiene una velocidad aleatoria (puedes usar la biblioteca random de Python) y cada ciclo del bucle representa un segundo de la carrera. Al final de cada segundo, cada auto avanza una distancia igual a su velocidad. La carrera dura 10 segundos. Al final de la carrera, debes imprimir el auto ganador. Si hay un empate, debes imprimir todos los autos que empataron.



import random as rd


#Me gemnera números menores que 1
numero1 = rd.random()
numero2 = rd.random()
numero3 = rd.random()
numero4 = rd.random()

#Genero velocidades formateando el número random que obtuve
velocidad1 = int(numero1*100)  
velocidad2 = int(numero2*100)
velocidad3 = int(numero3*100)
velocidad4 = int(numero4*100)

#Autos inician en 0
auto1 = 0
print(auto1)
auto2 = 0
print(auto2)
auto3 = 0
print(auto3)
auto4 =0
print(auto4)

print("-"*20)
segundos = 10


while segundos >= 0:
  auto1 += velocidad1
  print(auto1)
  auto2 += velocidad2
  print(auto2)
  auto3 += velocidad3
  print(auto3)
  auto4 += velocidad4
  print(auto4)
  
  print("-"*20)
  segundos -= 1  

  
resultados =[(auto1,"Auto1" ), (auto2, "Auto2"), (auto3, "Auto3"),(auto4,"Auto4")]
resultados.sort(reverse=True)  #Ordena la lista poniendo el auto con mayor velocidad primero

mayor_distancia = resultados[0][0]
for i in range(1,4):
  if mayor_distancia == resultados[i][0]:
    print(f"otro ganador fue {resultados[i][1]}")

print(resultados)

print(f"El Ganador es {resultados[0][1]}")

