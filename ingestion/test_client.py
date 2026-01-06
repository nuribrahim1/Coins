from ingestion.coingecko_client import CoinGeckoClient

client = CoinGeckoClient()

markets = client.get_markets()
print(markets[0])

chart = client.get_market_chart("bitcoin", days=7)
print(chart)