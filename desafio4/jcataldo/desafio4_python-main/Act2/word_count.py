#

# Librerias
from sys import argv

# Importando el texto:
with open(str(argv[1]), "r") as file:
    texto=file.read()

# separando texto en caracteras
# creo una lista con los caracteres dentro del texto
caracteres = [caracter for caracter in texto]

# Transformo la lista en set para eliminar elementos duplicados
# Las letras en mayusculas y en minusculas son consideradas caracteres diferentes aunque sean la misma letra. 
set_caracter = set(caracteres)

# Contando la cantidad de palabras
cantidad_caracteres = len(set_caracter)
print(f"El número de caracteres distintos es: {cantidad_caracteres}")


# separando el texto en palabras.
palabras = texto.split()

#Transformo lista a Set para eliminar elementos duplicados
set_palabras = set(palabras)

#Contando la cantidad de palabras
cantidad_palabras = len(set_palabras)
print(f"El número de palabras distintas es: {cantidad_palabras}")
