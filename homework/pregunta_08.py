def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    agrupacion_por_numero = {}
    
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            numero = int(columnas[1])
            
            if numero in agrupacion_por_numero:
                # Usamos .add() en lugar de .append() porque es un 'set' (conjunto)
                agrupacion_por_numero[numero].add(letra)
            else:
                # Inicializamos la clave con un set que contiene la primera letra
                agrupacion_por_numero[numero] = {letra}
                
    resultado = []
    
    # Recorremos el diccionario ordenado por sus claves (los números)
    for numero in sorted(agrupacion_por_numero.keys()):
        # Convertimos el set a lista y lo ordenamos alfabéticamente
        letras_ordenadas = sorted(list(agrupacion_por_numero[numero]))
        resultado.append((numero, letras_ordenadas))
        
    return resultado
