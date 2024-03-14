
"""
Determinar si un numero ingreso por el usuario
es par o inpar
utilizaremos el modulo
"""

# Paso1:abre tu editor de texto
# Paso2: solicitamos un valor al usuario de manera interactiva
numero = input("Ingrese el numero par o impar")

# Paso3: transformar string ingresado por el usuario a numeros
numero = int(numero)

# Paso4: evaluar con las condicionales

if numero%2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
    
    # Paso5: evaluar agragado elif e indicar cuando el numero es cero

if numero == 0:
    print("El numero es cero")
elif numero%2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

