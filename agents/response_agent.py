"""Prepare the final response returned to the student."""


def response_agent(agent_response: str, source_note: str = "") -> str:
    """Return the specialist response together with its official source guidance."""
    answer = agent_response.strip() if agent_response else "Sorry, I could not find an answer to that question."
    if not source_note:
        return answer

    return f"**Answer**\n{answer}\n\n**Source note:**\n{source_note}"
