import json

results = json.loads(response.text)
print(type(results)) # Veremos que el resultado es una lista
print(results[0]) # Mostramos el primer elemento