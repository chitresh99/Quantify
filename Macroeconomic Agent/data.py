from fastapi import FastAPI
import os
import json
import asyncio
import aiofiles

app = FastAPI()


async def get_data():
    async with aiofiles.open("marco_economic.json", "r") as f:
        contents = await f.read()
        data = json.loads(contents)
        return data
