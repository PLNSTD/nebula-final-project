import src.database_psql.db_interface.connect as db

def setup_continents():
    conn = db.get_connection()
    cursor = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS continents (
    name VARCHAR(50) PRIMARY KEY,
    population BIGINT,
    world_population REAL,
    density_per_km REAL
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
    CREATE TABLE IF NOT EXISTS countries(
    name VARCHAR(50) PRIMARY KEY,
    continent VARCHAR(50) REFERENCES continents (name),
    population BIGINT,
    density_per_km2 REAL
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
    CREATE TABLE IF NOT EXISTS cities(
    name VARCHAR(50) PRIMARY KEY,
    country VARCHAR(50) REFERENCES countries (name),
    population BIGINT
    );
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def setup_historical_population():
    conn = db.get_connection()
    cursor = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS historical_population(
    country VARCHAR(50) REFERENCES countries (name),
    population_year INT,
    population BIGINT,
    density_per_km2 REAL,
    population_rank INT,
    density_rank INT,
    CONSTRAINT pk PRIMARY KEY(country, population_year)
    );
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def setup_projections_population():
    conn = db.get_connection()
    cursor = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS projections_population(
    country VARCHAR(50) REFERENCES countries (name),
    population_year INT,
    population BIGINT,
    density_per_km2 REAL,
    population_rank INT,
    density_rank INT,
    CONSTRAINT pk_project PRIMARY KEY(country, population_year)
    );
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()