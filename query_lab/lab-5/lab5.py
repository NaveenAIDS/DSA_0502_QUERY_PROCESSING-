import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock.csv")
df["Date"] = pd.to_datetime(df["Date"])
data = df[(df["Date"] >= "2020-06-01") & (df["Date"] <= "2020-06-30")]
plt.bar(data["Date"].dt.strftime("%d-%b"), data["Volume"], color="green")
plt.title("Alphabet Inc. Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.xticks(rotation=45)
plt.show()