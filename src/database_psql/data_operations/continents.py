from src.database_psql.db_interface import connect as db
from flask import jsonify

def insert(name, population, world_population, density_per_km):
    conn = db.get_connection()
    cur = conn.cursor()
    query = """
    INSERT INTO continents (name, population, world_population, density_per_km) VALUES(%s, %s, %s, %s);"""
    cur.execute(query, (name, population, world_population, density_per_km))
    conn.commit()
    cur.close()
    conn.close()

def get_all():
    conn = db.get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM continents;')
    continents = cur.fetchall()
    cur.close()
    conn.close()
    
    return continents
