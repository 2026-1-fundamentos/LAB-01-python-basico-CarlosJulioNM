def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}

    """
    conteo_claves = {}
    
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            
            # La columna 5 está en el índice 4
            columna_5 = columnas[4]
            
            # Separamos los elementos por coma
            pares = columna_5.split(",")
            
            for par in pares:
                # Separamos por los dos puntos y nos quedamos solo con la clave (índice 0)
                clave = par.split(":")[0]
                
                # Aumentamos el contador de esa clave
                if clave in conteo_claves:
                    conteo_claves[clave] += 1
                else:
                    conteo_claves[clave] = 1
                    
    # Ordenamos el diccionario alfabéticamente por sus claves para que coincida con la respuesta
    resultado = {clave: conteo_claves[clave] for clave in sorted(conteo_claves.keys())}
    
    return resultado
