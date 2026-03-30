def calculate_ratios(df):
    if df is None or df.empty or len(df) < 2:
        raise ValueError("Insufficient data")

    latest = df.iloc[-1]
    first = df.iloc[0]

    revenue = latest["Revenue"]
    first_revenue = first["Revenue"]

    profit = latest["Net Profit"]
    equity = latest.get("Equity", 1)
    debt = latest.get("Debt", 0)
    ebit = latest.get("EBIT", 0)
    interest = latest.get("Interest", 0)
    ocf = latest.get("OCF", 0)

    revenue_cagr = (revenue / first_revenue)**(1/4) - 1
    roe = profit / equity if equity else 0
    debt_equity = debt / equity if equity else 0
    icr = ebit / interest if interest else 0
    ocf_ratio = ocf / profit if profit else 0

    return {
        "cagr": revenue_cagr,
        "roe": roe,
        "de": debt_equity,
        "icr": icr,
        "ocf_ratio": ocf_ratio
    }


def calculate_score(r):
    score = 0

    score += 5 if r["cagr"] > 0.15 else 3
    score += 5 if r["roe"] > 0.2 else 3
    score += 5 if r["de"] < 1 else 2
    score += 5 if r["ocf_ratio"] > 1 else 2

    return round(score / 4, 2)


def detect_red_flags(r):
    flags = []

    if r["icr"] < 2:
        flags.append("Low interest coverage")

    if r["de"] > 2:
        flags.append("High leverage")

    if r["ocf_ratio"] < 0.8:
        flags.append("Weak cash flow")

    return flags
