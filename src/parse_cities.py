from bs4 import BeautifulSoup
import fetch_webpage as fw
import fetch_air_quality as faiq

common_url = 'https://worldpopulationreview.com/countries/'

def parse_country_largest_cities(country = None):
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
        aqi = faiq.parse_city_air_quality(city)
        air_quality_indexes.append(aqi)
        cities.append(city)
        cities_population.append(population)
    
    return (cities, cities_population, air_quality_indexes)

# GOOD 
cities_info = parse_country_largest_cities('italy')
print(cities_info)