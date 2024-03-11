import math

P = float(input("Ingrese el Precio de Suscripción: "))
U = float(input("Ingrese el Numero de Usuarios: "))
GT= float(input("Ingrese el Gasto Total: "))
U_anterior= float(input("Ingrese las Utilidades del año Anterior: "))
utilidades_actuales = (P*U-GT)
razon_utilidades= utilidades_actuales/U_anterior

print("La razon entre las utilidades actuales y las del año enterior es", razon_utilidades)
