import pandas as pd

df = pd.read_csv("employees.csv")
distinct_dept_ids = df["DEPARTMENT_ID"].unique()

print("Distinct Department IDs:")
print(distinct_dept_ids)