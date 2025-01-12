from bs4 import BeautifulSoup
from src.fetch_data import fetch_webpage as fw

common_url = 'https://worldpopulationreview.com/cities/'

def fetch_country_cities(country = None):
    if not country:
        raise Exception('\n\tNo country provided to fetch data from\n')

    html_content = fw.fetch_page_content(common_url + country).text
    soup = BeautifulSoup(html_content, 'html.parser')
    table_content = soup.find('tbody', class_='relative z-10 text-sm')
    table_rows = table_content.find_all('tr', class_='table-row')

    cities = []
    cities_population = []

    for row in table_rows:
        city = row.find('th').get_text()
        population = row.find('td').get_text()
        cities.append(city)
        cities_population.append(population)
    
    return (cities, cities_population)

# GOOD 
cities_info = fetch_country_cities('switzerland')
print(len(cities_info[0]))