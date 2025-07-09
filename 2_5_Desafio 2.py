#Desafío 2: Calculadora Simple
#Escriba un programa que pida al usuario que ingrese dos números y luego imprima la suma, la resta, la multiplicación y la división de #esos números.


def calculadora(a,b, operacion):
  num = 0
  op = str(operacion)
  if op == "+":
     num = a + b
  elif op == "-":
   num = a - b 
  elif op == "*":
    num = a * b  
  return num


cuenta = calculadora(2,4,"*")

print(cuenta)

