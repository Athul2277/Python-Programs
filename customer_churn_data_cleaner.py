
import pandas as pd

data = pd.read_csv("customers.csv")
data.drop_duplicates(inplace=True)
data["Age"] = pd.to_numeric(data["Age"], errors="coerce")
data["MonthlyCharges"] = pd.to_numeric(data["MonthlyCharges"], errors="coerce")
data["Age"] = data["Age"].fillna(data["Age"].median())
data["MonthlyCharges"] = data["MonthlyCharges"].fillna(data["MonthlyCharges"].median())
data["Contract"] = data["Contract"].fillna("Unknown")
data.to_csv("cleaned_customers.csv", index=False)
print("Customer dataset cleaned successfully")
