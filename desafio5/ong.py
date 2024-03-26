import sys

def factorial(n):
    
    #Calcula el factorial de un número entero positivo n.
    
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def productoria(lista):
    
    #Calcula la productoria de los elementos de una lista.
   
    result = 1
    for num in lista:
        result *= num
    return result

def calcular(**kwargs):

# Controla los cálculos según los argumentos proporcionados.
    for key, value in kwargs.items():
        if key.startswith('fact_'):
            n = int(value)
            print(f"El factorial de {n} es {factorial(n)}")
        elif key.startswith('prod_'):
            lista = value
            print(f"La productoria de {lista} es {productoria(lista)}")
        else:
            print(f"Argumento '{key}' no reconocido")

# Ejemplo de uso
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
