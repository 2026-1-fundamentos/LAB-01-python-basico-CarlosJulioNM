def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]

    """
    resultado = []
    
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            
            # Extraemos la letra de la primera columna (índice 0)
            letra = columnas[0]
            
            # Columna 4 (índice 3): separamos por comas y contamos los elementos
            elementos_col4 = columnas[3].split(",")
            cantidad_col4 = len(elementos_col4)
            
            # Columna 5 (índice 4): separamos por comas y contamos los elementos
            elementos_col5 = columnas[4].split(",")
            cantidad_col5 = len(elementos_col5)
            
            # Agregamos la tupla a nuestra lista de resultados
            resultado.append((letra, cantidad_col4, cantidad_col5))
            
    return resultado
