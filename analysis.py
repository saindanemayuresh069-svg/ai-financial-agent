def calculate_ratios(df):

    # 🔒 Safety check
    if df is None or df.empty:
        raise ValueError("Excel file is empty or not readable")

    if len(df) < 2:
        raise ValueError("Need at least 2 rows (years) for analysis")

    latest = df.iloc[-1]
    first = df.iloc[0]
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


def calculate_score(r):
    score = 0

    if r["cagr"] > 0.15: score += 5 * 0.25
    elif r["cagr"] > 0.1: score += 4 * 0.25
    elif r["cagr"] > 0.05: score += 3 * 0.25
    else: score += 2 * 0.25

    if r["roe"] > 0.2: score += 5 * 0.25
    elif r["roe"] > 0.15: score += 4 * 0.25
    elif r["roe"] > 0.1: score += 3 * 0.25
    else: score += 2 * 0.25

    if r["de"] < 0.5: score += 5 * 0.2
    elif r["de"] < 1: score += 4 * 0.2
    elif r["de"] < 2: score += 3 * 0.2
    else: score += 1 * 0.2

    if r["ocf_ratio"] > 1.2: score += 5 * 0.2
    elif r["ocf_ratio"] > 1: score += 4 * 0.2
    elif r["ocf_ratio"] > 0.8: score += 3 * 0.2
    else: score += 1 * 0.2

    return round(score, 2)


def detect_red_flags(r):
    flags = []

    if r["icr"] < 2:
        flags.append("Low interest coverage")

    if r["de"] > 2:
        flags.append("High leverage")

    if r["ocf_ratio"] < 0.8:
        flags.append("Weak cash flow")

    return flags
