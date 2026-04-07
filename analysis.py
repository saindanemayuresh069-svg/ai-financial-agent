def calculate_ratios(df):

    first = df.iloc[0]
    last = df.iloc[-1]

    cagr = ((last["Revenue"] / first["Revenue"]) ** (1/3)) - 1 if first["Revenue"] else 0
    roe = last["Net Profit"] / last["Equity"] if last["Equity"] else 0

    return {"cagr": cagr, "roe": roe}


def calculate_score(ratios):
    score = 0

    if ratios["cagr"] > 0.15:
        score += 2
    if ratios["roe"] > 0.15:
        score += 2

    return score


def detect_red_flags(ratios):
    flags = []

    if ratios["roe"] < 0.1:
        flags.append("Low profitability")

    return flags
