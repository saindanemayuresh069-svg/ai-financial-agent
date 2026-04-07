import yfinance as yf
import pandas as pd

def get_financial_data(company):

    # Try India first
    ticker = company.upper().replace(" ", "") + ".NS"

    stock = yf.Ticker(ticker)

    try:
        financials = stock.financials

        if financials.empty:
            raise Exception

    except:
        # fallback US ticker
        ticker = company.upper()
        stock = yf.Ticker(ticker)
        financials = stock.financials

    balance = stock.balance_sheet
    cashflow = stock.cashflow

    df = pd.DataFrame({
        "Year": financials.columns,
        "Revenue": financials.loc["Total Revenue"],
        "Net Profit": financials.loc["Net Income"],
        "EBIT": financials.loc["EBIT"],
        "Debt": balance.loc["Total Debt"],
        "Equity": balance.loc["Total Stockholder Equity"],
        "OCF": cashflow.loc["Total Cash From Operating Activities"]
    })

    df = df.dropna()
    df["Year"] = df["Year"].dt.year
    df = df.tail(5)  # latest 5 years only

    return df.sort_values("Year")
