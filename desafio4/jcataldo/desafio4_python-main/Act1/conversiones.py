# Librerias
from sys import argv

# Variables
PEN = float(argv[1])
ARS = float(argv[2])
USD = float(argv[3])
CLP = int(argv[4])
DIV = {}

# Calculos
DIV["Soles"] = CLP*PEN
DIV["Pesos Argentinos"] = CLP*ARS
DIV["Dólares"] = CLP*USD

# Resultados
print(f"Los {argv[4]} pesos equivalen a:")
for k,v in DIV.items() :
    print(f"{v} {k}")