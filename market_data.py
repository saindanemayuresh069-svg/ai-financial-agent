import yfinance as yf


def get_market_data(company):

    ticker = company.upper().replace(" ", "") + ".NS"

    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")

        if hist.empty:
            raise Exception

        price = hist["Close"].iloc[-1]
        market_cap = stock.info.get("marketCap", 0)

    except:
        ticker = company.upper()
        stock = yf.Ticker(ticker)

        hist = stock.history(period="1d")

        if hist.empty:
            return {"price": 0, "market_cap": 0}

        price = hist["Close"].iloc[-1]
        market_cap = stock.info.get("marketCap", 0)

    return {
        "price": float(price),
        "market_cap": float(market_cap)
    }
