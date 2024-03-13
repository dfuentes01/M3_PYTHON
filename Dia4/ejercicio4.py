"""
solicitar al usuario el ingreso de 3 numeros y
determinar cuales de ellos es mayor que 33
solo numeros enteros 1 al 100
y determinar cual es mayor y cual es menor
"""
#Definir las variables
numero1, numero2, numero3, mayor, menor

#Solicitar al usuario ingresar los 3 numeros enteros
escribir ("Ingresar el primer numero (entre 1 y 100): ")
leer (numero1)

escribir ("Ingresar el segundo numero (entre 1 y 100): ")
leer (numero2)

escribir ("Ingresar el tercer numero (entre 1 y 100): ")
leer (numero3)

#Verificar que los numeros estan dentro del rango

si (numero1 < 1 o numero1 > 100 o numero2 < 1 o numero2 > o 100 numero3 < 1 o numero3 > 100 )
    escribir ("Ingresar numeros enteros entre 1 y 100")
    sino
    
    #Determinar cuales son mayores a 33
    
    si(numero1>33) entonces
    escribir("El numero1 es mayor que 33.")
    fin si
    
    si(numero2>33) entonces
    escribir("El numero2 es mayor que 33.")
    fin si
    
    si(numero3>33) entonces
    escribir("El numero3 es mayor que 33.")
    fin si
    
    #identificar el numero mayor y el numero menor
    mayor = max(numero1,numero2,numero3)
    menor = min(numero1,numero2,numero3)
    
    #mostrar los resultados
    escribir("el numero mayor es:", mayor)
    escribir("el numero menor es:", menor)

    
    
    


