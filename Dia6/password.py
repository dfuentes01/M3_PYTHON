#Ejercicio Clasificar un Pasword-

#Paso1 : definir las variables
# contrasenia, 

#Paso2 : Solicitar el ingreso de un password.
contrasenia = input("Ingrese una contraseña (minimo 6 caracteres)")

#Paso3 : contar caracteres del string -> len
if len(contrasenia) < 6 :
    print("El password es demasiado corto")

    
#string.count("")
if contrasenia.count (" ") > 0:
    print("El password no puede contener espacios")
elif len(contrasenia) < 6 :
    print("El password es demasiado corto")
    
#cuando indiques contraseña 12345 diga que es un error
if contrasenia.count (" ") > 0:
    print("El password no puede contener espacios")
elif contrasenia == "12345":
    print("El password es incorrecto")
elif len(contrasenia) < 6 :
    print("El password es demasiado corto")
else:
    print("El formato de password es incorrecto")
    
"""    
else:
    #len -> contar los caracteres
    if len(contrasenia) < 6 :
    print("El password es demasiado corto")                 
""" 
#antes se utilizaba de esta manera lo que hoy funcion como elif.