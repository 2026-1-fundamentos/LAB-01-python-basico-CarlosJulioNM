def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}

    """
    sumas_por_letra = {}
    
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            
            # Extraemos el valor a sumar (columna 2 -> índice 1)
            valor = int(columnas[1])
            
            # Extraemos y separamos las letras (columna 4 -> índice 3)
            letras_col4 = columnas[3].split(",")
            
            # Iteramos sobre cada letra de esa fila específica
            for letra in letras_col4:
                if letra in sumas_por_letra:
                    sumas_por_letra[letra] += valor
                else:
                    sumas_por_letra[letra] = valor
                    
    # Ordenamos el diccionario alfabéticamente por sus claves
    resultado = {letra: sumas_por_letra[letra] for letra in sorted(sumas_por_letra.keys())}
    
    return resultado
