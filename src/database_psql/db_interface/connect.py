import psycopg2
from psycopg2.extras import RealDictCursor
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# construct the file path relative to the script's location
credentials_path = os.path.join(current_dir, './db_credentials.txt')

def get_connection():
    try:
        # Get hidden db password
        with open(credentials_path, 'r') as credential_file:
            password = credential_file.read()
        
        connection = psycopg2.connect(
            dbname="nebuladb",
            user="nebuladb_owner",
            password=password,
            host="ep-patient-dream-a4vag2b0.us-east-1.aws.neon.tech"
        )
        # print("Connected to the database successfully")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
