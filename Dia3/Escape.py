import math

r_km = float(input("Ingrese el radio del planeta en kilometros: "))
g = float(input("Ingrese la constante g: "))
r_m = r_km*1000

Velocidad_de_escape = math.sqrt(2*g*r_m)
print("La velocidad de Escape es {:.1f} [m/s]".format(Velocidad_de_escape))