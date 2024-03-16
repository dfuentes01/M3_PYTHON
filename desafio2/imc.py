# Paso1: Definir las variables
# peso, altura_cm, altura_m, IMC

# Paso2: Solicitar el ingreso de datos al usuario

peso= float(input("ingrese su peso en kilogramos: "))
altura = float(input("ingrese su estatura en centimetros: "))/100

# Paso3: Realizar el calculo matematico con la formula entregada.
IMC = peso /(altura*altura)

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
elif IMC > 40 :
    print ("Las clasificacion OMS es Obesidad Grado 3")
    
    