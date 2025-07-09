#Desafío 3: Formateo de Factura
#Escriba un programa que pueda tomar los detalles de los productos (nombre, cantidad, precio) y produzca una factura bien formateada.

productos = [("TV", 4, 2500), ("Smartphones", 20, 500), ("Mouse", 15, 200)]

producto = input("Dime que quieres comprar: ")

if producto == "TV":
  print (f"Del producto TV, tenemos {productos[0][1]} unidades con un valor de {productos[0][2]} cada unidad")
  
if producto == "Smartphone":
  print (f"Del producto smartphone, tenemos {productos[1][1]} unidades con un valor de {productos[1][2]} cada unidad")
  
if producto == "Mouse":
  print (f"Del producto TV, tenemos {productos[2][1]} unidades con un valor de {productos[2][2]} cada unidad")