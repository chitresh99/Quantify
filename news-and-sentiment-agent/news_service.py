import asyncio
from fastapi import FastAPI
from dotenv import load_dotenv
import requests
import os
import httpx
import json
from config import ALPHA_NEWS_BASE_URL, ALPHA_NEWS_API

load_dotenv()

ALPHA_NEWS = f"{ALPHA_NEWS_BASE_URL}&apikey={ALPHA_NEWS_API}"

app = FastAPI()


async def newsandsentiment():
    async with httpx.AsyncClient() as client:
        response = await client.get(ALPHA_NEWS)
        response.raise_for_status()
        return response.json()
