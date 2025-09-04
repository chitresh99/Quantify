import os
import json
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

from config import (
    FINANCIAL_DATA_BASE_URL_STOCKS,
    FINANCIAL_DATA_API_KEY,
    COIN_MARKET_CAP_CRYPTO_DATA_BASE_URL,
    COIN_MARKET_CAP_CRYPTO_API_KEY,
    FOREX_RATE_API_KEY,
    FOREX_RATE_BASE_URL,
)


def stockdata():
    results = []
    try:
        stock_list = ["MSFT", "AAPL", "TSLA"]
        for stock in stock_list:
            stock_url = f"{FINANCIAL_DATA_BASE_URL_STOCKS}?identifier={stock}&offset=0&key={FINANCIAL_DATA_API_KEY}"
            response = requests.get(stock_url)
            response.raise_for_status()
            stock_data = response.json()

            if stock_data:
                latest_price = stock_data[0]
                results.append(
                    {
                        "symbol": stock,
                        "date": latest_price["date"],
                        "close": latest_price["close"],
                        "open": latest_price["open"],
                        "volume": latest_price["volume"],
                    }
                )
            else:
                results.append({"symbol": stock, "error": "No data"})
        return results
    except Exception as e:
        return {"error": str(e)}


def cryptodata():
    url = COIN_MARKET_CAP_CRYPTO_DATA_BASE_URL
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": COIN_MARKET_CAP_CRYPTO_API_KEY,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        response.raise_for_status()
        data = response.json()

        results = {
            "timestamp": data["status"]["timestamp"],
            "coins": [],
        }

        for coin in data["data"]:
            usd_data = coin["quote"]["USD"]
            btc_data = coin["quote"]["BTC"]
            results["coins"].append(
                {
                    "usd_price": usd_data["price"],
                    "usd_market_cap": usd_data["market_cap"],
                    "btc_price": btc_data["price"],
                }
            )

        return results
    except Exception as e:
        return {"error": str(e)}


def fxdata():
    results = []
    try:
        currency_list = ["EUR", "INR", "JPY"]
        for currency in currency_list:
            fx_url = f"{FOREX_RATE_BASE_URL}?api_key={FOREX_RATE_API_KEY}&base=USD&currencies={currency}"
            response = requests.get(fx_url)
            response.raise_for_status()
            fxdata = response.json()

            if fxdata.get("success"):
                rate = fxdata["rates"].get(currency)
                results.append(
                    {
                        "base": fxdata["base"],
                        "currency": currency,
                        "rate": rate,
                        "timestamp": fxdata["timestamp"],
                    }
                )
            else:
                results.append({"currency": currency, "error": "No data"})
        return results
    except Exception as e:
        return {"error": str(e)}
