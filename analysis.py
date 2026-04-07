def calculate_ratios(df):

    if df.empty:
        return {"cagr": 0, "roe": 0}

    first = df.iloc[0]["Revenue"]
    last = df.iloc[-1]["Revenue"]

    cagr = ((last / first) ** (1/len(df))) - 1 if first else 0
    roe = (df.iloc[-1]["Net Profit"] / df.iloc[-1]["Equity"]) if df.iloc[-1]["Equity"] else 0

    return {"cagr": cagr * 100, "roe": roe * 100}


def calculate_score(ratios):
    score = 0
    if ratios["cagr"] > 10:
        score += 2
    if ratios["roe"] > 15:
        score += 2
    return score


def detect_red_flags(df):
    return []
