# se importan los metodos desde los archivos creados en la misma carpeta.
from os import system
import suma
import resta as r
from input import captura_de_datos

print("Calculadora_basica\n")
opcion = input("Que operacion desea realizar?")
print("Seleccione opcion a realizar")
print("1) Sumar")
print("2) Restar")
print("0) Salir")
print("> ")
opcion = int(input("> "))

system("cls")
if opcion == 1:
    x,y = captura_de_datos()
    suma.sumar(x,y)
elif opcion == 2:
    x,y = captura_de_datos()#se utiliza el seudonimo "r" creado al momento de importar 
    r.restar(x,y)
elif opcion == 0:
    print("Hasa luego, regrese pronto")
    exit()
else:
    exit()
    print("Opcion invalida")

