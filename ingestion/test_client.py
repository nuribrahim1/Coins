from ingestion.coingecko_client import CoinGeckoClient
from datetime import datetime, UTC
import matplotlib.pyplot as plt


client = CoinGeckoClient()

raw_snapshot = client.get_markets()
print(raw_snapshot[0])

raw_price_timeseries = client.get_market_chart("bitcoin", days=7)


def represent(metric:str):
    coordinates = raw_price_timeseries[metric]

    print(coordinates)
    X = []
    y = []

    for i in coordinates:
        X.append(datetime.fromtimestamp((i[0]/1000),UTC))
        y.append(round(i[1],2))

    plt.plot(X,y)
    plt.show()

represent("prices")
represent("market_caps")
represent("total_volumes")



