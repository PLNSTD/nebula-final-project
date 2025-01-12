from bs4 import BeautifulSoup
from src.fetch_data import fetch_webpage as fw

common_url = 'https://worldpopulationreview.com/cities/'

def fetch_country_cities(country = None):
    try:
        if not country:
            raise Exception('\n\tNo country provided to fetch data from\n')
        request = fw.fetch_page_content(common_url + country)
        if request is None:
            raise Exception('Failed to fetch the web page fetch_cities.py')
        html_content = request.text
        soup = BeautifulSoup(html_content, 'html.parser')
        table_content = soup.find('tbody', class_='relative z-10 text-sm')
        table_rows = table_content.find_all('tr', class_='table-row')

        cities = []

        for row in table_rows:
            city = row.find('th').get_text()
            population = row.find('td').get_text()
            
            city_obj = {
                'name': city,
                'population': population
            }
            cities.append(city_obj)
        
        return cities
    except Exception as e:
        print(f'Error {e}')
        return None
