def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma_total = 0
    
    # La ruta correcta basada en tu explorador de archivos
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            suma_total += int(columnas[1])
            
    return suma_total
