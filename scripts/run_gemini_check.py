"""Check the optional Gemini connection when fallback is enabled."""

from config import LLM_FALLBACK_ENABLED, get_llm


if not LLM_FALLBACK_ENABLED:
    print("Gemini fallback is disabled. Set ENABLE_LLM_FALLBACK=true in .env to test it.")
else:
    print(get_llm().invoke("Say hello in one sentence.").content)
