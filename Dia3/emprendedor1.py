import math

P = float(input("Ingrese el Precio de Suscripción: "))
U = float(input("Ingrese el Numero de Usuarios: "))
GT= float(input("Ingrese el Gasto Total: "))

utilidades = (P*U-GT)
print("Las utilidades son", utilidades)