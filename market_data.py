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

FMP_API_KEY = "v5IIHUYVDu8Zme5v7RkKj9bx4Fst"


def get_market_data(company):

    company = company.lower().strip()
    ticker = TICKER_MAP.get(company)

    if not ticker:
        return {"price": 0, "market_cap": 0}

    # 🔹 INDIA (Yahoo API)
    if ticker.endswith(".NS"):
        try:
            url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={ticker}"
            headers = {"User-Agent": "Mozilla/5.0"}

            res = requests.get(url, headers=headers, timeout=5).json()
            result = res.get("quoteResponse", {}).get("result", [])

            if result:
                return {
                    "price": result[0].get("regularMarketPrice", 0),
                    "market_cap": result[0].get("marketCap", 0)
                }

        except:
            pass

    # 🔹 US (FMP API)
    else:
        try:
            url = f"https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey={FMP_API_KEY}"
            data = requests.get(url).json()

            if data:
                return {
                    "price": data[0].get("price", 0),
                    "market_cap": data[0].get("marketCap", 0)
                }

        except:
            pass

    return {"price": 0, "market_cap": 0}
