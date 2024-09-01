import os
from dotenv import load_dotenv


load_dotenv()

# Database onnection string
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')
DB_NAME = os.environ.get('POSTGRES_NAME')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASS = os.environ.get('POSTGRES_PASS')
ECHO = os.environ.get('ECHO')
