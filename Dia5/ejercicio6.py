edad = 27
#¿Juan es mayor de edad?
print(edad >=18) # True
print(edad<18) # False

edad_graduacion_colegio = 17 #años
#¿Juan se graduo del colegio antes de los 18 años?
print(edad_graduacion_colegio < 18) #True
print(edad_graduacion_colegio>=18) #False

exp_laboral=4 #años
#¿Juan no tiene 4 años de experiencia laboral?
print(exp_laboral!=4) #False
print(exp_laboral==4) #True

numero_hijos = 0
#¿Juan tiene hijos?
print(numero_hijos > 0) #False
print(numero_hijos == 0) #True
print(numero_hijos < 0) #False
print(numero_hijos != 0) #False
print(numero_hijos >= 0) #True

####Preguntas Indirectas####

"""
1.-Si las exportaciones disminuyen entonces bajarán las utilidades
2.-Los precios son altos si y sólo sí los costos aumentan
3.-Si la producción aumenta entonces bajarán los precios
4.-Si la contaminación aumenta entonces existirá restricción vehicular adicional
5.-Ser o No Ser
6.-la programacion no es facil
"""

nombre = "Juan"
me_llamo_juan = (nombre == "Juan")
print(me_llamo_juan)      #True
print(type(me_llamo_juan)) #<class 'bool'>

#Logica proposicional
""" 
#Quieres helado (P) SI - NO
#Quieres bebida (Q) SI - NO

# AND (Y; i) 2 ^ 3
# Quieres helado y Quieres bebida
#Punto critico para el AND es : ambos verdaderos el resultado es verdadero
P y Q
-------
V y V = V *
V y F = F
F y V = F
F y F = F 

#Punto critico para el O es: ambos falsos el resultado es falso
P o Q
-------
V o V = V
V o F = V
F o V = V
F o F = F *

#XoR
#Punto critico para el XoR es: ambas iguales el resultado es False
P ^ Q

-F = V
-V = F

"""