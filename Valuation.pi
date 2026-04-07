def calculate_dcf(df, growth_rate=0.12, discount_rate=0.10, terminal_growth=0.04):

    latest_ocf = df.iloc[-1]["OCF"]

    cash_flows = []

    # 5-year projection
    for i in range(1, 6):
        cf = latest_ocf * ((1 + growth_rate) ** i)
        discounted_cf = cf / ((1 + discount_rate) ** i)
        cash_flows.append(discounted_cf)

    # Terminal value
    terminal_value = (cash_flows[-1] * (1 + terminal_growth)) / (discount_rate - terminal_growth)
    terminal_discounted = terminal_value / ((1 + discount_rate) ** 5)

    intrinsic_value = sum(cash_flows) + terminal_discounted

    return round(intrinsic_value, 2)
