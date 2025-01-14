from src.database_psql.db_interface import connect as db

def insert(name, continent, population, density_per_km):
    conn = db.get_connection()
    cur = conn.cursor()
    query = """
    INSERT INTO countries (name, continent, population, density_per_km2) VALUES(%s, %s, %s, %s) ON CONFLICT DO NOTHING;"""
    cur.execute(query, (name, continent, population, density_per_km))
    conn.commit()
    cur.close()
    conn.close()

def get_all():
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM countries;')
    countries = cur.fetchall()
    cur.close()
    conn.close()
    
    return countries

def get_by_name(country):
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM countries where name = '{country}';")
    countries = cur.fetchall()
    cur.close()
    conn.close()
    
    return countries