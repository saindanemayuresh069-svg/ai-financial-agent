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

    ticker_symbol = TICKER_MAP.get(company.lower())

    if not ticker_symbol:
        return pd.DataFrame()

    stock = yf.Ticker(ticker_symbol)

    try:
        financials = stock.financials.T
        balance = stock.balance_sheet.T
        cashflow = stock.cashflow.T

        df = pd.DataFrame({
            "Year": financials.index.year,
            "Revenue": financials["Total Revenue"],
            "Net Profit": financials["Net Income"],
            "EBIT": financials.get("Ebit", 0),
            "Debt": balance.get("Total Debt", 0),
            "Equity": balance.get("Total Stockholder Equity", 0),
            "OCF": cashflow.get("Total Cash From Operating Activities", 0)
        })

        return df.dropna()

    except:
        return pd.DataFrame()
