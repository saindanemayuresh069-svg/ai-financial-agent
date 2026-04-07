def calculate_dcf(df):

    if df.empty:
        return 0

    last_ocf = df.iloc[-1]["OCF"]

    growth = 0.1
    discount = 0.12

    value = 0

    for i in range(1, 6):
        value += (last_ocf * (1 + growth) ** i) / ((1 + discount) ** i)

    return value
