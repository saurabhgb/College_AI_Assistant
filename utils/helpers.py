"""Shared helper functions for the College AI Assistant."""


def extract_response_text(content) -> str:
    """Return readable text from a LangChain model response content value."""
    if isinstance(content, list):
        first_item = content[0] if content else ""
        if isinstance(first_item, dict):
            return str(first_item.get("text", ""))
        return str(first_item)
    return str(content)
