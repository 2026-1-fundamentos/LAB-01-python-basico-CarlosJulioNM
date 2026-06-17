def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    min_max_por_clave = {}
    
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            
            # La columna 5 está en el índice 4
            columna_5 = columnas[4]
            
            # Separamos los pares por comas
            pares = columna_5.split(",")
            
            for par in pares:
                # Separamos la clave del valor usando los dos puntos
                clave, valor_str = par.split(":")
                valor = int(valor_str)
                
                # Lógica de actualización de mínimos y máximos
                if clave in min_max_por_clave:
                    # Actualizar mínimo (posición 0)
                    if valor < min_max_por_clave[clave][0]:
                        min_max_por_clave[clave][0] = valor
                        
                    # Actualizar máximo (posición 1)
                    if valor > min_max_por_clave[clave][1]:
                        min_max_por_clave[clave][1] = valor
                else:
                    # Inicializamos [mínimo, máximo]
                    min_max_por_clave[clave] = [valor, valor]
                    
    # Armamos la lista final ordenada
    resultado = []
    for clave in sorted(min_max_por_clave.keys()):
        min_val = min_max_por_clave[clave][0]
        max_val = min_max_por_clave[clave][1]
        
        # Ojo: la respuesta pide primero el mínimo y luego el máximo
        resultado.append((clave, min_val, max_val))
        
    return resultado
