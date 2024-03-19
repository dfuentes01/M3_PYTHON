
#### Transformando un ciclo for en un Comprehension####
# solicitamos el número de pares a generar
n=10
# generamos una lista vacía para almacenar los pares, el tamaño es 0
lista_par = []
print(len(lista_par))

for i in range(n):
# podemos hacer append de los valores generados
# en este caso partimos desde el 2
    lista_par.append(2*i + 2) #lo que hace es agregar un elemento al final de la lista
    print(f"lista_par {lista_par}")
    
# mostramos el resultado
print(lista_par)
print("ejemplo1")

##COMPREHENSION###
# [formula for variable in iterable]
lista_par = [2*i + 2 for i in range(n)]
print(lista_par)
print("ejemplo2")


####Condicionales con List Comprehensions####

valores = [0,4,5,6,7,8,9]
divisibles = []
for valor in valores:
    if valor % 2 == 0:
        divisibles.append('Divisible')
    else:
        divisibles.append('No Divisible')
    print("Divisible")     
    print("No Divisible")        
print("ejemplo3")

divisibles2= ['Divisible' if valor % 2 == 0 else 'No Divisible' for valor in valores ]
print(divisibles2)
print("ejemplo4")

####Operaciones de filtrado####

lista = ["Lechugas", "Tomates", 5, 10, True, False, True, "Papas", 5.1, 45.2, 1, 2, 0]
count_str = 0
lista_str = []
for elemento in lista:
    if type(elemento) is str:
        count_str += 1
        lista_str.append(elemento)
        
print(f"cantidad de string {count_str}")
print(f"cantidad de string {len(lista_str)}")

print("ejemplo5")
#TAREA CREAR LIST COMPREHENSION#

#Se realiza el ejemplo5 en una sola linea


###DICTIONARY COMPREHENSIONS###

claves = ['nombre','apellido','edad','altura']
valores = ['Juan','Pérez', 33, 1.75]
diccionario2 = ({k:v for k,v in zip(claves, valores)}) #{'nombre': 'Juan', 'apellido': 'Pérez', 'edad': 33, 'altura': 1.75}
print(diccionario2)
print("ejemplo6")

###Transformando segundos a minutos###

segundos = [100, 50, 1000, 5000, 1000, 500]
#convertir minutos a segundos
minutos = [segundo// 60 for segundo in segundos]
print(minutos)
print("Ejercicio Final clase")



