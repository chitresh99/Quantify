import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools


load_dotenv()

google_api = os.getenv("GOOGLE_API_KEY")

agent = Agent(
    model=Gemini(id="gemini-2.0-flash", api_key=google_api),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions=[
        "Use tables to display data",
        "Only output the report, no other text",
    ],
    markdown=True,
)


def list_of_companies():
    return ["Century Aluminum Company", "Nucor Corporation"]


stocks = list_of_companies()
agent.print_response(
    stocks=stocks,
    message=f"Write a report on {', '.join(stocks)}",
    stream=True,
    show_full_reasoning=True,
)
