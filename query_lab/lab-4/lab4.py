import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock.csv")
df["Date"] = pd.to_datetime(df["Date"])
start_date = "2023-01-03"
end_date = "2023-01-09"
filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
plt.figure(figsize=(10,5))
plt.plot(filtered_df["Date"], filtered_df["Close"], marker='o')
plt.title("Alphabet Inc. Historical Stock Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.grid(True)
plt.xticks(rotation=45)
plt.show()