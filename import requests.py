import requests
import pandas as pd
import time

# Alpha Vantage API Key (Get your own at https://www.alphavantage.co/support/#api-key)
API_KEY = "YOUR_API_KEY"

# API URL to get stock market data (Example: Microsoft stock prices)
API_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&apikey={API_KEY}"

# Fetch the data
response = requests.get(API_URL)

# Ensure API response is successful
if response.status_code == 200:
    data = response.json()

    # Extract relevant stock price data
    if "Time Series (Daily)" in data:
        df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
        df = df.rename(columns={
            "1. open": "Open",
            "2. high": "High",
            "3. low": "Low",
            "4. close": "Close",
            "5. adjusted close": "Adj_Close",
            "6. volume": "Volume"
        })
        df.index = pd.to_datetime(df.index)  # Convert index to datetime

        # Save to CSV
        df.to_csv("data/raw/financial_risk.csv", index=True)
        print("✅ Data successfully fetched and saved as financial_risk.csv")

    else:
        print("❌ API response is missing expected data structure.")

else:
    print(f"❌ API request failed with status code {response.status_code}")
