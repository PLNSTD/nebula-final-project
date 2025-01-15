from src.database_psql.db_interface import connect as db
from flask import jsonify

def insert(name, population, world_population, density_per_km):
    conn = db.get_connection()
    try:
        cur = conn.cursor()
        query = """
        INSERT INTO continents (name, population, world_population, density_per_km) 
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name) DO UPDATE
        SET
            population = EXCLUDED.population,
            world_population = EXCLUDED.world_population,
            density_per_km = EXCLUDED.density_per_km;
        """
        cur.execute(query, (name, population, world_population, density_per_km))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def get_all():
    conn = db.get_connection()
    try:
        cur = conn.cursor()
        cur.execute('SELECT * FROM continents;')
        continents = cur.fetchall()
        return continents  # Return the fetched data
    except Exception as e:
        raise e  # Re-raise the exception for the caller to handle
    finally:
        cur.close()
        conn.close()
