import requests
import yfinance as yf

API_KEY = "YOUR_ALPHA_VANTAGE_KEY"

SYMBOL_MAP = {
    "hdfc bank": "HDFCBANK.BSE",
    "sbi": "SBIN.BSE",
    "reliance": "RELIANCE.BSE",
    "tcs": "TCS.BSE",
    "infosys": "INFY.BSE",
    "icici bank": "ICICIBANK.BSE"
}

def get_market_data(company):

    symbol = SYMBOL_MAP.get(company.lower())

    if not symbol:
        return {"price": 0, "market_cap": 0}

    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url).json()

        price = float(response["Global Quote"]["05. price"])

    except:
        price = 0

    # ✅ fallback using yfinance
    try:
        yf_symbol = symbol.replace(".BSE", ".NS")
        stock = yf.Ticker(yf_symbol)
        info = stock.info

        market_cap = info.get("marketCap", 0)

    except:
        market_cap = 0

    return {
        "price": price,
        "market_cap": market_cap
    }
