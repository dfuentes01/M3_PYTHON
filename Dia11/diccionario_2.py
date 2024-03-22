notas = {
"Camila" : 7,
"Antonio" : 7,    
"Felipe" : 6,
"felipe" : 7,
"Antonia" : 6,            
}




#print(notas[2]) #KeyError:2
#print(notas["FELIPE"]) #KeyError: FElipe
print(notas.get("FELIPE")) #None
print(notas["Felipe"]) #6
print(notas.get("Camila")) #7
print(notas.get("Mijail", "valor no encontrado")) #valor no encontrado

prueba = notas.get ("Julio")
print(prueba) #None
print(type(prueba)) #<class 'NoneType'

#Agregar
notas["Israel"] = "FullStack Python"
print(notas) 
#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'felipe': 7, 'Antonia': 6, 'Israel': 'FullStack Python'}
notas["Israel"]=4
print(notas) #{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'felipe': 7, 'Antonia': 6, 'Israel': 4}
print("")
notas.setdefault("Juan",10) #Se agrego una nueva clave y valor.
#cuando la clave ya existe y se intenta agregar nuevamente, devuelve el valor actual. No lo reemplaza.
print(notas) #{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'felipe': 7, 'Antonia': 6, 'Israel': 4, 'Juan': 10}
print("")
notas.setdefault("Juan",2)

print(notas) #{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'felipe': 7, 'Antonia': 6, 'Israel': 4, 'Juan': 10}
print("")
notas.setdefault("Valeria")
print(notas) #{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'felipe': 7, 'Antonia': 6, 'Israel': 4, 'Juan': 10, 'Valeria': None}

print("")
del notas ["felipe"]
print(notas) #{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 6, 'Israel': 4, 'Juan': 10, 'Valeria': None}, del elimina enseguida la clave.

print("")
eliminado = notas.pop("Antonio")
print(eliminado) #7
print(notas) #{'Camila': 7, 'Felipe': 6, 'Antonia': 6, 'Israel': 4, 'Juan': 10, 'Valeria': None

eliminados={}
#eliminados = eliminados.setdefault(notas.pop("Camila"))
eliminados["Camila"] =  notas.pop("Camila")
print(eliminados) #{'Camila': 7} 
print("")

tupla1=notas.popitem() #elimina y devuelve la tupla(clave:valor) del ultimo elemento, en este caso "Valeria"
print(tupla1) #('Valeria', None)
print(notas) #{'Felipe': 6, 'Antonia': 6, 'Israel': 4, 'Juan': 10}
#Tupla : similar a las listas pero inmutables (valor1,valor2...), no se pueden modificar.
print(tupla1[0]) #Valeria
print(tupla1[1]) #None
# tupla1[1] = "Mishi" #TypeError: 'tuple' object does not support item assignment
print("")

notas.clear() #elimina los elementos, dejando diccionario vacio.
print(notas) #{}
print("")

###comparar diccionarios
dic1 = {1:"uno", 2:"dos",}
dic2 = {2:"dos", 1:"uno",}
dic3 = {2:"dos", 3:"tres",}
dic4 = {2:"dos", 3:"Cuatro",}
print(dic1==dic2) #True
print(dic1==dic3) #False
print(dic4==dic3) #False

##DICCIONARIOS ANIDADOS

pares_impares ={
    "pares" : {2:"dos",4:"cuatro",6:"seis",8:"ocho",10:"diez"},
    "impares" : {"uno":1,"tres":3,"cinco":5,"siete":7,"nueve":9},
}

#imprimir el valor "seis"
print(pares_impares["pares"][6])

#imprimir el valor 5
print(pares_impares["impares"]["cinco"])

#System.clear -> limpiar la terminal
# system("clear")

######################################FIN PRIMER MODULO.
#PRINCIPIO SEGUNDO MODULO.######################################
computador = {
'notebook': 489990,
'tablet': 120000,
'cargador': 12400,
}

print (computador.keys()) #dict_keys(['notebook', 'tablet', 'cargador'])
for elemento in computador.keys(): #dict_values([489990, 120000, 12400])
    print(elemento)    

print("Elemplo1")
print(computador.values())

print("Elemplo2")
print(computador.keys())
for key in computador.keys():
    print(key) #dict_keys(['notebook', 'tablet', 'cargador'])
#notebook
#tablet
#cargador

print("Elemplo3")
print(computador.values())
for valor in computador.values():
    print(valor) #dict_values([489990, 120000, 12400])
#489990
#120000
#12400

print("Elemplo4")
print(computador.items())
for clave,valor in computador.items():
    print(clave,valor) #dict_items([('notebook', 489990), ('tablet', 120000), ('cargador', 12400)])
#notebook 489990
#tablet 120000



