import sys

eleccion_usuario = sys.argv[1].lower #Tijeras o TIJERAS o TiJERas

if(eleccion_usuario != "piedra" and eleccion_usuario != "papel" and eleccion_usuario != "tijeras" ):
    print("Argumento invalido: debe ser piedra papel o tijeras")    