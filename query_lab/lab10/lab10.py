import pandas as pd
import webbrowser
import os

df = pd.read_csv("random_data.csv")

def highlight_numbers(value):
    if value < 0:
        return "color: red"
    else:
        return "color: black"

styled_df = df.style.map(highlight_numbers)
file_name = "output.html"
styled_df.to_html(file_name)
webbrowser.open("file://" + os.path.realpath(file_name))

print("Output generated successfully!")