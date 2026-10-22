
import statistics

prices = [120, 125, 118, 132, 140, 128, 145]

average = statistics.mean(prices)
volatility = statistics.stdev(prices)

print("Average Price:", round(average, 2))
print("Price Volatility:", round(volatility, 2))
print("Highest Price:", max(prices))
print("Lowest Price:", min(prices))

if volatility > 10:
    print("High Price Variation")
else:
    print("Relatively Stable Prices")
