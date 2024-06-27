import pyodbc



def ejecutar_sp(procedimiento):
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            'SERVER=KATTIA\\BYGRESGUARDO;'
                            'DATABASE=BYG_RR_HH;  '
                            'UID=sa;'
                            'PWD=Razon2623*')
    
    cursor = conexion.cursor()
    try:
        filas = []
        cursor.execute("EXEC "+ procedimiento)
        filas = cursor.fetchall()
        
    except pyodbc.ProgrammingError as e:
        if "No results. Previous SQL was not a query." in str(e):
            filas = []
        else:
            raise
    finally:
        conexion.close()
    
    return filas

def ejecutar_usp_Trabajadores_cancelados(params:tuple):  
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            'SERVER=KATTIA\\BYGRESGUARDO;'
                            'DATABASE=BYG_RR_HH;  '
                            'UID=sa;'
                            'PWD=Razon2623*')
    
    cursor = conexion.cursor()
    try:
        filas = []
        cursor.execute("EXEC usp_Trabajadores_cancelados "+"@ID_PERIODO=?",params)
        records = cursor.fetchall()
        id = 1
        for row in records:
            rows = []
            rows.append(id)
            rows.append(row[0])
            rows.append(row[1])
            rows.append(row[2])
            rows.append(row[3])
            filas.append(rows)
            id += 1

    except pyodbc.ProgrammingError as e:
        if "No results. Previous SQL was not a query." in str(e):
            filas = []
        else:
            raise
    finally:
        conexion.close()
    
    return filas
