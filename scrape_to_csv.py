import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Introduce la URL de la página web que quieres scrapear
url = 'https://introducelaweb.es'

# Realiza una solicitud HTTP a la página web
response = requests.get(url)

# Crea un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Encuentra los datos que quieres extraer
# 2. Aquí debes ajustar el scraping según la estructura de la página web
products = soup.find_all('div', class_='product-container')

# 3. Procesa los productos y extrae los datos
data = []
for product in products:
    name = product.find('h3', class_='product-name').text.strip()
    price = product.find('span', class_='price').text.strip()
    data.append([name, price])

# Crea un DataFrame con los datos extraídos
df = pd.DataFrame(data, columns=['Product Name', 'Price'])

# Guarda los datos en un archivo CSV
df.to_csv('datos_extraidos.csv', index=False)
