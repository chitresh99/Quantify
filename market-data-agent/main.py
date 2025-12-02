from fastapi import FastAPI
from openai_service import summarization

app = FastAPI()


@app.get("/")
def introduction():
    return {"message": "Hello this is Dex , your market data agent"}


@app.get("/dex")
def dex():
    try:
        response = summarization()
        return {"analysis": response}
    except Exception as e:
        print("Something went wrong", {e})
