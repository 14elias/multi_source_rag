
from model import get_llm
from query_constructor import build_llm_prompt

def answer_question(context: str, question: str) -> str:
    llm = get_llm()
    prompt = build_llm_prompt(context=context, query=question)
    return llm.invoke(prompt).content
