import pandas as pd

def calculate_ratios(df):
    latest = df.iloc[-1]
    first = df.iloc[0]

    revenue_cagr = (latest['Revenue'] / first['Revenue'])**(1/4) - 1
    roe = latest['Net Profit'] / latest['Equity']
    debt_equity = latest['Debt'] / latest['Equity']
    interest_coverage = latest['EBIT'] / latest['Interest']
    ocf_ratio = latest['OCF'] / latest['Net Profit']

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

    return round(score,2)

def detect_red_flags(r):
    flags = []
    if r["icr"] < 2:
        flags.append("Low interest coverage")
    if r["de"] > 2:
        flags.append("High leverage")
    if r["ocf_ratio"] < 0.8:
        flags.append("Weak cash flow")
    return flags
