import sys

tasa_conversion_soles = float(sys.argv[1])
tasa_conversion_peso_argentino = float(sys.argv[2])
tasa_conversion_dolar_americano = float(sys.argv[3])
"""
#Valores de prueba tasas_conversion
tasa_conversion_soles = 0.0046
tasa_conversion_peso_argentino = 0.093
tasa_conversion_dolar_americano = 0.0013 #en los valores entregados hay un error en esta tasa. sobre 1 0
monto_peso_chileno = 10000
"""

monto_peso_chileno = int(sys.argv[4])
print(f"Los {monto_peso_chileno} pesos chilenos equivalen a:")

monto_soles = monto_peso_chileno * tasa_conversion_soles
monto_peso_argentino = monto_peso_chileno * tasa_conversion_peso_argentino
monto_dolar_americano = monto_peso_chileno * tasa_conversion_dolar_americano

print(f"{monto_soles} Soles")
print(f"{monto_peso_argentino} Pesos Argentinos")
print(f"{monto_dolar_americano} Dólares")
