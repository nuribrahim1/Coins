from sample_prices import sample_prices
from normalise import normalise
import matplotlib.pyplot as plt

rows = normalise("bitcoin", sample_prices, "price_usd")

for row in rows:
    print(row)

X = [row["event_time"] for row in rows]
y = [row["price_usd"] for row in rows]
plt.plot(X,y)
plt.show()