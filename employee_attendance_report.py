
import pandas as pd

data = pd.read_csv("attendance.csv")
data["Date"] = pd.to_datetime(data["Date"])
summary = data.groupby("Employee_ID").agg(
    total_days=("Date", "nunique"),
    present_days=("Status", lambda x: (x == "Present").sum())
)
summary["attendance_rate"] = summary["present_days"] / summary["total_days"] * 100
summary.to_csv("attendance_report.csv")
print(summary.sort_values("attendance_rate"))
