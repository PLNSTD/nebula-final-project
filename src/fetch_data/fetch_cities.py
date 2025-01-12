from bs4 import BeautifulSoup
import fetch_data.fetch_webpage as fw
import temp_ideas.fetch_air_quality as faiq
import db_management.psql.db_interface as db

common_url = 'https://worldpopulationreview.com/countries/'

def fetch_country_largest_cities(country = None):
    if not country:
        raise Exception('\n\tNo country provided to parse data from\n')

    html_content = fw.fetch_page_content(common_url + country).text
    soup = BeautifulSoup(html_content, 'html.parser')
    table_content = soup.find('tbody', class_='relative z-10 text-sm')
    table_rows = table_content.find_all('tr', class_='table-row')

    cities = []
    cities_population = []
    air_quality_indexes = []

    for row in table_rows:
        city = row.find('th').get_text()
        population = row.find('td').get_text()
        aqi = faiq.fetch_city_air_quality(city)
        air_quality_indexes.append(aqi)
        cities.append(city)
        cities_population.append(population)
    
    return (cities, cities_population, air_quality_indexes)

# GOOD 
cities_info = fetch_country_largest_cities('united-states')
print(cities_info)