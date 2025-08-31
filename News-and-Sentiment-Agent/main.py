from fastapi import FastAPI
import asyncio
from openai_service import summarization
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello this is nuzumi your news and sentiment ai agent"}


@app.get("/nuzumi")
async def nuzumi():
    try:
        response = await summarization()
        return {"analysis": response}
    except Exception:
        print("API key exhausted")
