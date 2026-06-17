def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sumas_por_letra = {}
    
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            
            # Extraemos la letra (columna 1 -> índice 0)
            letra = columnas[0]
            
            # Extraemos el texto del diccionario (columna 5 -> índice 4)
            columna_5 = columnas[4]
            pares = columna_5.split(",")
            
            # Sumamos todos los valores numéricos de esta fila
            suma_fila = 0
            for par in pares:
                # Separamos por ":" y tomamos el valor numérico (índice 1)
                valor = int(par.split(":")[1])
                suma_fila += valor
                
            # Acumulamos la suma en el diccionario principal
            if letra in sumas_por_letra:
                sumas_por_letra[letra] += suma_fila
            else:
                sumas_por_letra[letra] = suma_fila
                
    # Ordenamos el diccionario alfabéticamente por sus claves
    resultado = {letra: sumas_por_letra[letra] for letra in sorted(sumas_por_letra.keys())}
    
    return resultado
