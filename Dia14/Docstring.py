"""El docstring sirve para describir para que sirve el metodo creado """
# La recomendacion como buena practica es comentar los codigos realizados.

# Ejemplo
def elevar(base, exponente):
    """Esta funcion tiene como objetivo elevar la base a un exponente"""
    return base**exponente

# Otro Ejemplo

#Calculo del factorial de un numero.
def factorial (numero): #5! = 5*4*3*2*1
    """Este metodo calcula el factorial de un numero

    Args:
        numero (int)): numero sobre el cual se calculara el factorial.

    Returns:
        int : resultado del factorial de un numero 
    """
    valor = 1 #variable acumulable
    for n in range(1,numero+1): #1,2,3,4,5
        valor = valor * n
    return valor

factorial(5)
print("el factorial es", factorial(5))

#Calculo del Productoria de una lista de numeros.
def productoria (lista):
    """Este metodo calcula la productoria de una lista de numeros.

    Args:
        lista (int): El metodo devuelve el resultado de la productoria de una lista de numeros.

    Returns:
        int: resultado de la productoria de una lista de numeros
    """
    valor = 1
    for elemento in lista:
        valor *= elemento
    return valor
print(productoria([3, 6, 4, 2, 8]))

#Funcion para calcular los datos.
def calcular(**parametros): #*tupla; ** diccionario
    for clave, valor in parametros.items():
        if "fact" in clave: #busca un trozo del texto en una clave
            print(f"El factorial de {valor} es {factorial(valor)}")
        else:
            print(f"La productoria de {valor} es {productoria(valor)}")

calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)


#REFACTORIZACION


