import duckdb
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR,"warehouse", "crypto.db")

def get_connection():
    return duckdb.connect(DB_PATH)