import sys

respuesta_usuario = input("¿Responde a estímulos? (si/no): ")
while respuesta_usuario.lower() not in ["si", "no"]:
    respuesta_usuario = input("Favor, responder 'si' o 'no': ")
    
if respuesta_usuario.lower() == "si":
    print ("Valorar la necesidad de llevarlo al hospital mas cercano")
    print ("Fin del programa")
elif respuesta_usuario.lower() == "no":
    print ("Abrir la vía aérea")

    respuesta_usuario = input("¿Respira? (si/no): ")
    while respuesta_usuario.lower() not in ["si", "no"]:
        respuesta_usuario = input("Favor, responder 'si' o 'no': ")  
    
    if respuesta_usuario.lower() == "si":
        print ("Permitirle posicion de suficiente ventilacion")
        print ("Fin del programa")
    elif respuesta_usuario.lower() == "no":
        print ("Administrar 5 ventilaciones y llamar a Ambulancia")    
        
        
        while True:
            respuesta_usuario = input("¿Hay signos de vida? (si/no): ")
            while respuesta_usuario.lower() not in ["si", "no"]:
                respuesta_usuario = input("Por favor, responda 'si' o 'no': ")

            if respuesta_usuario.lower() == "si":
                print("Reevaluar a la espera de la ambulancia.")
            elif respuesta_usuario.lower() == "no":
                print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
        
            llego_ambulancia = input("¿Llegó la ambulancia? (si/no): ")
            while llego_ambulancia.lower() not in ["si", "no"]:
                llego_ambulancia = input("Por favor, responda 'si' o 'no': ")

            if llego_ambulancia.lower() == "si":
                print("Fin del programa.")
                break      

    
