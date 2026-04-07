import yfinance as yf
import requests


TICKER_MAP = {
    "hdfc bank": "HDFCBANK.NS",
    "sbi": "SBIN.NS",
    "reliance": "RELIANCE.NS",
    "tcs": "TCS.NS",
    "infosys": "INFY.NS",
    "icici bank": "ICICIBANK.NS",

    "apple": "AAPL",
    "tesla": "TSLA",
    "microsoft": "MSFT",
    "google": "GOOGL",
    "amazon": "AMZN"
}


def get_market_data(company):

    ticker = TICKER_MAP.get(company.lower())

    if not ticker:
        ticker = company.upper().replace(" ", "") + ".NS"

    # 🔹 TRY YAHOO FIRST
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")

        if not hist.empty:
            price = hist["Close"].iloc[-1]
            market_cap = stock.info.get("marketCap", 0)

            return {
                "price": float(price),
                "market_cap": float(market_cap)
            }

    except:
        pass

    # 🔹 FALLBACK (FREE API - VERY STABLE)
    try:
        url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}"
        res = requests.get(url)
        data = res.json()

        result = data["quoteResponse"]["result"][0]

        return {
            "price": result.get("regularMarketPrice", 0),
            "market_cap": result.get("marketCap", 0)
        }

    except:
        return {
            "price": 0,
            "market_cap": 0
        }
