from ingestion.coingecko_client import CoinGeckoClient
from datetime import datetime
import matplotlib.pyplot as plt


client = CoinGeckoClient()

markets = client.get_markets()
print(markets[0])

chart = client.get_market_chart("bitcoin", days=7)


coordinates = chart['prices']

print(coordinates)
X = []
y = []

for i in coordinates:
    X.append(datetime.fromtimestamp(i[0]/1000))
    y.append(round(i[1],2))

plt.plot(X,y)
plt.show()



