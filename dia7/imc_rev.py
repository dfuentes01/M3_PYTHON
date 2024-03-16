"""
# Paso1: Definir las variables
# peso, altura_cm, altura_m, IMC

# Paso2: Solicitar el ingreso de datos al usuario

peso= float(input("ingrese su peso en kilogramos: "))
altura_cm = float(input("ingrese su estatura en centimetros: "))
altura_m = (altura_cm)/100    

# Paso3: Realizar el calculo matematico con la formula entregada.
IMC = peso /(altura_m*altura_m)

# Paso4: Redondear el IMC a 2 decimales.
IMC_redondeado = round(IMC,2)
print("Su indice de masa corporal es", IMC_redondeado, "[kg/m2]")

# Paso5: Establecer las condicionales para la clasificacion.
if IMC < 18.50 :
print ("Las clasificacion OMS es Bajo Peso")
elif 18.5 <= IMC <= 25 :
print ("Las clasificacion OMS es Adecuado")
elif 25 <= IMC <= 30 :
print ("Las clasificacion OMS es Sobrepeso")
elif 30 <= IMC <= 35 :
print ("Las clasificacion OMS es Obesidad Grado 1")
elif 35 <= IMC <= 40 :
print ("Las clasificacion OMS es Obesidad Grado 2")
elif IMC < 40 :
print ("Las clasificacion OMS es Obesidad Grado 3")
"""
import sys

#se ejecuta en la terminal : python dia7/imc_rev.py 81 178
print(sys.argv) #['dia7/imc_rev.py', '81', '178']
print(sys.argv[1]) #81
print(sys.argv[2]) #178

peso_kilogramos = float(sys.argv[1])
estatura = float(sys.argv[2])/100

print(type(peso_kilogramos))
print(type(estatura))

# calculo del imc
# imc = peso_kilogramos / (estatura * estatura)
imc = peso_kilogramos / (estatura ** 2) 
print(f"Tu IMC es de {round(imc,2)}")
print(f"Tu IMC es de {imc:.2}")


if imc < 18.5:
    print("Su clasificacion OMS es: Bajo peso")
elif imc < 25:
    print("Su clasificacion OMS es: Adecuado")
elif imc < 30:
    print("Su clasificacion OMS es: Sobrepeso")
elif imc < 35:
    print("Su clasificacion OMS es: Obesidad grado I")
elif imc < 40:
    print("Su clasificacion OMS es: Obesidad grado II")
else:
    print("Su clasificacion OMS es: Obesidad grado III")
    
