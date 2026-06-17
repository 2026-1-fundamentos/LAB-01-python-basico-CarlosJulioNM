def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    max_min_por_letra = {}
    
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            valor = int(columnas[1])
            
            # Si la letra ya está registrada, actualizamos sus máximos y mínimos
            if letra in max_min_por_letra:
                # Actualizar máximo (posición 0 de la lista)
                if valor > max_min_por_letra[letra][0]:
                    max_min_por_letra[letra][0] = valor
                
                # Actualizar mínimo (posición 1 de la lista)
                if valor < max_min_por_letra[letra][1]:
                    max_min_por_letra[letra][1] = valor
            else:
                # Si es la primera vez que vemos la letra, inicializamos 
                # la lista [max, min] con el primer valor encontrado
                max_min_por_letra[letra] = [valor, valor]
                
    # Ordenamos las letras alfabéticamente y construimos la lista de tuplas final
    resultado = []
    for letra in sorted(max_min_por_letra.keys()):
        max_val = max_min_por_letra[letra][0]
        min_val = max_min_por_letra[letra][1]
        resultado.append((letra, max_val, min_val))
        
    return resultado
