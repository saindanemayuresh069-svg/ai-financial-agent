def calculate_ratios(df):

    latest = df.iloc[-1]
    first = df.iloc[0]

    revenue = latest["Revenue"]
    first_revenue = first["Revenue"]
    profit = latest["Net Profit"]
    equity = latest["Equity"]
    debt = latest["Debt"]
    ocf = latest["OCF"]

    cagr = (revenue / first_revenue)**(1/4) - 1 if first_revenue else 0
    roe = profit / equity if equity else 0
    de = debt / equity if equity else 0
    ocf_ratio = ocf / profit if profit else 0

    return {
        "cagr": cagr,
        "roe": roe,
        "de": de,
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
    if r["de"] > 2:
        flags.append("High leverage")
    if r["ocf_ratio"] < 0.8:
        flags.append("Weak cash flow")
    return flags
