from src.database_psql.db_interface import connect as db

def insert(name, country, population):
    conn = db.get_connection()
    cur = conn.cursor()
    query = """
    INSERT INTO cities (name, country, population) VALUES(%s, %s, %s);"""
    cur.execute(query, (name, country, population))
    conn.commit()
    cur.close()
    conn.close()