import requests
import yfinance as yf

API_KEY = "v5IIHUYVDu8Zme5v7RkKj9bx4Fst"

SYMBOL_MAP = {
    "hdfc bank": "HDFCBANK.BSE",
    "sbi": "SBIN.BSE",
    "reliance": "RELIANCE.BSE",
    "tcs": "TCS.BSE",
    "infosys": "INFY.BSE",
    "icici bank": "ICICIBANK.BSE"
}

def get_market_data(company):
    company = company.lower().strip()
    symbol = SYMBOL_MAP.get(company)

    if not symbol:
        return {"price": 0, "market_cap": 0}

    price = 0
    market_cap = 0

    # 🔹 Alpha Vantage
    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url).json()

        if "Global Quote" in response:
            price = float(response["Global Quote"].get("05. price", 0))
    except:
        pass

    # 🔹 yfinance fallback
    try:
        yf_symbol = symbol.replace(".BSE", ".NS")
        stock = yf.Ticker(yf_symbol)
        info = stock.info

        if price == 0:
            price = info.get("currentPrice", 0)

        market_cap = info.get("marketCap", 0)
    except:
        pass

    return {
        "price": price,
        "market_cap": market_cap
    }
