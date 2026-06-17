def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    conteo = {}
    
    # Ruta corregida a la carpeta input
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1
                
    resultado_ordenado = sorted(conteo.items())
    
    return resultado_ordenado
    
