import streamlit as st
from data_fetch import get_financial_data
from market_data import get_market_data
from analysis import calculate_ratios, calculate_score
from valuation import calculate_dcf

st.set_page_config(page_title="AI Financial Analyst PRO", layout="wide")

st.title("📊 AI Financial Analyst PRO")

company = st.text_input("Enter Company Name (e.g., HDFC Bank, SBI, Apple)")

if company:

    try:
        df = get_financial_data(company)
        market = get_market_data(company)

    except Exception as e:
        st.error(f"Error: {e}")
        df = None
        market = {"price": 0, "market_cap": 0}

    if df is not None and not df.empty:

        st.subheader("📊 Financial Data")
        st.dataframe(df)

        ratios = calculate_ratios(df)
        score = calculate_score(ratios)
        intrinsic = calculate_dcf(df)

        st.subheader("📈 Metrics")
        col1, col2, col3 = st.columns(3)

        col1.metric("CAGR", f"{ratios['cagr']:.2f}%")
        col2.metric("ROE", f"{ratios['roe']:.2f}%")
        col3.metric("Score", score)

        st.subheader("💰 Intrinsic Value")
        st.write(f"{intrinsic:,.0f}")

        st.subheader("📊 Market Data")

        col1, col2, col3 = st.columns(3)

        price = market["price"]
        upside = ((intrinsic - price) / price * 100) if price else 0

        col1.metric("Stock Price", f"{price}")
        col2.metric("Market Cap", f"{market['market_cap']}")
        col3.metric("Upside %", f"{upside:.2f}%")

    else:
        st.warning("No data found")
