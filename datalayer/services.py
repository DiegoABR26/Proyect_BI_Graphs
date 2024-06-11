import requests
url = 'http://localhost:9095/api'


def consulta_horario():
    connection = '{}/BusinessIntelligenceController/GetTipoHorarios'.format(url)
    data = requests.get(connection)

    table_data = []

    if data.status_code == 200:
        data = data.json()
        for e in data['result']:
            row = []
            row.append(e['id_Horario'])
            row.append(e['hora_Inicio'])
            row.append(e['hora_Final'])
            row.append(e['canT_HORAS_TRABJ'])
            row.append(e['actividad'])
            table_data.append(row)
    return table_data
