import os
from crewai import Agent

# from stock_analysis.tools.browser_tools import BrowserTools, DuckduckGoSearch

from stock_analysis.tools.calculator_tools import CalculatorTools
from stock_analysis.tools.search_tools import SearchTools
from stock_analysis.tools.sec_tools import SECTools
from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_community.llms import Ollama
from langchain_community.tools import DuckDuckGoSearchRun

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class StockAnalysisAgents:
    def financial_analyst(self):
        return Agent(
            role="The Best Financial Analyst",
            goal="""Impress all customers with your financial data 
      and market trends analysis""",
            backstory="""The most seasoned financial analyst with 
      lots of expertise in stock market analysis and investment
      strategies that is working for a super important customer.""",
            verbose=True,
            tools=[
                DuckDuckGoSearchRun(),
                SearchTools.search_internet,
                CalculatorTools.calculate,
                SECTools.search_10q,
                SECTools.search_10k,
            ],
            llm=Ollama(
                model=os.getenv("OLLAMA_BASE_MODEL"),
                base_url=os.getenv("OllAMA_BASE_URL"),
            ),
        )

    def research_analyst(self):
        return Agent(
            role="Staff Research Analyst",
            goal="""Being the best at gather, interpret data and amaze
      your customer with it""",
            backstory="""Known as the BEST research analyst, you're
      skilled in sifting through news, company announcements, 
      and market sentiments. Now you're working on a super 
      important customer""",
            verbose=True,
            tools=[
                DuckDuckGoSearchRun(),
                SearchTools.search_internet,
                SearchTools.search_news,
                YahooFinanceNewsTool(),
                SECTools.search_10q,
                SECTools.search_10k,
            ],
            llm=Ollama(
                model=os.getenv("OLLAMA_BASE_MODEL"),
                base_url=os.getenv("OllAMA_BASE_URL"),
            ),
        )

    def investment_advisor(self):
        return Agent(
            role="Private Investment Advisor",
            goal="""Impress your customers with full analyses over stocks
      and completer investment recommendations""",
            backstory="""You're the most experienced investment advisor
      and you combine various analytical insights to formulate
      strategic investment advice. You are now working for
      a super important customer you need to impress.""",
            verbose=True,
            tools=[
                DuckDuckGoSearchRun(),
                SearchTools.search_internet,
                SearchTools.search_news,
                CalculatorTools.calculate,
                YahooFinanceNewsTool(),
            ],
            llm=Ollama(
                model=os.getenv("OLLAMA_BASE_MODEL"),
                base_url=os.getenv("OllAMA_BASE_URL"),
            ),
        )
