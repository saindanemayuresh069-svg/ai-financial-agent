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

    company = company.lower().strip()
    ticker = TICKER_MAP.get(company)

    if not ticker:
        return {"price": 0, "market_cap": 0}

    try:
        url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}"
        res = requests.get(url, timeout=5)
        data = res.json()

        result = data.get("quoteResponse", {}).get("result", [])

        if not result:
            return {"price": 0, "market_cap": 0}

        return {
            "price": result[0].get("regularMarketPrice", 0),
            "market_cap": result[0].get("marketCap", 0)
        }

    except Exception as e:
        print("Market API error:", e)
        return {"price": 0, "market_cap": 0}
