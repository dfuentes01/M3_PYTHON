import getpass
from string import ascii_lowercase

password = getpass.getpass("Ingrese la contraseña: ").lower()

letras = ascii_lowercase
intentos = 0
longitud_password = len(password)

for letra in letras:
    intentos += 1
    if letra == password[0]:
        print(f"{letra} es igual a {password[0]} => Sí ({intentos} intentos), continúa con la siguiente letra.")
        break

for i in range(1, longitud_password):
    for letra in letras:
        intentos += 1
        if letra == password[i]:
            print(f"{letra} es igual a {password[i]} => Sí ({intentos} intentos), continúa con la siguiente letra.")
            break

print(f"La Contraseña. fue forzada en {intentos} intentos.")
print(f"La contraseña es {password}")

