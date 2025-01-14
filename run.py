from flask import Flask, request, send_file
from src.database_psql.data_operations import historical_population as historical_pop_table
from src.database_psql.data_operations import projections_population as projections_pop_table
from src.database_psql.data_operations import countries as country_table
from src import data_visualization as dv_plot
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
plt.switch_backend('Agg')

@app.route('/')
def index():
    return 'Welcome to the Flask API with psycopg2!'

@app.errorhandler(404)
def page_not_found(Error = None):
    return "404 Error: The page you're looking for doesn't exist.", 404

@app.route('/population_chart/<country>', methods=['GET'])
def get_population_chart_by_country(country):
    country = country.title()
    db_rows = country_table.get_by_name(country)

    if len(db_rows) == 0:
        return page_not_found()

    projections_df = projections_pop_table.get_by_country_to_dataframe(country)
    historical_df = historical_pop_table.get_by_country_to_dataframe(country)

    df_combined = pd.concat([
        projections_df[['population_year', 'population']],
        historical_df[['population_year', 'population']]
    ], ignore_index=True)

    df_combined = df_combined.drop_duplicates(subset='population_year', keep='first').sort_values(by='population_year')
    
    buf = dv_plot.plot_population_trends(df_combined, country)
    # return 'You are looking for ' + country
    return send_file(buf, mimetype='image/png') 

@app.route('/population_chart', methods=['GET'])
def population_chart():
    # Get the list of countries from the query parameters
    countries_arg = request.args.getlist('country')  # Expects a list like ?country=USA&country=India
    countries_to_fetch = []
    countries_dataframes = {}
    for country in countries_arg:
        country = country.title()
        db_rows = country_table.get_by_name(country)

        if len(db_rows) > 0:
            countries_to_fetch.append(db_rows[0][0])

        projections_df = projections_pop_table.get_by_country_to_dataframe(country)
        historical_df = historical_pop_table.get_by_country_to_dataframe(country)

        df_combined = pd.concat([
            projections_df[['population_year', 'population']],
            historical_df[['population_year', 'population']]
        ], ignore_index=True)

        df_combined = df_combined.drop_duplicates(subset='population_year', keep='first').sort_values(by='population_year')
        
        countries_dataframes.update({country: df_combined})

    if not countries_dataframes:
        return "No valid countries provided", 404

    # Call the function to generate the plot
    buf = dv_plot.plot_population_comparison_trends(countries_dataframes, countries_to_fetch)

    # Send the image to the client
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)