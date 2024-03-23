import sys
from os import system

conversion = [float(sys.argv[i]) for i in range(1, 4)]
pesosChilenos = float(sys.argv[4])

conversiones = [pesosChilenos * convierte for convierte in conversion]

system('cls')

# Imprimir los resultados de las conversiones
print(f'Los {pesosChilenos} pesos equivalen a:')
print(f'{conversiones[0]} Soles')
print(f'{conversiones[1]} Pesos Argentinos')
print(f'{conversiones[2]} Dólares')