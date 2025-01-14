from src.database_psql.db_interface import connect as db
import pandas as pd

def insert(country, year_pop, population, density_per_km2, pop_rank, density_rank):
    conn = db.get_connection()
    cur = conn.cursor()
    query = """
    INSERT INTO historical_population (country, population_year, population, density_per_km2, population_rank, density_rank) VALUES(%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;"""
    cur.execute(query, (country, year_pop, population, density_per_km2, pop_rank, density_rank))
    conn.commit()
    cur.close()
    conn.close()

def get_by_country(country):
    conn = db.get_connection()
    cur = conn.cursor()
    query = """
    SELECT * FROM historical_population WHERE country = %s;
    """
    cur.execute(query, (country,))
    years_record = cur.fetchall()
    cur.close()
    conn.close()
    
    return years_record

def get_by_country_to_dataframe(country):
    query = f"SELECT * FROM historical_population WHERE country = '{country}';"
    dataframe = pd.read_sql_query(query, db.get_connection())
    return dataframe