import requests
import json

url = "https://aves.ninjas.cl/api/birds"

def request_get(url):
    return json.loads(requests.get(url).text)




if __name__ == "__main__": #lo que queda bajo esto es de prueba.

    url = "https://aves.ninjas.cl/api/birds"

    response = requests.get(url)


    print(response) 

    if response.status_code == 200:
        print("obtencion correcta")
        # print(response.json())
        print("")
        # post = response.json()
        # print(post[0])
    else:
        print("Error en la solicitud", response.text,response.status_code)

