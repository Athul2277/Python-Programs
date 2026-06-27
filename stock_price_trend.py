import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download(
    "AAPL",
    period="6mo"
)

plt.plot(data["Close"])

plt.title("Apple Stock Price")

plt.show()
