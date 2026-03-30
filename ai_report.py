import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_report(ratios, score, flags):

    prompt = f"""
You are a professional equity research analyst.

Company Analysis:

Growth (CAGR): {ratios['cagr']:.2f}
ROE: {ratios['roe']:.2f}
Debt/Equity: {ratios['de']:.2f}

Score: {score}/5

Risks: {flags}

Give:
1. Investment Summary
2. Strengths
3. Risks
4. Final Verdict (Buy/Hold/Sell)
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
