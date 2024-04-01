def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    nivel = (n_pregunta - 1) // p_level  # Calculando el nivel basado en el número de pregunta y preguntas por nivel
    
    if nivel == 0:
        return "basicas"
    elif nivel == 1:
        return "intermedias"
    elif nivel == 2:
        return "avanzadas"
    else:
        return "Error: numero de pregunta fuera de rango"  
    
    ##################################################


if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias