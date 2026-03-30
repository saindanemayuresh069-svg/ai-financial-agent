import pandas as pd

def get_sample_data(company):
    # Demo data (later we connect real API)
    data = {
        "Year": [2019, 2020, 2021, 2022, 2023],
        "Revenue": [100, 120, 150, 180, 220],
        "Net Profit": [20, 25, 35, 45, 60],
        "Debt": [50, 55, 60, 65, 70],
        "Equity": [80, 85, 90, 100, 120],
        "EBIT": [30, 40, 50, 65, 80],
        "OCF": [18, 22, 30, 40, 55]
    }

    return pd.DataFrame(data)
