def get_col(df, possible_names):
    for col in df.columns:
        if col.lower() in [name.lower() for name in possible_names]:
            return col
    return None

def calculate_ratios(df):
    latest = df.iloc[-1]
    first = df.iloc[0]

    revenue_col = get_col(df, ["Revenue", "Sales", "Total Income"])
    profit_col = get_col(df, ["Net Profit", "PAT"])
    debt_col = get_col(df, ["Debt", "Borrowings"])
    equity_col = get_col(df, ["Equity", "Net Worth"])
    interest_col = get_col(df, ["Interest"])
    ocf_col = get_col(df, ["OCF", "Operating Cash Flow"])
    ebit_col = get_col(df, ["EBIT", "Operating Profit"])

    if None in [revenue_col, profit_col, debt_col, equity_col]:
        raise ValueError("Required columns not found in Excel")

    revenue_cagr = (latest[revenue_col] / first[revenue_col])**(1/4) - 1
    roe = latest[profit_col] / latest[equity_col]
    debt_equity = latest[debt_col] / latest[equity_col]

    interest_coverage = latest[ebit_col] / latest[interest_col] if interest_col and ebit_col else 0
    ocf_ratio = latest[ocf_col] / latest[profit_col] if ocf_col else 0

    return {
        "cagr": revenue_cagr,
        "roe": roe,
        "de": debt_equity,
        "icr": interest_coverage,
        "ocf_ratio": ocf_ratio
    }
