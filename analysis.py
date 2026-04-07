def get_col(df, names):
    for name in names:
        if name in df.columns:
            return name
    return None


def calculate_ratios(df):

    if df is None or df.empty or len(df) < 2:
        raise ValueError("Insufficient data")

    latest = df.iloc[-1]
    first = df.iloc[0]

    revenue_col = get_col(df, ["Revenue", "Total Revenue"])
    profit_col = get_col(df, ["Net Profit", "Net Income"])
    ebit_col = get_col(df, ["EBIT", "Operating Income"])

    debt_col = get_col(df, ["Debt", "Total Debt"])
    equity_col = get_col(df, ["Equity", "Total Stockholder Equity"])
    ocf_col = get_col(df, ["OCF", "Total Cash From Operating Activities"])
    interest_col = get_col(df, ["Interest"])

    if not revenue_col or not profit_col:
        raise ValueError("Revenue or Profit column missing")

    revenue = latest[revenue_col]
    first_revenue = first[revenue_col]
    profit = latest[profit_col]

    equity = latest[equity_col] if equity_col else 1
    debt = latest[debt_col] if debt_col else 0
    ebit = latest[ebit_col] if ebit_col else 0
    ocf = latest[ocf_col] if ocf_col else 0
    interest = latest[interest_col] if interest_col else 0

    cagr = (revenue / first_revenue)**(1/4) - 1
    roe = profit / equity if equity else 0
    de = debt / equity if equity else 0
    icr = ebit / interest if interest else 0
    ocf_ratio = ocf / profit if profit else 0

    return {
        "cagr": cagr,
        "roe": roe,
        "de": de,
        "icr": icr,
        "ocf_ratio": ocf_ratio
    }
