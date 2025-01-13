from src.database_psql.db_interface import connect as db

def insert(country, year_pop, population, density_per_km2, pop_rank, density_rank):
    conn = db.get_connection()
    cur = conn.cursor()
    query = """
    INSERT INTO projections_population (country, population_year, population, density_per_km2, population_rank, density_rank) VALUES(%s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;"""
    cur.execute(query, (country, year_pop, population, density_per_km2, pop_rank, density_rank))
    conn.commit()
    cur.close()
    conn.close()