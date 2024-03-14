#condicional if

"""
Si se cumple la condicion (True) ,
entonces se ejecuta el codigo
"""
#if condicion : #esta condicion debe ser verdadera.
    #codigo a ejecutar (tabulado a la derecha)
    
#Ejemplo

edad = input("¿Que edad tienes?\n")#17 -> se almacena "17"
edad = int(edad) #edad = int("17") -> edad = 17

#Si el usuario es mayor de edad o menor de edad
if edad >= 18: 
    print("Eres mayor de edad")    
    print("Programa terminado") 
    
    
#condicional else, para mas de una opcion como respuesta.

#if condicion :
#   Codigo a a ejecutar (tabulado a la derecha)
#else:
#   (entonces) Ejecutar el siguiente codigo

#Ejemplo.

if edad >= 18: 
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")  
    
print("Programa terminado") 

# condicional ELIF, vuelve a realizar una evaluacion.
# if condicion :
#   codigo a ejecutar (tabulado a la derecha)
# elif (otra condicion :)
#   Si se cumple esta nueva condicion se ejecutar el codigo
# else:
#   (entonces)Ejecutar el siguiente codigo
#edad==18; edad>18; edad<188

#Ejemplo.

if edad > 18: 
    print("Tu edad es mayor a 18")
elif edad == 18:
    print("Tu edad es igual a 18")    
else:
    print("Tu edad es menor a 18")  
    
print("Programa terminado") 