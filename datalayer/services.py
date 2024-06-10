import requests
url = 'http://localhost:9095/api'


def consulta_horario():
    connection = '{}/BusinessIntelligenceController/GetTipoHorarios'.format(url)
    data = requests.get(connection)

    table_data = []

    if data.status_code == 200:
        data = data.json()
        for e in data['result']:
            table_data.append(e['id_Horario'])
    print(table_data)
    return table_data
