import psycopg2
from psycopg2.extras import RealDictCursor

def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="nebuladb",
            user="nebuladb_owner",
            password="T7XYaZjPgF9w",
            host="ep-patient-dream-a4vag2b0.us-east-1.aws.neon.tech"
        )
        connection.autocommit = True
        print("Connected to the database successfully")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")

def setup_continents():
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    query = """
    CREATE TABLE continents (
    name VARCHAR(50) PRIMARY KEY,
    population INTEGER,
    world_population REAL,
    density_per_km INTEGER
    );
    """
    cursor.execute(query)
    cursor.close()
    db_connection.close()

def add_continent(name, population, world_population, density_per_km):
    conn = connect_to_db()
    cur = conn.cursor()
    query = """
    INSERT INTO continents (name, population, world_population, density_per_km) VALUES(%s, %s, %s, %s);"""
    cur.execute(query, (name, population, world_population, density_per_km))
    cur.close()
    conn.close()

# setup_continents()
# add_continent('Oceania', 46088704, 0.58, 5)