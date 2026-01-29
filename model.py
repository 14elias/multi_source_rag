from langchain_openai import ChatOpenAI
from settings import settings

def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        openai_api_key=settings.OPENAI_API_KEY,
        base_url=settings.OPENAI_API_BASE_URL
    )
