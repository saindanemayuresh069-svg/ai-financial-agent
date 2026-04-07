def generate_report(ratios, score, flags):

    return f"""
    Company Analysis Summary:

    CAGR: {ratios['cagr']:.2%}
    ROE: {ratios['roe']:.2%}
    Score: {score}

    Risks: {', '.join(flags) if flags else 'None'}

    Overall View:
    This company shows moderate financial performance based on available data.
    """
