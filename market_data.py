import yfinance as yf

def get_market_data(company):

    ticker = company.upper().replace(" ", "") + ".NS"
    stock = yf.Ticker(ticker)

    try:
        hist = stock.history(period="1d")
        price = hist["Close"].iloc[-1]

        info = stock.info
        market_cap = info.get("marketCap", 0)

        if price == 0:
            raise Exception

    except:
        ticker = company.upper()
        stock = yf.Ticker(ticker)

        hist = stock.history(period="1d")
        price = hist["Close"].iloc[-1]

        info = stock.info
        market_cap = info.get("marketCap", 0)

    return {
        "price": round(price, 2),
        "market_cap": market_cap
    }
