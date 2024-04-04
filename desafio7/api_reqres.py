"""
Descripción
Se tiene una API que contiene cierta información personal de clientes. Esta API está siendo
testeada porque otro equipo de desarrolladores quiere integrarla en una aplicación que utiliza
información personal de personas.
● Para este desafío, se debe usar la API de pruebas de reqres, disponible en
https://reqres.in/ .
● Esta API no requiere autenticación, y su único recurso es users.
● Todas las solicitudes se hacen a https://reqres.in/api/users.
● Se considerará para la evaluación, que las respuestas de la API sean exitosas (códigos
2xx).
Requerimientos
1. Obtenga toda la información de los usuarios retornada por la API, guárdela en una
variable llamada users_data e imprímala en pantalla.
(3 Puntos)
2. Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el
diccionario de respuesta en una variable llamada created_user e imprímala en
pantalla.
(2 Puntos)
3. Actualice un usuario llamado morpheus para que tenga un campo llamado residence
igual a zion. Guarde el diccionario de respuesta en una variable llamada
updated_user e imprímala en pantalla.
(3 Puntos)
4. Elimine un usuario llamado Tracey. Imprima el código de respuesta en pantalla.
(2 Puntos)
¡Mucho éxito!
"""
import requests

# Req.1 obtener usuarios
url = "https://reqres.in/api/users" # definiendo la url de la API
response = requests.get(url) # realizando la solicitud GET
if response.status_code // 100 == 2 :
    users_data = response.json()
    print("Informacion de los usuarios")
    print(users_data)
else:
    print("Error al obtener información de usuarios. Codigo estado", response.status_code)


# Req.2 Creando un usuario
url = "https://reqres.in/api/users"
nuevo_usuario = {"name" : "Ignacio", "job" : "Profesor"}
response = requests.post(url, json=nuevo_usuario)
if response.status_code // 100 == 2 :
    created_user = response.json()
    print("Usuario creado exitosamente")
    print(created_user)
else:
    print("Error al crear usuario. Código de estado:", response.status_code)

# Req. 3 Actualizando un usuario. No hay usuario con el nombre indicado se hace el cambio a "Eve"
url = "https://reqres.in/api/users/4"
update_usuario = {"name" : "Eve", "job" : "Leader", "residence": "zion"}
response = requests.put(url, json=update_usuario)
if response.status_code // 100 == 2 :
    created_user = response.json()
    print("Usuario actualizado exitosamente:")
    print(update_usuario)
else:
    print("Error al actualizar usuario. Código de estado:", response.status_code)

#Req.4 Eliminando un usuario.
    
url = "https://reqres.in/api/users/6"
response = requests.delete(url)
print("Código de respuesta al eliminar usuario:", response.status_code)#204








