from src.database_psql.db_interface import connect as db

def insert(name, country, population):
    conn = db.get_connection()
    try:
        cur = conn.cursor()
        query = """
        INSERT INTO cities (name, country, population) 
        VALUES (%s, %s, %s) 
        ON CONFLICT (name) DO UPDATE 
        SET 
            country = EXCLUDED.country,
            population = EXCLUDED.population;
        """
        cur.execute(query, (name, country, population))
        conn.commit()
    except Exception as e:
        conn.rollback()  # Rollback in case of an error
        raise e  # Re-raise the exception for handling by the caller
    finally:
        cur.close()
        conn.close()

def get_all():
    conn = db.get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM cities;")
        cities = cur.fetchall()
        return cities
    except Exception as e:
        raise e  # Re-raise the exception for handling by the caller
    finally:
        cur.close()
        conn.close()
