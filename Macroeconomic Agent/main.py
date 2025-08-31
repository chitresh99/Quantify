from fastapi import FastAPI
import asyncio
from openai_service import summarization
import json


##############################################
# IMPORTANT DISCLAIMER:
#
# This economic data was retrieved using AI tools
# and stored in JSON format. Please verify all data
# from official sources before making investment decisions.
#
# AI-generated analysis can contain errors, biases,
# or outdated information. This is for informational
# purposes only and not financial advice.
#
# The creators of Quantify are not responsible
# for any financial losses resulting from use of
# this data or analysis.
#
# Always consult official sources:
# - Federal Reserve Economic Data (FRED)
# - Bureau of Labor Statistics
# - Bureau of Economic Analysis
# - Your financial advisor
##############################################

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello this is Keynes your macro economic agent"}


@app.get("/keynes")
async def keynes():
    try:
        response = await summarization()
        return {"analysis": response}
    except Exception:
        print("Something went wrong")
