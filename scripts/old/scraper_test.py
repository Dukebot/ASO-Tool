# Importar módulos
import requests
import csv
from bs4 import BeautifulSoup

# Dirección de la página web
url = "https://dukebot.github.io/trap-ball-landing-page/"

def get_html(url):
    # Ejecutar GET-Request
    response = requests.get(url)
    # Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
    html = BeautifulSoup(response.text, 'html.parser')
    return html

def print_pretty(html):
    print(html.prettify)

def print_all_links(html):
    for link in html.find_all('a'): 
        print(link.get('href'))

def print_all_text(html):
    print(html.get_text())


html = get_html(url)
print_pretty(html)
#print_all_links(html)