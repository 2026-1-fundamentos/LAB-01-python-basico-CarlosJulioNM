def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    agrupacion_por_numero = {}
    
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            # Convertimos el número a entero porque las respuestas clave son enteros (0, 1, 2...)
            numero = int(columnas[1])
            
            if numero in agrupacion_por_numero:
                # Si el número ya existe como clave, agregamos la letra a su lista
                agrupacion_por_numero[numero].append(letra)
            else:
                # Si no existe, creamos la clave y le asignamos una lista con esa primera letra
                agrupacion_por_numero[numero] = [letra]
                
    # sorted() ordenará el diccionario basándose en las claves numéricas (0, 1, 2...)
    resultado_ordenado = sorted(agrupacion_por_numero.items())
    
    return resultado_ordenado
