import random
import sys

# Verificar si se proporcionó un argumento válido
if len(sys.argv) != 2 or sys.argv[1] not in ["piedra", "papel", "tijera"]:
    print("Argumento inválido. Debe ser 'piedra', 'papel' o 'tijera'")
    print("Uso: python cachipun.py [piedra|papel|tijera]")
    sys.exit()

# Elección del usuario
eleccion_usuario = sys.argv[1]

# Opciones del juego
opciones = ["piedra", "papel", "tijera"]

# Elección aleatoria del computador
eleccion_computador = random.choice(opciones)

# Mostrar elecciones
print("Tu jugaste:", eleccion_usuario)
print("Computador jugó:", eleccion_computador)

# Determinar el resultado
if eleccion_usuario == eleccion_computador:
    print("Empate!")
elif (eleccion_usuario == "piedra" and eleccion_computador == "tijera") or \
    (eleccion_usuario == "papel" and eleccion_computador == "piedra") or \
    (eleccion_usuario == "tijera" and eleccion_computador == "papel"):
    print("¡Ganaste!")
else:
    print("¡Computador gana!")