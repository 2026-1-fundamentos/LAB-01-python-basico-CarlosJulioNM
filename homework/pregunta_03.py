def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    sumas = {}
    
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1]) 
            
            if letra in sumas:
                sumas[letra] += valor
            else:
                sumas[letra] = valor
                
    resultado_ordenado = sorted(sumas.items())
    
    return resultado_ordenado
