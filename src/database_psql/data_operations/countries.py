from src.database_psql.db_interface import connect as db

def insert(name, continent, population, density_per_km):
    conn = db.get_connection()
    try:
        cur = conn.cursor()
        query = """
        INSERT INTO countries (name, continent, population, density_per_km2)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name) DO UPDATE
        SET 
            continent = EXCLUDED.continent,
            population = EXCLUDED.population,
            density_per_km2 = EXCLUDED.density_per_km2;
        """
        cur.execute(query, (name, continent, population, density_per_km))
        conn.commit()
    except Exception as e:
        conn.rollback()  # Rollback in case of an error
        raise e  # Re-raise the exception for the caller to handle
    finally:
        cur.close()
        conn.close()

def get_all():
    conn = db.get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM countries;")
        countries = cur.fetchall()
        return countries
    except Exception as e:
        raise e  # Re-raise the exception for handling by the caller
    finally:
        cur.close()
        conn.close()

def get_by_name(country):
    conn = db.get_connection()
    try:
        cur = conn.cursor()
        query = "SELECT * FROM countries WHERE name = %s;"
        cur.execute(query, (country,))
        countries = cur.fetchall()
        return countries
    except Exception as e:
        raise e  # Re-raise the exception for handling by the caller
    finally:
        cur.close()
        conn.close()