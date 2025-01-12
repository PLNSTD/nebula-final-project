from src.database_psql.db_interface import connect as db

def insert(name, continent, population, density_per_km):
    conn = db.get_connection()
    cur = conn.cursor()
    query = """
    INSERT INTO countries (name, continent, population, density_per_km2) VALUES(%s, %s, %s, %s);"""
    cur.execute(query, (name, continent, population, density_per_km))
    conn.commit()
    cur.close()
    conn.close()