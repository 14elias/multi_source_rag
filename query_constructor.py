def build_llm_prompt(query: str, context: str) -> str:
    """
    Constructs a prompt that strictly constrains the LLM to answer
    ONLY from the given context.

    Rules enforced:
    - If the answer is not in the context, respond with:
      "I do not have enough info."
    - Do NOT use external knowledge.
    """

    context = context.strip()

    if not context:
        return (
            "You are a strict question-answering assistant.\n"
            "There is NO context provided.\n\n"
            "Instruction:\n"
            "If there is not enough information to answer the question, "
            "respond exactly with:\n"
            "\"I do not have enough info.\"\n\n"
            f"Question:\n{query}"
        )

    return f"""
You are a strict question-answering assistant.

You MUST follow these rules:
1. Answer ONLY using the information provided in the context below.
2. Do NOT use prior knowledge, assumptions, or external facts.
3. If the context does not contain enough information to answer the question,
   respond EXACTLY with:
   "I do not have enough info."
4. Do NOT add explanations, guesses, or extra details outside the context.

Context:
{context}

Question:
{query}

Answer:
""".strip()


from langchain_core.prompts import ChatPromptTemplate

ENTITY_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", "You extract person and organization entities."),
        ("human", "Extract entities from: {question}")
    ]
)
