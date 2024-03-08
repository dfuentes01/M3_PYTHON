#la separacion de los floats es un punto (.).
#la division entre integers, el resultado es un float.

print(4/2) #2.0
print(5/2) #2.5
print(5/3.5) #1.4285714285714286
print(2.4*4) #9.6

nombre= "David"
apellido1= "Fuentes"
apellido2= "Pedreros"
año="2024"
print(3*nombre) #DavidDavidDavid
print(año*2) #20242024
#print(nombre/2) #no se puede dividir un string

#interpolacion de cadenas (otra forma de imprimir) print(f" {nombre_variable})
mes=3
dia=7

print(f"Hola {nombre}, El año es {año} del mes {mes} y el dia {dia}")

#string.format
#string.format
print("".format()) #estructura para trabajar con el string format.

#string.format
print("Hola {}, El año es {} del mes {} y el dia {}".format(nombre,año,mes,dia))

#interpolacion con % (%s para string y %d para numeros)
print("Hola %s, El año es %s del mes %d y el dia %d" %(nombre, año, mes,dia))

#Metodo count = cuenta cuantas veces se encuentra un caracter en un string
print("Saitama".count("a"))
print(nombre.count("i"))

#Metodo upper y lower = sirve para colocar string en mayusculas o en minusculas
print("Saitama".upper())# string en mayusculas #SAITAMA
print("Saitama".lower())# string en minusculas #saitama
print(nombre.upper()) #DAVID
print(nombre.lower()) #david

#Metodo title =sirve para colocar la primera letra en mayuscula aunque lo anteceda un numero
print("SAITAMA".title()) #Saitama
print(nombre.title()) #David

#Metodo len() = sirve para contar los caracteres incluidos los espacios.
print(len(" david fuentes 2024")) #19 #caracteres

#Metodo join() =sirve para unir string separados en un solo string con un caracter predeterminado, una coma y espacio en este ejemplo
print(", ".join(["David","Fuentes","Pedreros"])) #David, Fuentes, Pedreros
print("-/".join([nombre,apellido1,apellido2])) #David-/Fuentes-/Pedreros

#imprimir en mas de una linea (/n)
print("escribir\ncualquier\ncosa")
"""
escribir
cualquier
cosa
"""

#Valores Booleanos = True y False

#la variable se compone de un texto en minuscula, sin espacios o separados con un guion bajo, un signo igual y un valor numerico o texto entre "".
direccion= ""
mi_direccion= ""
cantidad_alumnos= 30
peso = 115.5
verdadero= True

#Tipo de datos type(nombre_variable)
#indica el tipo de variable. (string-integer-float-booleanos)

print(type(nombre)) #str
print(type(año)) #str
print(type(peso)) #float
print(type(mes)) #int
print(type(verdadero)) #bool

type(verdadero) #no imprime el tipo de dato por que falta el print "print(type(variable))"

#####Manipulacion de variables.#####

numero = 2
numero = numero + 3 #numero = 2 + 3 y se transforma en "numero = 5" se reasigna.
print(numero) #5

nombre = nombre + "Fuentes" #DavidFuentes se reasigna la variable "nombre" a DavidFuentes.

print(nombre)

#####Precision de datos#####

print(5/9) #0.5555555555555556
print(f"resultado de la division {5/9:.2f}") #0.56
print(f"resultado de la division {5/9:.5f}") #0.55556
print("el resultado de la division",round(5/9,3)) #0.556

#####Ingresando datos con input (en la consola)#####

input("ingrese su nombre:")

nombre = input("ingrese su nombre:")
print("Tu nombre es",nombre) #David
print(f"Tu nombre es {nombre}") #David

edad = input("ingrese su edad:")
print("Tu tienes",edad,"años")
print(type(edad)) #class 'str'



