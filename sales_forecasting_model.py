
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("monthly_sales.csv")
data["Month_Number"] = range(1, len(data) + 1)
X = data[["Month_Number"]]
y = data["Sales"]
model = LinearRegression()
model.fit(X, y)
next_month = [[len(data) + 1]]
forecast = model.predict(next_month)[0]
print("Forecasted next month sales:", round(forecast, 2))
