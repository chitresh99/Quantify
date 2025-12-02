from dotenv import load_dotenv
import os

load_dotenv()

ALPHA_NEWS_API = os.getenv("ALPHA_NEWS_API")
ALPHA_NEWS_BASE_URL = os.getenv("ALPHA_NEWS_BASE_URL")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
