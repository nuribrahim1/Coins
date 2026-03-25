import duckdb
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR,"warehouse", "crypto.db")

def get_connection():
    return duckdb.connect(DB_PATH)

connection = duckdb.connect(DB_PATH)

print(connection.execute("SELECT * FROM fact_crypto LIMIT 10").fetchall())