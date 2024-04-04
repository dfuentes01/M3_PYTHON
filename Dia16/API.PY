import requests

url ="https://jsonplaceholder.typicode.com/posts"

payload = {}
headers = {}

response = requests.request("GET", url, headers = headers, data= payload)
print (response.text)

import json
results = json.loads(response.text)
print(type(results)) # Veremos que el resultado es una lista
print(results[0]) # Mostramos el primer elemento

print(results[0].keys()) #dict_keys(['userId', 'id', 'title', 'body'])
print(results[0]["userId"]) #1
print(results[0]["title"]) #sunt aut facere repellat provident occaecati excepturi optio reprehenderit
print([post['title'] for post in results]) #se imprimen todos los listos - lsita larga.

import json

def request_get(url):
    return json.loads(requests.get(url).text)

request_get('http://jsonplaceholder.typicode.com/posts/post')

print("PRESENTACION 2")

data = request_get('https://jsonplaceholder.typicode.com/photos')[0:10]
# Tomamos solo 10
print(data)

