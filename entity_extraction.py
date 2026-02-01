from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import StrOutputParser
from model import get_llm
from query_constructor import ENTITY_PROMPT

class Entities(BaseModel):
    names: List[str] = Field(...)


def extract_entities(question: str) -> List[str]:
    llm = get_llm()
    chain = ENTITY_PROMPT | llm.with_structured_output(Entities)
    return chain.invoke({"question": question}).names