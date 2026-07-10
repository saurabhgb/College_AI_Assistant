"""Prepare the final response returned to the student."""


def response_agent(agent_response: str, source_note: str = "") -> str:
    """Return the specialist response together with its official source guidance."""
    answer = agent_response.strip() if agent_response else "Sorry, I could not find an answer to that question."
    return f"{answer}\n\nSource: {source_note}" if source_note else answer
