import database_psql.db_interface.connect as db

def setup_continents():
    conn = db.get_connection()
    cursor = conn.cursor()
    query = """
    CREATE TABLE continents IF NOT EXISTS(
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

def setup_countries():
    conn = db.get_connection()
    cursor = conn.cursor()
    query = """
    CREATE TABLE countries IF NOT EXISTS(
    name VARCHAR(50) PRIMARY KEY,
    continent VARCHAR(50) REFERENCES continents (name),
    population INTEGER,
    density_per_km2 INTEGER
    );
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def setup_cities():
    conn = db.get_connection()
    cursor = conn.cursor()
    query = """
    CREATE TABLE cities IF NOT EXISTS(
    name VARCHAR(50) PRIMARY KEY,
    country VARCHAR(50) REFERENCES countries (name),
    population INTEGER,
    );
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
