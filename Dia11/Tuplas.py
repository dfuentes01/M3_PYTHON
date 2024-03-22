from os import system

"""
-Una tupla no se puede modificar
-corchetes para las listas y llaves para los diccionarios.
-se puede agregar una tupla dentro de otra tupla
    
"""

tupla_eje = ("Marzo", "2024")
print(tupla_eje) #('Marzo', '2024')
print(type(tupla_eje)) #<class 'tuple'>

#desempaquetamiento
mes, anio = tupla_eje
print(mes) #Marzo
print(anio) #2024
print("")

"""
tupla1= 12,24,36,48,59 #agregando datos sin parentesis.
print(tupla2) #(3, 5, 7, 9)
print(type(tupla2)) #<class 'tuple'>
print("")
"""

tupla2= 3,5,7,9 #agregando datos sin parentesis.
print(tupla2) #(3, 5, 7, 9)
print(type(tupla2)) #<class 'tuple'>
print("")


tupla3= 3,5,(1,11),7,9 #Tupla anidada.
print(tupla3) #(3, 5, (1, 11), 7, 9)
print(type(tupla3)) #<class 'tuple'>
print("")

#crear una lista en tupla.
lista_vocales= ["a", "e", "i", "o", "u"]
print(lista_vocales) #['a', 'e', 'i', 'o', 'u']"
tupla_vocales = tuple(lista_vocales) #funcion tuple.
print(tupla_vocales) #('a', 'e', 'i', 'o', 'u')
print(type(tupla_vocales)) #<class 'tuple'>

#iterando una tupla = se puede realizar con el "for"
for tv in tupla_vocales:
    print(tv)
    """
    a
    e
    i
    o
    u
    """
    
print(tupla_vocales.count("a")) #1 #contando la cantidad de un elemento dentro de una tupla

###CONVERTIR DICCIONARIO EN UNA LISTA
lista_dicc=list({"k1": 5, "k2": 7}.items()) # [('k1', 5), ('k2', 7)]
print(lista_dicc) #[('k1', 5), ('k2', 7)]
print(lista_dicc[0]) #('k1', 5) #accediendo a tupla con la posicion cero
print(lista_dicc[0][1]) #5 accediendo a tupla con la posicion uno dentro de la tupla

###CONVERTIR LISTA EN DICCIONARIO
#internamente los elementos deben ser tuplas, una se transformara en clave y otra en valor.
# dict([('k1', 5), ('k2', 7)]) # {"k1": 5, "k2": 7}

print(dir(tupla_vocales)) #se puede ver que metodos o funciones se le pueden aplicar a un dato (string, float, int, lista, diccionario, etc.)

















