from src.fetch_data import fetch_webpage as fw
from bs4 import BeautifulSoup

common_url = 'https://worldpopulationreview.com/countries/'

def fetch_population_data(country = None):
    try:
        if not country:
            raise Exception('\n\tNo country provided to fetch data from\n')
        request = fw.fetch_page_content(common_url + country)
        if request is None:
            raise Exception('Failed to fetch the web page')
        html_content = request.text
        soup = BeautifulSoup(html_content, 'html.parser')
        data_tables = soup.find_all('tbody', class_='relative z-10 text-sm')

        historical_population = []
        historical_population_table = data_tables[1]
        for row in historical_population_table:
            pop_year = row.find('th').text
            row_info = row.find_all('td')
            population = row_info[0].text
            density_km2 = row_info[2].text
            population_rank = row_info[3].text
            density_rank = row_info[4].text
            historical_population.append({
                'population_year': pop_year,
                'population': population,
                'density_km2': density_km2,
                'population_rank': population_rank,
                'density_rank': density_rank
            })
            print(pop_year, population, density_km2, population_rank, density_rank)
        
        projection_population = []
        projection_population_table = data_tables[2]
        for row in projection_population_table:
            pop_year = row.find('th').text
            row_info = row.find_all('td')
            population = row_info[0].text
            density_km2 = row_info[2].text
            population_rank = row_info[3].text
            density_rank = row_info[4].text
            projection_population.append({
                'population_year': pop_year,
                'population': population,
                'density_km2': density_km2,
                'population_rank': population_rank,
                'density_rank': density_rank
            })
            print(pop_year, population, density_km2, population_rank, density_rank)
        
        return {
            'historical_population': historical_population,
            'projection_population': projection_population
        }

    except Exception as e:
        print(f'Error {e}. While parsing population')
        return None
