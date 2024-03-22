# definición de un set
# Es una estructura de datos, se escriben entre llaves, no tienen clave, no permite datos repetidos.
# No hay un orden especifico, si se imprime varias veces, todas las veces cambia el orden.
# se puede trabajar con strings, datos numericos, floats.
# la diferencia con los diccionarios es que solo tienen valores y no claves.
# no se puede trabajar con listas y diccionarios.
# 
# se pueden ver que existen valores repetidos
muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra',2,2,2,2.5
}

# no hay duplicados, sólo valores únicos
print(muchos_animales) #{'Erizo de Tierra', 'Hurón', 'Perro', 'Hamster', 'Gato', 'Tortuga'} #desaparecieron los que se repétian.

# añadir datos al Set
muchos_animales.add(7) #se agrego el 7
print(muchos_animales) #{2, 2.5, 'Erizo de Tierra', 'Tortuga', 7, 'Perro', 'Hamster', 'Gato', 'Hurón'}

# remove
muchos_animales.remove("Hamster") #se elimina Hamster
print(muchos_animales) #{'Erizo de Tierra', 2, 2.5, 'Tortuga', 'Gato', 7, 'Perro', 'Hurón'}

# discard
muchos_animales.discard("Perro") #se descarta Perro
print(muchos_animales) #{'Hurón', 2, 2.5, 7, 'Erizo de Tierra', 'Gato', 'Tortuga'}

# pop
muchos_animales.pop() #elimina cualquier valor y lo devuelve en cualquier orden.
print(muchos_animales) #{2.5, 7, 'Hurón', 'Erizo de Tierra', 'Tortuga', 'Gato'}


# clear
muchos_animales.clear() #vacia el set
print(muchos_animales) #set()