import pandas as pd
df = pd.read_csv("job_history.csv")
job_count = df.groupby("EMPLOYEE_ID").size()
result = (
    df.groupby("EMPLOYEE_ID")
      .size()
      .reset_index(name="JOB_COUNT")
)
result = result[result["JOB_COUNT"] >= 2]
print(result)