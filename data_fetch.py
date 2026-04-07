import pandas as pd

def get_financial_data(company):

    data = {
        "Year": [2022, 2023, 2024, 2025],
        "Revenue": [1000, 1200, 1800, 2300],
        "Net Profit": [400, 500, 620, 700],
        "EBIT": [500, 600, 800, 900],
        "Debt": [200, 300, 350, 400],
        "Equity": [800, 900, 1100, 1300],
        "OCF": [300, 400, 500, 600]
    }

    return pd.DataFrame(data)
