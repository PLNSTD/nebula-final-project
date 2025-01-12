from bs4 import BeautifulSoup
from src.fetch_data import fetch_webpage as fw

common_url = 'https://worldpopulationreview.com/continents/'

def fetch__countries_by_continent(continent = None):
    try:
        if not continent:
            raise Exception('\n\tNo continent provided to fetch data from\n')
        request = fw.fetch_page_content(common_url + continent)
        if not request:
            raise Exception('Failed to fetch the web page')
        html_content = request.text
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
    except Exception as e:
        print(f'Error {e}')
    return None
