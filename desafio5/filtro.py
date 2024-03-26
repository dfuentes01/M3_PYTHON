import sys

#diccionario.
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

def filtrar_productos(precios, umbral, operacion="mayor"):
    if operacion == "mayor":
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio > umbral}
    elif operacion == "menor":
        productos_filtrados = {producto: precio for producto, precio in precios.items() if precio < umbral}
    else:
        return "Lo sentimos, no es una operación válida"
    
    return productos_filtrados

if __name__ == "__main__":
    if len(sys.argv) == 2: #quiere decir que se ingreso solo el umbral. posicion 0 y 1.
        umbral = int(sys.argv[1])
        productos_filtrados = filtrar_productos(precios, umbral)
        print("Los productos mayores al umbral son:", ', '.join(productos_filtrados.keys()))
    elif len(sys.argv) == 3: #quiere decir que se ingreso el umbral y la operacion "menor". posicion 0,1 y 2
        umbral = int(sys.argv[1])
        operacion = sys.argv[2].lower()
        if operacion == "mayor":
            productos_filtrados = filtrar_productos(precios, umbral, operacion)
            print("Los productos mayores al umbral son:", ', '.join(productos_filtrados.keys()))
        elif operacion == "menor":
            productos_filtrados = filtrar_productos(precios, umbral, operacion)
            print("Los productos menores al umbral son:", ', '.join(productos_filtrados.keys()))
        else:
            print("Lo sentimos, no es una operación válida")
    else:
        print("Uso: python filtro.py umbral [mayor|menor]")
