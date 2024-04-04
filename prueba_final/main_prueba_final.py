import plantillas
from call_API import request_get
from generador_html import generador_html

url = "https://aves.ninjas.cl/api/birds" #definiendo url.
response = request_get(url) # llamando a la funcion para extraer los datos requeridos desde el diccionario.
generador_html(url) #llamando a la funcion con la url definida. para crear nuevo archivo .html con los valores reemplazados.

