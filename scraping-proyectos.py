import requests
from bs4 import BeautifulSoup
import json
import re
import concurrent.futures

def get_page_data(url):
    response = requests.get(url)

    # Crear una instancia de Beautiful Soup con el contenido HTML de la página web
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar la tabla de datos por su clase
    table = soup.find('table', {'class': 'tabla_datos'})

    # Obtener los encabezados de columna de la tabla si no han sido obtenidos anteriormente
    headers = []
    for row in table.find_all('tr'):
        if row.find('th'):
            headers = [header.text.strip() for header in row.find_all('th')]
            break

    # Iterar sobre las filas de la tabla y extraer la información de cada celda
    page_data = []
    for row in table.find_all('tr'):
        row_data = {}
        cells = row.find_all('td')
        if len(cells) != len(headers):
            continue
        for i, header in enumerate(headers):
            if header == 'Nombre':
                row_data[header] = cells[i].text
                link = cells[i].find('a')
                if link:
                    row_data['Enlace'] = link['href']
            elif header == 'Mapa':
                try:
                    texto = cells[i].find('a')['onclick']  # Url del mapa
                except TypeError:
                    texto = "N/A"
                    row_data[header] = texto
                else:
                    patron = r"'/mapa/visualizacion/PuntoRepresentativo/index.php\?idExpediente=\d+'"
                    mapa_url = re.search(patron, texto).group().strip("'")
                    url_completa = "https://seia.sea.gob.cl" + mapa_url
                    row_data[header] = url_completa
            else:
                row_data[header] = cells[i].text
        page_data.append(row_data)
    print(f'Se escribe correctamente la pagina {url} en json')
    return page_data

total = 2844
data = []
urls = [f'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php?_paginador_fila_actual={p}' for p in range(1, total)]

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(get_page_data, url) for url in urls]

    for future in concurrent.futures.as_completed(futures):
        data.extend(future.result())

# Guardar la información en un archivo JSON
with open('tabla_datos.json', 'w') as f:
    json.dump(data, f)
