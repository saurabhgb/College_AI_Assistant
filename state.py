from typing import NotRequired, TypedDict


class CollegeAssistantState(TypedDict):
    """
    Shared state passed between all LangGraph nodes.
    """

    user_query: str
    intent: NotRequired[str]
    agent_response: NotRequired[str]
    source_note: NotRequired[str]
    final_response: NotRequired[str]
