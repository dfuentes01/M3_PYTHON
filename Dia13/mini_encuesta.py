"""
preguntas = [
    'Enunciado Pregunta 1',
    'Enunciado Pregunta 2',
    'Enunciado Pregunta 3'
    ]

#agregar las respuestas en una lista vacia.
respuestas=[]

#hacer preguntas.
print(preguntas[0])
print("Opciones: ")
print("1). De acuerdo")
print("2). En desacuerdo")
print("3). No me interesa")
respuestas.append(input("> \n"))

print(preguntas[1])
print("Opciones: ")
print("1). De acuerdo")
print("2). En desacuerdo")
print("3). No me interesa")
respuestas.append(input("> \n"))

print(preguntas[2])
print("Opciones: ")
print("1). De acuerdo")
print("2). En desacuerdo")
print("3). No me interesa")
respuestas.append(input("> \n"))

print(f"La respuesta a la pregunta 1 es: {respuestas[0]}")
print(f"La respuesta a la pregunta 2 es: {respuestas[1]}")
print(f"La respuesta a la pregunta 3 es: {respuestas[2]}")
"""

# AHORA REALIZAREMOS LO MISMO PERO CON MENOS LINEAS DE CODIGO

#definimos la funcion
def imprimir_menu():
    print("Opciones: ")
    print("1). De acuerdo")
    print("2). En desacuerdo")
    print("3). No me interesa")
    respuestas.append(input("> \n"))

preguntas = ['Enunciado Pregunta 1', 'Enunciado Pregunta 2','Enunciado Pregunta 3']
respuestas = []

for pregunta in preguntas:
    print(pregunta)
    imprimir_menu()
    respuestas.append(input("> \n"))
    print("")

for i in range(len(respuestas)): #[0,1,2]  len = 3
    print(f"La respuesta a la pregunta {i+1} es: {respuestas[i]}")
