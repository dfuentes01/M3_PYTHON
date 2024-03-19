"""
for variable iterable    
"""

"""
#funcion range()
#valor de inicio es el cero [0-10]
for i in range(10):
    print(i)    #0,1,2,3,4,5,6,7,8,9
print("ejemplo1")


#valor de inicio es el 4 [4-10]
for i in range(4,10): 
    print(i) #4,5,6,7,8,9
print("ejemplo2")
    
#el tercer valor corresponde a la frecuencia [4-10]
for i in range(4,10,4): 
    print(i) #4,8
print("ejemplo3")
    
#todos los numeros pares del 1 al 20 [1-20]
for i in range(0,21,2): 
    print(i) #0,2,4,6,8,10,12,14,16,18,20
print("ejemplo4")

#todos los numeros pares del 1 al 20 [1-20] otro ejemplo con if
for num in range(1,21): 
    if num % 2 == 0:
        print(num) #0,2,4,6,8,10,12,14,16,18,20
print("ejemplo5")

#todos los numeros pares del 1 al 20 [1-20] con while
        
contador = 1        
while contador <=20:        
    if contador % 2 == 0:
        print(contador) #0,2,4,6,8,10,12,14,16,18,20
    contador+=2
print("ejemplo6_Sebastian")
"""
"""
####LISTAS ITERABLES####
# Una lista es un conjunto de datos, ordenados segun su ingreso, separados por coma
# el primer elemento, esta en la posicion 0
#lista.append = agregar elemento al final de la linea
lista= [1,5,8,3,4]
print("___LISTAS___")
for elemento in lista: #elemento=4
    print(elemento)


print("___STRING___")    
# String = Objeto
texto= "Hola mundo!!" 
for caracter in texto: #elemento=4
    print(caracter) #la variable reconoce el espacio como un caracter

# El tamaño de la lista es la cantidad de elementos    
opciones =["piedra", "papel", "tijeras"]
for opcion in opciones:
    print(opcion)
"""
"""
    DICCIONARIO {clave: valor,}
    - No existen las posiciones en un diccionario.    
"""
    
"""    
diccionario = {
    "Nombre" : "Carlos", 
    "Apellido": "Santana",
    "Ocupacion": "Guitarrista"
}    
print("___Diccionario___")
    
for clave in diccionario:
    print(clave)
print("___Diccionario2___") 
    
for clave in diccionario:
    print(f"clave {clave} - valor {diccionario[clave]}")
print("___Diccionario3___") 
    
for valor in diccionario.values():
    print(f"el valor es {valor}")        
print("___Diccionario4___") 
    
for clave, valor in diccionario.items():
    print(f"clave {clave} - valor {clave}")
print("___Diccionario5___")  
"""
    
#####TABLAS DE MULTIPLICAR####

for numero1 in range(11):
    print(f'\nTabla del {numero1}:------------------------------\n')
    for numero2 in range(1,11):
        print(f"{numero1} * {numero2} = {numero1*numero2}")
        
# for (let index = 0; index <10; index++) {
    # console.log(index)   
# }        
