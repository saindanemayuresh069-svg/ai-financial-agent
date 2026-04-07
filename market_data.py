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

    company_lower = company.lower().strip()

    # 🔥 STEP 1: FIX TICKER
    ticker = TICKER_MAP.get(company_lower)

    if not ticker:
        ticker = company_upper = company.upper().replace(" ", "")
    
    # 🔍 DEBUG
    print("Using ticker:", ticker)

    # 🔹 TRY DIRECT API FIRST (MORE RELIABLE)
    try:
        url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}"
        res = requests.get(url)
        data = res.json()

        result = data["quoteResponse"]["result"]

        if result:
            return {
                "price": result[0].get("regularMarketPrice", 0),
                "market_cap": result[0].get("marketCap", 0)
            }

    except Exception as e:
        print("API error:", e)

    # 🔹 FALLBACK TO YFINANCE
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")

        if not hist.empty:
            return {
                "price": float(hist["Close"].iloc[-1]),
                "market_cap": float(stock.info.get("marketCap", 0))
            }

    except Exception as e:
        print("yfinance error:", e)

    return {"price": 0, "market_cap": 0}
