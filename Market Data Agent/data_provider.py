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
    try:
        stock_list = ["MSFT", "AAPL", "TSLA"]
        for stock in stock_list:
            stock_url = f"{FINANCIAL_DATA_BASE_URL_STOCKS}?identifier={stock}&offset=0&key={FINANCIAL_DATA_API_KEY}"
            response = requests.get(stock_url)
            stock_data = response.json()

            if stock_data:
                latest_price = stock_data[0]
                print(
                    f"Latest stock price for {stock} on {latest_price['date']} "
                    f"is {latest_price['close']} (opened at {latest_price['open']}, "
                    f"volume: {latest_price['volume']})"
                )
            else:
                print(f"No data for {stock}.")
    except Exception as e:
        print("Something went wrong:", e)


def cryptodata():
    url = os.getenv("COIN_MARKET_CAP_CRYPTO_DATA_BASE_URL")

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "COIN_MARKET_CAP_CRYPTO_API_KEY",
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        response.raise_for_status()
        data = response.json()

        status = data["status"]["timestamp"]
        print(f"Timestamp: {status}")

        for coin in data["data"]:
            usd_data = coin["quote"]["USD"]
            usd_price = usd_data["price"]
            usd_market_cap = usd_data["market_cap"]
            btc_data = coin["quote"]["BTC"]
            btc_price = btc_data["price"]
            print(f"   USD: ${usd_price:.4f}, Market Cap: {usd_market_cap}")
            print(f"   BTC: {btc_price} BTC\n")

    except Exception as e:
        print(f"Something went wrong: {e}")


def fxdata():
    try:
        currency_list = ["EUR", "INR", "JPY"]
        for currency in currency_list:
            fx_url = f"{FOREX_RATE_BASE_URL}?api_key={FOREX_RATE_API_KEY}&base=USD&currencies={currency}"
            response = requests.get(fx_url)
            fxdata = response.json()

            if fxdata.get("success"):
                rate = fxdata["rates"].get(currency)
                print(
                    f"1 USD = {rate:.4f} {currency} "
                    f"(Base: {fxdata['base']}, Timestamp: {fxdata['timestamp']})"
                )
            else:
                print(f"No data returned for {currency}.")
    except Exception as e:
        print("Something went wrong:", e)
