from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def introduction():
    return {"message": "Hello this is Dex , your market data agent"}


@app.get("/dex")
async def dex():
    pass
