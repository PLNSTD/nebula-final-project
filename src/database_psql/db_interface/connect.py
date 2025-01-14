from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor
import os

# Load environment variables from the .env file
load_dotenv()

# Access the variables from the .env file
dbname = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')

def get_connection():
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )
        # print("Connected to the database successfully")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
