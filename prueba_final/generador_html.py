import plantillas
from call_API import request_get

def generador_html(url):
    response = request_get(url)
    cadena = ""
    for dicc in response:
        print(dicc["name"]["spanish"], dicc["name"]["english"], dicc["images"]["full"])
        cadena = cadena + plantillas.plantilla_A.substitute(name_esp = dicc["name"]["spanish"],
                                                        name_eng = dicc["name"]["english"],
                                                        imagen_url = dicc["images"]["full"])
    file_name = "Aves_de_Chile.html"
    with open (file_name, "w") as file:
        message = plantillas.plantilla.substitute(contenido = cadena)
        file.write(message)
    print (f"Archivo .html generado : {file_name}")