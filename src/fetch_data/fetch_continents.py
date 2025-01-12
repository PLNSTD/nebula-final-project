from src.fetch_data import fetch_webpage as fw
from bs4 import BeautifulSoup

common_url = 'https://worldpopulationreview.com/continents'

def fetch_continents_from_page():
    html_content = fw.fetch_page_content(common_url).text
    soup = BeautifulSoup(html_content, 'html.parser')
    continent_container = soup.find('tbody', class_='relative z-10 text-sm').find_all('tr', class_='table-row')

    continents = []

    for continent_row in continent_container:
        name = continent_row.find('th').find('a').get_text()
        continent_info = continent_row.find_all('td')
        population = continent_info[0].get_text()
        world_population = continent_info[1].get_text()
        density_per_km = continent_info[2].get_text()
        continents.append({
            'name': name,
            'population': population,
            'world_population': world_population,
            'density_per_km2': density_per_km
        })
    
    return continents
