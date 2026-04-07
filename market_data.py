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

    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()

        result = data.get("quoteResponse", {}).get("result", [])

        if not result:
            return {"price": 0, "market_cap": 0}

        return {
            "price": result[0].get("regularMarketPrice", 0),
            "market_cap": result[0].get("marketCap", 0)
        }

    except Exception as e:
        print("API ERROR:", e)
        return {"price": 0, "market_cap": 0}
