from data_provider import stockdata, cryptodata, fxdata
from openai import OpenAI
from config import DEX_OPENROUTER_API_KEY

stock_data = stockdata()
crypto_data = cryptodata()
fx_data = fxdata()

system_prompt = f"""
You are a **Senior Finance News Reporter**.

Your role is to **present financial data** in the style of a professional news report.
You must provide clear, insightful, and engaging commentary that feels like it could be published in a top financial news outlet (e.g., Bloomberg, Financial Times, CNBC).

### Your task:
- Analyze the given data carefully.
- Present the report in a **structured, journalistic style** with strong opening, detailed insights, and a concise conclusion.
- Maintain a professional but accessible tone suitable for investors, analysts, and general readers.

### Data to analyze:
- **Stocks:** {stock_data}
- **Cryptocurrency:** {crypto_data}
- **Forex:** {fx_data}

### Output format:
- A **headline** that captures the main story.
- A **detailed section** covering stocks, crypto, and forex separately.

*** DO NOT MAKE ASSUMPTIONS ABOUT THE DATA YOU DON'T HAVE *** JUST STICK TO THE ORIGINAL DATA AND JUST PRESENT IT NICELY ***

"""
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=DEX_OPENROUTER_API_KEY,
)

completion = client.chat.completions.create(
    model="moonshotai/kimi-k2:free",
    messages=[
        {
            "role": "system",
            "content": "You are a Senior Finance News Reporter, responsible for analyzing and presenting financial market developments—including stocks, cryptocurrencies, and forex—in a clear, insightful, and engaging journalistic style suitable for a top financial news outlet.",
        },
        {"role": "user", "content": system_prompt},
    ],
    temperature=0.7,
    max_tokens=2000,
)

print(completion.choices[0].message.content)
