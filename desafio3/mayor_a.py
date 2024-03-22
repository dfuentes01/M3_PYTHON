import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

umbral = int(sys.argv[1])
meses_mayor_a_umbral = {}

for mes, valor in ventas.items():
    if valor > umbral:
        meses_mayor_a_umbral[mes] = valor

print("Meses con ventas mayores a", umbral, ":")
print(meses_mayor_a_umbral)
