import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None


def generate_report(ratios, score, flags):

    if not client:
        return "⚠️ API key not configured"

    prompt = f"""
    Financial Analysis:

    CAGR: {ratios['cagr']:.2f}
    ROE: {ratios['roe']:.2f}
    Score: {score}

    Risks: {flags}

    Give short investment recommendation.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
