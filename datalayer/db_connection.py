import pyodbc
import pandas as pd
import matplotlib.pyplot as plt


def obtener_datos(procedimiento):
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER=KATTIA\\BYGRESGUARDO;'
                              'DATABASE=BYG_RR_HH;  '
                              'UID=sa;'
                              'PWD=Razon2623*')
    cursor = conexion.cursor()
    
    try:
        cursor.execute("EXEC "+ procedimiento)
        print(cursor.fetchall())
        filas = []
    except pyodbc.ProgrammingError as e:
        if "No results. Previous SQL was not a query." in str(e):
            filas = []
        else:
            raise
    finally:
        conexion.close()
        
    return filas

def prueba(procedimiento):
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                'SERVER=KATTIA\\BYGRESGUARDO;'
                                'DATABASE=BYG_RR_HH;'
                                'UID=sa;'
                                'PWD=Razon2623*')
    cursor = conexion.cursor()

    try:
        cursor.execute("EXEC "+ procedimiento)
        print(cursor.fetchall())
        filas = []
    except pyodbc.ProgrammingError as e:
        if "No results. Previous SQL was not a query." in str(e):
            filas = []
        else:
            raise
    finally:
        conexion.close()
        
    return filas
