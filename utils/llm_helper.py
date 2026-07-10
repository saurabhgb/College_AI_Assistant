"""Safe, optional Gemini fallback constrained to supplied college data."""

import json

from config import LLM_FALLBACK_ENABLED, get_llm
from utils.constants import VALID_INTENTS
from utils.helpers import extract_response_text
from prompts.intent_prompt import INTENT_PROMPT


def answer_from_context(user_query: str, data: dict, system_prompt: str) -> str | None:
    """Answer only from supplied data, or return None if fallback is unavailable."""
    if not LLM_FALLBACK_ENABLED:
        return None

    prompt = f"""{system_prompt}

Use only the verified college data below. Do not invent dates, fees, contacts,
eligibility, or policies. If the data does not answer the question, say that the
student should check the official college notice or contact the college office.

Verified college data:
{json.dumps(data, indent=2)}

Student question: {user_query}
"""
    try:
        return extract_response_text(get_llm().invoke(prompt).content).strip()
    except Exception:
        return None


def classify_with_llm(user_query: str) -> str | None:
    """Classify unmatched questions only when optional Gemini fallback is enabled."""
    if not LLM_FALLBACK_ENABLED:
        return None

    prompt = f"""{INTENT_PROMPT}

Allowed labels: {", ".join(VALID_INTENTS)}.

Return only the label. Use unknown for unrelated questions.

Question: {user_query}
"""
    try:
        result = extract_response_text(get_llm().invoke(prompt).content).strip().lower()
        return result if result in VALID_INTENTS else "unknown"
    except Exception:
        return None
