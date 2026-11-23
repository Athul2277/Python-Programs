import sqlite3
import pandas as pd
from datetime import datetime

connection = sqlite3.connect("business.db")
report = pd.read_sql_query(
    "SELECT department, COUNT(*) AS employees FROM employees GROUP BY department",
    connection
)
filename = f"employee_report_{datetime.now():%Y%m%d}.csv"
report.to_csv(filename, index=False)
print(report)
print("Report generated:", filename)
connection.close()
