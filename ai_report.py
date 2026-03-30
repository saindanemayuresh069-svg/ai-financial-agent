import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_report(ratios, score, flags):
    prompt = f"""
You are a buy-side equity analyst.

Financial Summary:
- Revenue CAGR: {ratios['cagr']:.2f}
- ROE: {ratios['roe']:.2f}
- Debt/Equity: {ratios['de']:.2f}
- Interest Coverage: {ratios['icr']:.2f}
- Cash Flow Ratio: {ratios['ocf_ratio']:.2f}

Score: {score}/5
Red Flags: {flags}

Give:
1. Summary
2. Strengths
3. Risks
4. Final Recommendation (Buy/Hold/Sell)
"""

    response = client.chat.completions.create(
        model="gpt-5.3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
