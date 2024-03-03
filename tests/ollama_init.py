from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
key = os.getenv("OllAMA_BASE_URL")
# print(key)
