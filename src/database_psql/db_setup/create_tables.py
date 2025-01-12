import database_psql.db_interface.connect as db

def setup_continents():
    conn = db.get_connection()
    cursor = conn.cursor()
    query = """
    CREATE TABLE continents (
    name VARCHAR(50) PRIMARY KEY,
    population INTEGER,
    world_population REAL,
    density_per_km INTEGER
    );
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

# TODO
def setup_countries():
    pass

# TODO
def setup_cities():
    pass
