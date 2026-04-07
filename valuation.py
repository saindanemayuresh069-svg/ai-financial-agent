def calculate_dcf(df):

    last_cashflow = df.iloc[-1]["OCF"]
    growth_rate = 0.10
    discount_rate = 0.12

    value = 0

    for i in range(1, 6):
        future_cf = last_cashflow * ((1 + growth_rate) ** i)
        value += future_cf / ((1 + discount_rate) ** i)

    return value
