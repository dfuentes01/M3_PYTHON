#Calculo del factorial de un numero.
def factorial (numero): #5! = 5*4*3*2*1
    valor = 1 #variable acumulable
    for n in range(1,numero+1): #1,2,3,4,5
        valor = valor * n
    return valor

factorial(5)
print("el factorial es", factorial(5))

#Calculo del Productoria de una lista de numeros.
def productoria (lista):
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


