import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(10, 4),
    columns=["A", "B", "C", "D"]
)

df.loc[0, "C"] = np.nan
df.loc[3, "D"] = np.nan
df.loc[5, "A"] = np.nan
df.loc[9, "D"] = np.nan

styled_df = df.style.highlight_null(color="red")

styled_df.to_html("output.html")

print(df)
print("\nStyled DataFrame saved as output.html")