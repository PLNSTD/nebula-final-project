from src.fetch_data.fetch_continents import fetch_continents_from_page as fetch_continents
from src.fetch_data.fetch_countries import fetch__countries_by_continent as fetch_countries
from src.fetch_data.fetch_cities import fetch_country_cities as fetch_cities
from src.database_psql.db_setup import create_tables
from src.database_psql.data_operations import continents as continents_table
from src.database_psql.data_operations import countries as countries_table
from src.database_psql.data_operations import cities as cities_table
import os
from src.fetch_data.fetch_country_population import fetch_population_data as fetch_pop

def fill_db_with_continents():
    create_tables.setup_continents()
    continents = fetch_continents()

    if continents is None:
        return
    
    cntContinent = 0
    for continent in continents:
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Continents: {cntContinent}/{len(continents)}')
        name = continent['name']
        population = int(continent['population'].replace(',', ''))
        world_population = float(continent['world_population'][:-1])
        density_per_km2 = float(continent['density_per_km2'])
        continents_table.insert(
            name,
            population,
            world_population,
            density_per_km2
        )
        cntContinent += 1

    print('Complete Continents')

def fill_db_with_countries():
    create_tables.setup_countries()
    continents = continents_table.get_all()

    if not continents:
        return
    
    cntContinent = 0
    for continent in continents:
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print(continent)
        print(f'Continents: {cntContinent}/{len(continents)}')
        original_continent_name = continent[0]
        continent_name = original_continent_name.lower()
        continent_name = continent_name.replace(' ', '-')
        countries = fetch_countries(continent_name)

        if countries is None:
            continue

        cntCountries = 0
        for country in countries:
            # Clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')
            print(continent)
            print(f'Countries: {cntCountries}/{len(countries)}')
            country_name = country['name']
            country_population = int(country['population'].replace(',', ''))
            country_density = country['density_km2'].replace(',','.')
            country_density = float(country_density)

            countries_table.insert(
                country_name,
                original_continent_name,
                country_population,
                country_density
            )
            cntCountries += 1

        print('Completed ' + continent_name)
        cntContinent += 1
        # x = input('Continue?')
        x = 1
        if x == 0:
            return
    print('Completed all countries')

def fill_db_with_cities():
    create_tables.setup_cities()
    countries = countries_table.get_all()
    flag = False
    if countries is None:
        return
    
    cntCountries = 0
    for country in countries:
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Countries: {cntCountries}/{len(countries)}')
        original_country_name = country[0]
        country_name = original_country_name.lower()
        country_name = country_name.replace(' ','-')
        cities = fetch_cities(country_name)

        if cities is None:
            cntCountries += 1
            continue
        
        cntCities = 0
        for city in cities:
            if cntCities == 10:
                break
            # Clear the screen
            os.system('cls' if os.name == 'nt' else 'clear')
            print(country)
            print(f'Cities: {cntCities}/{len(cities)}')
            city_name = city['name']
            city_population = int(city['population'].replace(',', ''))

            cities_table.insert(
                city_name,
                original_country_name,
                city_population
            )
            cntCities += 1

        cntCountries += 1
        print('Completed ' + country_name)
        x = 1
        # x = input('Continue?')
        if x == 0:
            return

def fill_db_with_country_pop_projections():
    countries = countries_table.get_all()
    
    if countries is None:
        return
    
    cntCountries = 0

    for country in countries:
        # Clear the screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Countries: {cntCountries}/{len(countries)}')
        original_country_name = country[0]
        country_name = original_country_name.lower()
        country_name = country_name.replace(' ','-')

        population_projection_data = fetch_pop(country_name)

        if population_projection_data is None:
            cntCountries += 1
            continue

        for year_pop_history in population_projection_data['historical_population']:
            year = int(year_pop_history['population_year'])
            city_population = int(year_pop_history['population'].replace(',', ''))
            density_km2 = year_pop_history['density_km2'].replace(',','.')
            density_km2 = float(density_km2)
            population_rank = int(year_pop_history['population_rank'])
            density_rank = int(year_pop_history['density_rank'])

            print(year, city_population, density_km2, population_rank, density_rank)

        for year_pop_history in population_projection_data['projection_population']:
            year = int(year_pop_history['population_year'])
            city_population = int(year_pop_history['population'].replace(',', ''))
            density_km2 = year_pop_history['density_km2'].replace(',','.')
            density_km2 = float(density_km2)
            population_rank = int(year_pop_history['population_rank'])
            density_rank = int(year_pop_history['density_rank'])

            print(year, city_population, density_km2, population_rank, density_rank)
        
        cntCountries += 1

# fill_db_with_continents()
# fill_db_with_countries()
# fill_db_with_cities()
fill_db_with_country_pop_projections()