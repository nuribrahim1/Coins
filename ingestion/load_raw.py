from ingestion.coingecko_client import CoinGeckoClient
from ingestion.normalise import normalise
from warehouse.connection import get_connection

client = CoinGeckoClient()
connection = get_connection()

coin_id = "bitcoin"

# Extraction
values = client.get_market_chart(coin_id, "gbp", 30)

# Normalisation
price_rows = normalise(coin_id, values["prices"], "price_gbp")
market_cap_rows = normalise(coin_id, values["market_caps"], "market_cap_gbp")
volume_rows = normalise(coin_id, values["total_volumes"], "volume_gbp")

# Create Tables
connection.execute("""
CREATE TABLE IF NOT EXISTS raw_prices (
    coin_id TEXT,
    event_time TIMESTAMP,
    price_gbp DOUBLE,
    PRIMARY KEY (coin_id, event_time)
)
""")

connection.execute("""
CREATE TABLE IF NOT EXISTS raw_market_caps (
    coin_id TEXT,
    event_time TIMESTAMP,
    market_cap_gbp DOUBLE,
    PRIMARY KEY (coin_id, event_time)
)
""")

connection.execute("""
CREATE TABLE IF NOT EXISTS raw_volumes (
    coin_id TEXT,
    event_time TIMESTAMP,
    volume_gbp DOUBLE,
    PRIMARY KEY (coin_id, event_time)
)
""")

# Insert rows

connection.executemany("""
INSERT OR IGNORE INTO raw_prices VALUES (? ,? ,?)
""", [(r["coin_id"], r["event_time"], r["price_gbp"]) for r in price_rows])

connection.executemany("""
INSERT OR IGNORE INTO raw_market_caps VALUES (? ,? ,?)
""", [(r["coin_id"], r["event_time"], r["market_cap_gbp"]) for r in market_cap_rows])

connection.executemany("""
INSERT OR IGNORE INTO raw_volumes VALUES (? ,? ,?)
""", [(r["coin_id"], r["event_time"], r["volume_gbp"]) for r in volume_rows])

connection.close()