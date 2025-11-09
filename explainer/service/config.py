from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model

def get_chat_model(model_name: str = "openai:gpt-4.1-mini"):
    """Return a langchain chat model"""
    load_dotenv()
    api_key=os.getenv("OPENAI_API_KEY")

    if not api_key:
        return Exception("Could not kind the open ai key")
    else:
        return init_chat_model(model=model_name,api_key=api_key)
    