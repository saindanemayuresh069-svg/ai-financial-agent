import yfinance as yf
import pandas as pd


def safe_get(df, keys):
    for key in keys:
        if df is not None and key in df.index:
            return df.loc[key]
    return None


def get_financial_data(company):

    ticker = company.upper().replace(" ", "") + ".NS"

    try:
        stock = yf.Ticker(ticker)
        financials = stock.financials

        if financials.empty:
            raise Exception

    except:
        ticker = company.upper()
        stock = yf.Ticker(ticker)
        financials = stock.financials

    balance = stock.balance_sheet
    cashflow = stock.cashflow

    revenue = safe_get(financials, ["Total Revenue"])
    profit = safe_get(financials, ["Net Income"])
    ebit = safe_get(financials, ["EBIT", "Operating Income"])
    debt = safe_get(balance, ["Total Debt"])
    equity = safe_get(balance, [
        "Total Stockholder Equity",
        "Stockholders Equity",
        "Total Equity Gross Minority Interest"
    ])
    ocf = safe_get(cashflow, [
        "Total Cash From Operating Activities",
        "Operating Cash Flow"
    ])

    df = pd.DataFrame({
        "Year": financials.columns,
        "Revenue": revenue,
        "Net Profit": profit,
        "EBIT": ebit if ebit is not None else 0,
        "Debt": debt if debt is not None else 0,
        "Equity": equity if equity is not None else 0,
        "OCF": ocf if ocf is not None else 0
    })

    df = df.dropna()
    df["Year"] = df["Year"].dt.year

    return df.sort_values("Year").tail(5)
