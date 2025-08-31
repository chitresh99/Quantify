import os
import json
import asyncio
import aiofiles
from config import OPENROUTER_API_KEY
from data import get_data
from openai import OpenAI


async def summarization():

    raw_data = await get_data()

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )

    prompt = f"""
    You are a senior macroeconomic analyst. Analyze the following 2025 economic data and provide balanced investment insights.

    ECONOMIC DATA FOR 2025:
    {json.dumps(raw_data, indent=2)}

    Provide analysis with these sections:

    1. **ECONOMIC TREND ANALYSIS**
    - Key patterns in inflation, employment, and growth indicators
    - Month-over-month momentum and directional changes

    2. **FEDERAL RESERVE OUTLOOK**
    - Policy implications based on current data trends
    - Likely interest rate path given inflation and employment

    3. **ASSET CLASS IMPLICATIONS**
    - **Equities**: How macro trends affect different sectors
    - **Bonds**: Yield and duration considerations
    - **Commodities**: Gold and oil outlook based on data
    - **FX**: Dollar trends vs other currencies

    4. **INVESTMENT THEMES**
    - Current opportunities based on economic backdrop
    - Areas of caution given the data trends
    - Key data points to monitor for changes

    IMPORTANT GUIDELINES:
    - Base conclusions strictly on the provided data trends
    - Avoid overly bearish or bullish bias - be balanced
    - Consider that markets can perform differently than economic theory suggests
    - Focus on what the DATA actually shows, not worst-case scenarios
    - Acknowledge when data shows mixed signals rather than forcing a narrative
    - Do not use words like "Of course", "Oh", Keep it really formal and provide only the required information
    Format with clear headers and practical insights for investors.
    """

    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3.1:free",
        messages=[
            {
                "role": "system",
                "content": "You are a senior macroeconomic analyst and portfolio strategist specializing in cross-asset market analysis, Federal Reserve policy interpretation, and translating economic data into actionable investment strategies.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=2000,
    )
    response = completion.choices[0].message.content
    return response
