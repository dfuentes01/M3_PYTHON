"""
Funciones

-def nombre_de_la_fucnion():
    #codigo a ejecutar

-La funcion debe definirse previo ante de llamarla.
-Es imperativo utilizar los () en el llamado a la funcion, sino no se ejecutara.

"""

print("Inicio")
# imprimir_menu() no se puede llamar a una funcion que no este definida previamente, la moveremos luego de definir la funcion.

#definicion de la funcion. se recomienda realizar estas definiciones al principio del codigo.-
def imprimir_menu():
    print("Opciones: ")
    print("1). De acuerdo")
    print("2). En desacuerdo")
    print("3). No me interesa")

#llamado a ala funcion (invocacion), aqui si funciona por que ya se definio la funcion.
imprimir_menu() 
imprimir_menu() #se vuelve a llamar la funcion
imprimir_menu() # nuevamente la llamamos.

print("Fin")

##DRY = Dont Repeat Yourself. principio basico en el diseño que busca evitar la redundancia de codigo.
# si tengo que copiar y pegar un trozo de codigo 2 o más veces es muy probable que necesite crear una funcion.

##PARAMETROS Y ARGUMENTOS.

"""
-Parametro: es la variable a utilizar en la funcion.
-argumento: valor que sera pasado en el llamado de la funcion.
-cuando hacemos un return multiple se devueve una tupla
"""

#definiendo la funcion
def suma (valor1 , valor2): #valor1=3 valor2=5
    suma = valor1 + valor2 #suma = 3 + 5; suma = 8
    return suma #return 8

def suma2(valor1,valor2): #misma funcion simplificada.
    return valor1 + valor2
    print(qwerty123456) #nunca se imprimira por estar despuest de "return"

#llamando a la funcion
suma(3,5) #capturando el resultado
print("valor respuesta capturado",suma2(1,9)) #imprimiendo el valor de retorno.

resultado = suma(6,7) #capturando el valor de retorno.
print("valor respuesta capturado", resultado) #imprimiendo el valor de retorno.


##Retorno Multiple
def cuadrado_cubo(base):
    cuadrado = base** 2
    cubo = base ** 3
    return cuadrado, cubo

print(cuadrado_cubo(2)) #retorno de una tupla (4, 8)

valor_cuadrado, valor_cubo = cuadrado_cubo(3)
print(valor_cuadrado,valor_cubo)


precios = {'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar(diccionario, umbral): #diccionario = precios
    filtro = {k:v for k,v in diccionario.items() if v > umbral}
    return filtro

print(filtrar(precios, 12000))

"""

def extremo_multiplicando(lista,factor):
    minimo = min(lista)
    maximo = max(lista)
    return factor*minimo, factor*maximo
# print(extremo_multiplicado(4,[1,2,3,4])) no funciona por que requiere elementos iterables.
print(extremo_multiplicado([1,2,3,4], 4))


    print(args[2])

argumentos(23,"hola,[2,3,4,5,6])

"""

#VARIABLES LOCALES Y VARIABLES GLOBALES

pais = "Chile" #variable global, existen variables consantes que podrian utilizarse ya que no varian (ej. valor de pi, el rho del cobre, constantes, etc.)
# se recomienda establecer variables globales que sean constantes al inicio del codigo luego de la importacion de bibliotecas.

def ciudades():
    #scope de la variable "capital" es solo en el metodo cidades()
    capital = "Santiago"
    print(pais,capital)
    # pais = "Peru" / no se puede, recomiendo modificar el valor de una variable global.
    return capital # lo que se retorna es el contenido de la variable, no la variable."Santiago"

print(pais)
ciudades() #se invoca la variable.
# print(capital) #variable no definida.















