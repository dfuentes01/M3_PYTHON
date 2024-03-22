"""
DICCIONARIOS:
-PAR -> {"CLAVE1":VALOR1, "CLAVE2":VALOR2 }
- la CLAVE debe ser unica, si la clave esta duplicada, se considerará el ultimo valor.


"""
    
#diccionario vacio
notas = {}    
#Creacion de un diccionario.
notas = {
"Camila":7, 
"Antonio": 7, 
"Felipe" : 6, 
"Antonia" : 7,
"Antonia" : 4,
"Antonia" : 3
} #Se puede ingresar el diccionario de manera horizontal o vertical , siempre clave : valor separados por comas.
    
print(notas)
    
#Acceder a los valores del diccionario
print(notas["Camila"]) #7
print(notas["Antonio"]) #7 
print(notas["Felipe"]) #6
print(notas["Antonia"]) #7
# print(notas["Mijail"]) #KeyError: 'Mijail'
# print(notas["felipe"]) #KeyError: 'felipe'

#agregar par clave:valor al diccionario
# diccionario[clave]=valor

notas["Mijail"]=7
print(notas["Mijail"]) #7

notas["felipe"]=3
print(notas["felipe"]) #3

#Cambiar el valor de una clave
notas["Felipe"] = 2
print(notas["Felipe"])

#Eliminar elementos del diccionario utilizando del.
del notas["Antonia"]
print(notas) #{'Camila': 7, 'Antonio': 7, 'Felipe': 2, 'Mijail': 7, 'felipe': 3}

#pop -> al eliminar, permite capturar el elemento.
eliminado = notas.pop("Antonio")
print(eliminado) #7
print(notas) #{'Camila': 7, 'Felipe': 2, 'Mijail': 7, 'felipe': 3}

#unir diccionarios

notas2 ={
"Alexis": 6,
"Yasna" : 6,
"Camila" : 3, #Reemplaza el valor de la clave duplicada en diccionario original.
}

# notas.update(notas2) #Agrego los datos del diccionario notas2 al diccionario notas.
# print(notas) #{'Camila': 7, 'Felipe': 2, 'Mijail': 7, 'felipe': 3, 'Alexis': 6, 'Yasna': 6}

notas2.update(notas) #Agrego los datos del diccionario notas al diccionario notas2.
print(notas2) #{'Alexis': 6, 'Yasna': 6, 'Camila': 7, 'Felipe': 2, 'Mijail': 7, 'felipe': 3}


