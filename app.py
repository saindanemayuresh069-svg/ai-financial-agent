import streamlit as st
from analysis import calculate_ratios, calculate_score, detect_red_flags
from valuation import calculate_dcf
from ai_report import generate_report
from data_fetch import get_financial_data
from market_data import get_market_data

st.set_page_config(page_title="AI Financial Analyst", layout="wide")

st.title("📊 AI Financial Analyst PRO")

# 🔹 Input
company = st.text_input("Enter Company Name (e.g., HDFC Bank, SBI, Apple)")

if company:
    try:
        # Normalize input
        company = company.lower().strip()

        # 📊 Financial Data
        df = get_financial_data(company)

        if df is None or df.empty:
            st.error("No financial data found for this company")
            st.stop()

        st.subheader("📊 Financial Data")
        st.dataframe(df)

        # 📈 Charts
        st.subheader("📈 Growth Trends")
        available_cols = [col for col in ["Revenue", "Net Profit"] if col in df.columns]
        if available_cols:
            st.line_chart(df.set_index("Year")[available_cols])

        # 📊 Ratios
        ratios = calculate_ratios(df)
        score = calculate_score(ratios)
        flags = detect_red_flags(ratios)

        col1, col2, col3 = st.columns(3)
        col1.metric("📈 CAGR", f"{ratios['cagr']:.2%}")
        col2.metric("💰 ROE", f"{ratios['roe']:.2%}")
        col3.metric("⭐ Score", score)

        # 💰 DCF
        dcf_value = calculate_dcf(df)

        st.subheader("💰 Intrinsic Value (DCF)")
        st.metric("Estimated Value", f"{dcf_value:,.0f}")

        # 📈 Market Data
        try:
            market = get_market_data(company)

            # 🔍 DEBUG (REMOVE AFTER WORKING)
            st.write("DEBUG MARKET:", market)

            price = market.get("price", 0)
            market_cap = market.get("market_cap", 0)

        except Exception as e:
            st.warning(f"Market data error: {e}")
            price = 0
            market_cap = 0

        # 📊 Market Display
        st.subheader("📊 Market Data")

        c1, c2, c3 = st.columns(3)

        c1.metric("Stock Price", f"{price:,.2f}")
        c2.metric("Market Cap", f"{market_cap:,.0f}")

        # 📊 Upside %
        if market_cap > 0:
            upside = (dcf_value - market_cap) / market_cap * 100
        else:
            upside = 0

        c3.metric("Upside %", f"{upside:.2f}%")

        # 📌 Verdict
        if upside > 20:
            verdict = "🟢 BUY"
        elif upside > 0:
            verdict = "🟡 HOLD"
        else:
            verdict = "🔴 SELL"

        st.subheader("📌 Investment Verdict")
        st.write(verdict)

        # ⚠️ Risk Flags
        st.subheader("⚠️ Risk Flags")
        st.write(flags if flags else "No major risks detected")

        # 🤖 AI Report
        if st.button("Generate AI Report"):
            report = generate_report(ratios, score, flags)
            st.subheader("🤖 AI Investment Report")
            st.write(report)

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("Enter a company name to begin analysis")
