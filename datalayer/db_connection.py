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
        records = cursor.fetchall()
        id = 1
        i=len(records)
        for row in records:
            rows = []
            for i in range(len(row)):
                rows.append(row[i])
                i -= 1
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

def ejecutar_sp_con_params(sp:str, argumentos:str ,params:tuple):  
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            'SERVER=KATTIA\\BYGRESGUARDO;'
                            'DATABASE=BYG_RR_HH;  '
                            'UID=sa;'
                            'PWD=Razon2623*')
    
    cursor = conexion.cursor()
    try:
        filas = []
        cursor.execute("EXEC {} ".format(sp)+"{}".format(argumentos),params)
        records = cursor.fetchall()
        id = 1
        i=len(records)
        for row in records:
            rows = []
            for i in range(len(row)):
                rows.append(row[i])
                i -= 1
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
