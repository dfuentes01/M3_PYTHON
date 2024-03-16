import getpass

"""
password = getpass.getpass("Ingrese la clave secreta: ") #getpass permite teclar la clave sin que se vea.
# print(f"el password capturado {password}") #solo para testear la funcion .getpass


while password != "hola mundo" :
    password = getpass.getpass("Password incorrecto, intente nuevamente: ")
print("Fin del Programa")


numero = int(input("Ingrese un numero entero del 1 al 100: "))


while numero < 1 or numero > 100:
    numero = int(input("Ingrese un numero entero del 1 al 100: "))

while numero != 33:
    numero = int(input("Ingrese un numero entero 33: "))
print("Fin del Programa")


inicio = 0
fin = 3

while inicio < fin:
    print(f"incio {inicio}, fin {fin}")
    inicio = inicio + 1
print ("fin del while") 



###iteraciones###

saludo = "hola"
saludo += " mundo"
print(saludo) # hola mundo
saludo += "chao"
print(saludo) # hola mundochao

"""   

i = 99 #primer valor a sumar
suma = 0
while i <= 100:
    suma += i #acumulamos para la suma
    i += 1 #incrementamos para sumar el siguiente valor
print(f"El resultado final es {suma}")