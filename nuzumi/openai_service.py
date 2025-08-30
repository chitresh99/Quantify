import asyncio
from openai import OpenAI
from config import OPENROUTER_API_KEY
import os
from news_service import newsandsentiment
import httpx
import json


async def summarization():
    raw_data = await newsandsentiment()
    print(raw_data)

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )

    prompt = f"""
    You are a financial news analyst. I have news data with sentiment scores that need to be summarized and analyzed.

    Here's the sentiment scoring system:
    {raw_data['sentiment_score_definition']}

    Relevance scoring: {raw_data['relevance_score_definition']}

    Please analyze the following {raw_data['items']} news items and provide:

    1. **Overall Market Sentiment Summary**: Brief overview of the general market mood
    2. **Key Headlines Analysis**: Summarize the most important/relevant stories
    3. **Sentiment Distribution**: Break down how many articles fall into each sentiment category
    4. **Top Tickers Mentioned**: List the most mentioned stocks and their sentiment
    5. **Market Implications**: What this news suggests for market direction

    News Data:
    {json.dumps(raw_data['feed'], indent=2)}

    Please provide a clear, concise analysis that would be useful for investment decision-making.
    Format your response with clear sections and bullet points where appropriate.
    """

    completion = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3.1:free",
        messages=[
            {
                "role": "system",
                "content": "You are an expert financial analyst specializing in news sentiment analysis and market implications.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=2000,
    )
    print(completion.choices[0].message.content)
