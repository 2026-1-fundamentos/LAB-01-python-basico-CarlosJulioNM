def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    conteo_meses = {}
    
    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            
            # La fecha está en la tercera columna (índice 2) -> Ej: "1999-02-28"
            fecha = columnas[2]
            
            # Separamos la fecha por los guiones -> ["1999", "02", "28"]
            partes_fecha = fecha.split("-")
            
            # El mes es el segundo elemento (índice 1) -> "02"
            mes = partes_fecha[1]
            
            # Lógica de conteo en el diccionario
            if mes in conteo_meses:
                conteo_meses[mes] += 1
            else:
                conteo_meses[mes] = 1
                
    # Ordenamos por la clave (el mes en formato string, ej: '01', '02'...)
    resultado_ordenado = sorted(conteo_meses.items())
    
    return resultado_ordenado
