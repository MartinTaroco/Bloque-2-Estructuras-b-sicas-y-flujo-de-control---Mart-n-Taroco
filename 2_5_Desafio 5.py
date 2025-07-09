#Desafío 5: Contador de Palabras
#Escriba un programa que permita al usuario ingresar un texto y luego cuente y muestre la cantidad de palabras que contiene el texto. El programa debe manejar la entrada de datos y formatear la salida adecuadamente.

texto = input("Escribe un texto: ")

lista_auxiliar = texto.split()  #Separo el texto teniendo en cuenta los espacios entre palabras como referencia

contador = 0 
for i in lista_auxiliar:
 contador += 1


print(contador)