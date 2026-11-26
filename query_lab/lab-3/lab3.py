import pandas as pd
df = pd.read_csv("jobs.csv")
result = df.sort_values(by="JOB_TITLE", ascending=False)
print(result)   