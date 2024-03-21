"""
lista: conjunto de datos, ordenados segun su ingreso, separados por coma, 
el primer elemento, esta en la posicion cero, pueden contener distintos tipos de elementos,
son mutables
se usan los [] para definir una variable de tipo lista
**indice=> la posicion de los elementos

la primera posicion SIEMPRE es CERO
la ultima posicion esta dada por la ultimaPosicion= (cantidad_elementos -1) o lista[-1]
para acceder a los elementos ultilizamos las posiciones; lista[posicion]
no existen indices sin elementos en python
los metodos con __nombre__, se les llama magic build-in o dundees
"""

lista1 = [1,2,3,4]
print(f"la lista es: {lista1}")
print(f"nueva lista{[5,"Hola Mundo",7]}")


colores = ["verde", "rojo", "rosa", "azul"]
#cuantos elementos tiene : 4 -> el tamaño de la lista.
# la ultima posicion = 4-1 ->3
print(colores[0]) #verde
print(colores[1]) #rojo
print(colores[2]) #rosa
print(colores[3]) #azul
# print(colores[4]) #IndexError: list index out of range
print(colores[-1]) #azul
print(colores[-2]) #rosa
# print(colores[-5]) #IndexError: list index out of range

##METODOS
# print(colores.__dir__()) #mostrar todos los metodos que contiene la lista

#append() -> agregar un elemento al final de la lista
colores.append("amarillo") #agregar un elemento
print(colores) #['verde', 'rojo', 'rosa', 'azul', 'amarillo']

#insert(indice, elemento) ->agregar el elemento en una posicion especifica
# y su esta utilizada por otro elemento, este es despazado en una posicion mas

colores.insert(0, "blanco")
print(colores) #['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo']
colores.insert(6, "negro") #agregar en la posicion final de la lista
print(colores) #['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo', 'negro']

colores.insert(8, "cafe") #si la indice no existe, se le asigna la ultima posicion
print(colores) #['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo', 'negro', 'cafe']        
colores.insert(0, "cafe")
print(colores) #['cafe', 'blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo', 'negro', 'cafe']

#pop([indice])-> elimina un elemento dentro de la lista
colores.pop(1) #elimino blanco de la lista, en posicion 0
print(colores) #['cafe', 'verde', 'rojo', 'rosa', 'azul', 'amarillo', 'negro', 'cafe']]

colores.pop(3) #elimino azul de la lista, en posicion 3
print(colores) #['cafe', 'verde', 'rojo', 'azul', 'amarillo', 'negro', 'cafe']

#remove()
colores.remove("cafe") #elima el primer "cafe" que encuentre
print(colores) #['verde', 'rojo', 'azul', 'amarillo', 'negro', 'cafe']
# colores.remove("cafes") #ValueError: list.remove(x): x not in list

#reverse() -> invierte el orden de los elementos de la lista, permanente.
colores.reverse()
print(colores) #['cafe', 'negro', 'amarillo', 'azul', 'rojo', 'verde']

#sort() -> ordena los elementos de forma ascendente por defecto
colores.sort() #ordeno alfabeticamente en orden ascendente.
print(colores) #['amarillo', 'azul', 'cafe', 'negro', 'rojo', 'verde']



lista2 = lista1
print(lista2)
lista2.append(5)
print(f"lista2 {lista2}")
print(f"lista1 {lista1}")

"""
En Python, cuando asignas una lista a otra variable utilizando el operador
de asignación (=), estás creando una nueva referencia a la misma lista en
la memoria, no una nueva lista. Por lo tanto, ambas variables 
(lista1 y lista2) apuntan a la misma ubicación de memoria, lo que significa
que cualquier cambio realizado en una de las variables también afectará a la otra.

Si quieres crear una copia independiente de la lista, puedes usar el método copy()
o hacer una copia mediante slicing. Aquí tienes cómo hacerlo:
"""

lista3 = lista1.copy() #esto si es un respaldo de los datos.
print(f"lista3 {lista3}")

lista4 = lista1[:]
print(f"lista4 {lista4}")

lista5 = list(lista1) #tambien funciona para respaldar. funcion list.
print(f"lista5 {lista5}")

lista7 = lista1 + [] #tambien sirve para respaldar una lista de manera no tan limpia.
lista8 = lista7 * 1 #tambien sirve para respaldar una lista de manera.

#sorted(lista, reverse = True) -> ordena descendente, no es permanente 
# sorted(colores,reverse=True) #ordeno alfabeticamente en orden ascendente.
print(sorted(colores,reverse=True)) #['verde', 'rojo', 'negro', 'cafe', 'azul', 'amarillo'], no es permanente este orden.
print(colores) #['amarillo', 'azul', 'cafe', 'negro', 'rojo', 'verde']

#index()-> retorna el indice del elemento
print(colores.index('azul')) #1
print(colores.index('negro')) #3
# print(colores.index('pink')) #ValueError: 'pink' is not in list

colores.clear() #elimina todos los elementos de la lista
print(colores) #lista vacia, tamaño 0
print(len(colores)) #tamaño 0

##OPERACIONES

lista6 = [20,30,40,50]
lista_concatenada = lista1 + lista6
print(lista1) #[1, 2, 3, 4, 5]
print(lista6) #[20, 30, 40, 50]
print(lista7) #[1, 2, 3, 4, 5] lista 1 respaldada.
print(lista8) #[1, 2, 3, 4, 5] lista 1 respaldada.
print(lista_concatenada) #[1, 2, 3, 4, 5, 20, 30, 40, 50]
lista6.append(60)
print(lista_concatenada) #[1, 2, 3, 4, 5, 20, 30, 40, 50]
