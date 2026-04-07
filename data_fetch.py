import yfinance as yf
import pandas as pd

TICKER_MAP = {
    "hdfc bank": "HDFCBANK.NS",
    "sbi": "SBIN.NS",
    "reliance": "RELIANCE.NS",
    "tcs": "TCS.NS",
    "infosys": "INFY.NS",
    "icici bank": "ICICIBANK.NS",
    "apple": "AAPL"
}

def get_financial_data(company):

    ticker = TICKER_MAP.get(company.lower())

    if not ticker:
        return pd.DataFrame()

    stock = yf.Ticker(ticker)

    try:
        fin = stock.financials.T
        bal = stock.balance_sheet.T
        cf = stock.cashflow.T

        df = pd.DataFrame({
            "Year": fin.index.year,
            "Revenue": fin.get("Total Revenue", 0),
            "Net Profit": fin.get("Net Income", 0),
            "EBIT": fin.get("Operating Income", 0),
            "Debt": bal.get("Total Debt", 0),
            "Equity": bal.get("Total Stockholder Equity", 0),
            "OCF": cf.get("Operating Cash Flow", 0)
        })

        df = df.fillna(0)
        return df.sort_values("Year")

    except Exception as e:
        print("Error:", e)
        return pd.DataFrame()
