def calculate_dcf(df):

    if "OCF" not in df.columns:
        return 0

    latest_ocf = df.iloc[-1]["OCF"]

    if latest_ocf <= 0:
        return 0

    growth_rate = 0.12
    discount_rate = 0.10
    terminal_growth = 0.04

    cash_flows = []

    for i in range(1, 6):
        cf = latest_ocf * ((1 + growth_rate) ** i)
        discounted = cf / ((1 + discount_rate) ** i)
        cash_flows.append(discounted)

    terminal_value = (cash_flows[-1] * (1 + terminal_growth)) / (discount_rate - terminal_growth)
    terminal_discounted = terminal_value / ((1 + discount_rate) ** 5)

    return round(sum(cash_flows) + terminal_discounted, 2)
