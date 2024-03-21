#1. Crea un diccionario
deportes = {
"Diego":"Basquetbol", 
"Aline": "Tenis", 
"Sergio" : "Futbol", 
}
print(deportes) #{'Diego': 'Basquetbol', 'Aline': 'Tenis', 'Sergio': 'Futbol'}

#2. Agrega un elemento
deportes["Fabian"]="Rugby"
print(deportes) #{'Diego': 'Basquetbol', 'Aline': 'Tenis', 'Sergio': 'Futbol', 'Fabian': 'Rugby'}

#3. Cambia un elemento
deportes["Aline"]="Danza"
print(deportes) #{'Diego': 'Basquetbol', 'Aline': 'Danza', 'Sergio': 'Futbol', 'Fabian': 'Rugby'}

#4. Elimina un elemento

eliminado = deportes.pop("Fabian")
print(eliminado) #Rugby
print(deportes) #{'Diego': 'Basquetbol', 'Aline': 'Danza', 'Sergio': 'Futbol'}