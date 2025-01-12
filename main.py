from src.fetch_data.fetch_continents import fetch_continents_from_page as fetch_continents
from src.fetch_data.fetch_countries import fetch__countries_by_continent as fetch_countries
from src.fetch_data.fetch_cities import fetch_country_cities as fetch_cities
from src.database_psql.db_setup import create_tables
from src.database_psql.data_operations import continents as continents_table
from src.database_psql.data_operations import countries as countries_table
from src.database_psql.data_operations import cities as cities_table

def fill_db_with_continents():
    create_tables.setup_continents()
    continents = fetch_continents()

    for continent in continents:
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

    print('Complete Continents')

def fill_db_with_countries():
    create_tables.setup_countries()
    continents = continents_table.get_all()

    for continent in continents:
        original_continent_name = continent[0]
        continent_name = original_continent_name.lower()
        continent_name = continent_name.replace(' ', '-')
        countries = fetch_countries(continent_name)

        for country in countries:
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

        print('Completed ' + continent_name)
        # x = input('Continue?')
        x = 1
        if x == 0:
            return
    print('Completed all countries')

def fill_db_with_cities():
    countries = countries_table.get_all()
    for country in countries:
        original_country_name = country[0]
        country_name = original_country_name.lower()
        country_name = country_name.replace(' ','-')
        cities = fetch_cities(country_name)

        for city_tuple in cities:
            city_name = city_tuple[0]
            city_population = city_tuple[1]

        print('Completed ' + country_name)
        x = 1
        x = input('Continue?')
        if x == 0:
            return

# fill_db_with_continents()
# fill_db_with_countries()
fill_db_with_cities()