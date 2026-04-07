import requests
import streamlit as st
import yfinance as yf

API_KEY = st.secrets["ALPHA_VANTAGE_API_KEY"]

TICKER_MAP = {
    "hdfc bank": "HDFCBANK.BSE",
    "sbi": "SBIN.BSE",
    "reliance": "RELIANCE.BSE",
    "tcs": "TCS.BSE",
    "infosys": "INFY.BSE",
    "icici bank": "ICICIBANK.BSE",
    "apple": "AAPL"
}

def get_market_data(company):

    symbol = TICKER_MAP.get(company.lower())

    if not symbol:
        return {"price": 0, "market_cap": 0}

    # 🔹 Alpha Vantage
    # 🔹 fallback for market cap
try:
    yf_symbol = symbol.replace(".BSE", ".NS")
    stock = yf.Ticker(yf_symbol)
    info = stock.info

    market_cap = info.get("marketCap", 0)

    return {
        "price": price,
        "market_cap": market_cap
    }
except:
    pass
    try:
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url).json()

        price = float(response["Global Quote"]["05. price"])

        return {
            "price": price,
            "market_cap": 0  # free API limitation
        }

    except:
        pass

    # 🔹 Fallback: yfinance
    try:
        ticker = symbol.replace(".BSE", ".NS")
        stock = yf.Ticker(ticker)
        info = stock.info

        return {
            "price": info.get("currentPrice", 0),
            "market_cap": info.get("marketCap", 0)
        }

    except:
        return {"price": 0, "market_cap": 0}
