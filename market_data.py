import requests

API_KEY = "YOUR_API_KEY_HERE"

TICKER_MAP = {
    "hdfc bank": "HDFCBANK.NS",
    "sbi": "SBIN.NS",
    "reliance": "RELIANCE.NS",
    "tcs": "TCS.NS",
    "infosys": "INFY.NS",

    "apple": "AAPL",
    "tesla": "TSLA",
    "microsoft": "MSFT",
    "google": "GOOGL",
}


def get_market_data(company):

    ticker = TICKER_MAP.get(company)

    if not ticker:
        return {"price": 0, "market_cap": 0}

    try:
        url = f"https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey={API_KEY}"
        data = requests.get(url).json()

        if not data:
            return {"price": 0, "market_cap": 0}

        return {
            "price": data[0].get("price", 0),
            "market_cap": data[0].get("marketCap", 0)
        }

    except:
        return {"price": 0, "market_cap": 0}
