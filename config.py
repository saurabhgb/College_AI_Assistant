"""Optional Gemini configuration for fallback answers and intent detection."""

import os

from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "gemini-2.5-flash"
LLM_FALLBACK_ENABLED = os.getenv("ENABLE_LLM_FALLBACK", "false").lower() == "true"


def get_llm():
    """Create the Gemini client only when the optional fallback is required."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY is required when ENABLE_LLM_FALLBACK=true.")

    from langchain_google_genai import ChatGoogleGenerativeAI

    return ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        temperature=0.1,
        google_api_key=api_key,
    )
