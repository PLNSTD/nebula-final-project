from bs4 import BeautifulSoup
from src.fetch_data import fetch_webpage as fw

common_url = 'https://worldpopulationreview.com/continents/'

def fetch_continent_countries(continent = None):
    if not continent:
        raise Exception('\n\tNo continent provided to fetch data from\n')
    
    html_content = fw.fetch_page_content(common_url + continent).text
    soup = BeautifulSoup(html_content, 'html.parser')

    table_data_rows = soup.find_all('tbody', class_='relative z-10 text-sm')[1].find_all('tr', class_='table-row')
    countries = []

    for row in table_data_rows:
        name = row.find('a').text
        row_info = row.find_all('td')
        population = row_info[0].get_text()
        density = row_info[1].text
        country = {
            'name': name,
            'population': population,
            'density_km2': density
            }
        countries.append(country)
    
    return countries

