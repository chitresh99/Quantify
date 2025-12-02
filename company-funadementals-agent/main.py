from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import json
from config import OPENROUTER_API_KEY

app = FastAPI()


@app.get("/")
def introduction():
    return {"message": "Hello this is Darwyn , your market data agent"}


class CompanyData(BaseModel):
    content: str


@app.post("/darwyn")
def darwyn(company_data: CompanyData):
    try:
        company_information = company_data.content

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=OPENROUTER_API_KEY,
        )

        system_prompt = f"""
        You are an AI agent for financial research focused on parsing company earnings call transcripts and related filings.

        This is the data:
        {company_information}

        Your goals:

        Extract structured financial insights from transcripts.

        Focus on:

        Guidance → forward-looking revenue, EPS, margin outlook, and any changes vs last quarter.

        Revenue & Margin Drivers → which business units are growing/declining, gross vs operating margin trends.

        Cost Structure → Opex, R&D, headcount changes, restructuring, efficiency measures.

        Demand Commentary → customer spending trends, geographic regions (US, Europe, Asia), macroeconomic impacts.

        Competitive Positioning → competitor mentions, new product launches, moat defenses.

        Risk Factors → FX headwinds, supply chain, regulation, geopolitical issues.

        Tone & Sentiment → overall sentiment (positive, negative, neutral, mixed) and notable language shifts.

        Output requirements:

        Always return results in normal text **NO JSON NO MARKDOWN***.

        Use concise summaries (1–3 sentences per field).

        Keep sentiment labels as: "positive", "negative", "neutral", or "mixed".

        Do not add explanations outside of the data.
        """

        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3.1:free",
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior equity research analyst and corporate fundamentals specialist, focused on parsing earnings transcripts, SEC filings, and management commentary to extract structured insights, assess financial health, and identify investment-relevant risks and opportunities.",
                },
                {"role": "user", "content": system_prompt},
            ],
            temperature=0.7,
            max_tokens=2000,
        )
        response = completion.choices[0].message.content
        return {"message": "Summary created succefully", "summary": response}
    except Exception as e:
        return {"error": f"Something went wrong: {str(e)}"}
