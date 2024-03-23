#Importando el texto:
print("")
with open("C:/Curso_Python/0044-2/M3_Python/desafio4/lorem_ipsum.txt", "r") as file:
    texto=file.read()
print(texto)

#separando texto en caracteras
#creo una lista con los caracteres dentro del texto
print("")
caracteres = [caracter for caracter in texto]
print(caracteres)

#Transformo la lista en set para eliminar elementos duplicados
#Las letras en mayusculas y en minusculas son consideradas caracteres diferentes aunque sean la misma letra. 
print("")
set_caracter = set(caracteres)
print(set_caracter)

#Contando la cantidad de palabras
print("")
cantidad_caracteres = len(set_caracter)
print(cantidad_caracteres)
print(f"El número de caracteres distintos es: {cantidad_caracteres}")


#separando el texto en palabras.
print("")
palabras = texto.split()
print(palabras) #el resultado se muestra en una lista


#Transformo lista a Set para eliminar elementos duplicados
print("")
set_palabras = set(palabras)
print(set_palabras)

#Contando la cantidad de palabras
print("")
cantidad_palabras = len(set_palabras)
print(cantidad_palabras)
print(f"El número de palabras distintas es: {cantidad_palabras}")
