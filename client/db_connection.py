import pyodbc
import pandas as pd
import matplotlib.pyplot as plt


def obtener_datos(procedimiento):
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

def prueba():
    conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER=KATTIA\\BYGRESGUARDO;'
                              'DATABASE=BYG_RR_HH;'
                              'UID=sa;'
                              'PWD=Razon2623*'
    )
    conn = pyodbc.connect(conn_str)

    # Consulta SQL para obtener los datos
    query = """
    SELECT sede.NOMBRE_SEDE, COUNT(*) as num_trabajadores
    FROM EMPLEADOS_DETALLE u
	LEFT JOIN TIPO_SEDE sede on u.SEDE = sede.ID_SEDES
    GROUP BY sede.NOMBRE_SEDE
    """

    # Ejecutar la consulta y obtener los datos
    df = pd.read_sql(query, conn)

    # Cerrar la conexión
    conn.close()

    # Mostrar los datos obtenidos
    print(df)

    # Generar el gráfico de líneas
    # Generar el gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(df['NOMBRE_SEDE'], df['num_trabajadores'], color='b')
    plt.xlabel('Lugar de Trabajo')
    plt.ylabel('Número de Trabajadores')
    plt.title('Número de Trabajadores por Lugar de Trabajo')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y')
    plt.tight_layout()

    # Guardar el gráfico como una imagen
    #plt.savefig('trabajadores_por_lugar.png')

    # Mostrar el gráfico
    plt.show()