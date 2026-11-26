import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock.csv")
df["Date"] = pd.to_datetime(df["Date"])
start_date = "2020-04-01"
end_date = "2020-04-30"
data = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
plt.scatter(data["Volume"], data["Close"])
plt.xlabel("Trading Volume")
plt.ylabel("Stock Price (Close)")
plt.title("Alphabet Inc. Trading Volume vs Stock Price")
plt.show()