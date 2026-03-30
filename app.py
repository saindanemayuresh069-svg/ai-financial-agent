import streamlit as st
from analysis import calculate_ratios, calculate_score, detect_red_flags
from ai_report import generate_report
from data_fetch import get_sample_data

st.set_page_config(page_title="AI Financial Analyst", layout="wide")

st.title("📊 AI Financial Analyst (Pro Version)")

company = st.text_input("Enter Company Name (e.g., HDFC Bank)")

if company:
    df = get_sample_data(company)

    st.subheader("📊 Financial Data")
    st.dataframe(df)

    # Charts
    st.subheader("📈 Growth Trends")
    st.line_chart(df.set_index("Year")[["Revenue", "Net Profit"]])

    try:
        ratios = calculate_ratios(df)
        score = calculate_score(ratios)
        flags = detect_red_flags(ratios)

        col1, col2, col3 = st.columns(3)

        col1.metric("📈 CAGR", f"{ratios['cagr']:.2%}")
        col2.metric("💰 ROE", f"{ratios['roe']:.2%}")
        col3.metric("⭐ Score", score)

        st.subheader("⚠️ Risk Flags")
        st.write(flags if flags else "No major risks detected")

        if st.button("Generate AI Report"):
            report = generate_report(ratios, score, flags)

            st.subheader("🤖 AI Investment Report")
            st.write(report)

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("Enter a company name to begin analysis")
