import pandas as pd
df = pd.DataFrame({
    "name": [
        "Alberto Franco",
        "Gino Mcneill",
        "Ryan Parkes",
        "Eesha Hinton",
        "David Parkes"
    ]
})
substring = "Park"
df["position"] = df["name"].str.find(substring)

print(df)