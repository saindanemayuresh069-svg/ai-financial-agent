import streamlit as st
import pandas as pd
from analysis import calculate_ratios, calculate_score, detect_red_flags
from ai_report import generate_report

st.title("📊 AI Financial Analyst")

uploaded_file = st.file_uploader("Upload Excel File")

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.write("### Raw Data")
    st.dataframe(df)

    st.write("### Columns in your file:")
st.write(list(df.columns))

try:
    ratios = calculate_ratios(df)
    score = calculate_score(ratios)
    flags = detect_red_flags(ratios)

    st.write("### 📈 Ratios", ratios)
    st.write("### ⭐ Score:", score)
    st.write("### ⚠️ Red Flags:", flags)

    if st.button("Generate AI Report"):
        report = generate_report(ratios, score, flags)
        st.write("### 🤖 AI Report")
        st.write(report)

except Exception as e:
    st.error(f"Error: {e}")
    score = calculate_score(ratios)
    flags = detect_red_flags(ratios)

    st.write("### 📈 Ratios", ratios)
    st.write("### ⭐ Score:", score)
    st.write("### ⚠️ Red Flags:", flags)

    if st.button("Generate AI Report"):
        report = generate_report(ratios, score, flags)
        st.write("### 🤖 AI Report")
        st.write(report)  
