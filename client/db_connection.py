import pyodbc


def obtener_datos(procedimiento):
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER=KATTIA\BYGRESGUARDO;'
                              'DATABASE=BYG_RR_HH;'
                              'UID=sa;'
                              'PWD=Razon2623*')
    cursor = conexion.cursor()
    cursor.execute(f"EXEC {procedimiento}")
    filas = cursor.fetchall()
    conexion.close()
    return filas