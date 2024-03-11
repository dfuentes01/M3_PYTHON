import math

P_normal = float(input("Ingrese el Precio de Suscripción para usuarios normales: "))
U_normal = float(input("Ingrese el Numero de Usuarios normales: "))

P_premium = 1.5 * P_normal
U_premium = float(input("Ingrese el Numero de Usuarios premium: "))


GT= float(input("Ingrese el Gasto Total: "))

utilidades = (P_normal * U_normal + P_premium * U_premium) - GT
print("Las utilidades son", utilidades)