from src.database_psql.db_interface import connect as db
import pandas as pd

def insert(country, year_pop, population, density_per_km2, pop_rank, density_rank):
    conn = db.get_connection()
    try:
        cur = conn.cursor()
        query = """
        INSERT INTO historical_population (country, population_year, population, density_per_km2, population_rank, density_rank)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (country, population_year) DO UPDATE
        SET 
            population = EXCLUDED.population,
            density_per_km2 = EXCLUDED.density_per_km2,
            population_rank = EXCLUDED.population_rank,
            density_rank = EXCLUDED.density_rank;
        """
        cur.execute(query, (country, year_pop, population, density_per_km2, pop_rank, density_rank))
        conn.commit()
    except Exception as e:
        conn.rollback()  # Rollback the transaction in case of an error
        raise e
    finally:
        cur.close()
        conn.close()

def get_by_country(country):
    conn = db.get_connection()
    try:
        cur = conn.cursor()
        query = """
        SELECT * FROM historical_population WHERE country = %s;
        """
        cur.execute(query, (country,))
        years_record = cur.fetchall()
        return years_record
    except Exception as e:
        raise e
    finally:
        cur.close()
        conn.close()

def get_by_country_to_dataframe(country):
    conn = db.get_connection()
    try:
        query = """
        SELECT * FROM historical_population WHERE country = %s;
        """
        dataframe = pd.read_sql_query(query, conn, params=(country,))
        return dataframe
    except Exception as e:
        raise e
    finally:
        conn.close()