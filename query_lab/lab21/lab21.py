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

# Swap uppercase and lowercase characters
df["name"] = df["name"].str.swapcase()

print(df)