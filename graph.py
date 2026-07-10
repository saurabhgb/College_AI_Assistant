"""LangGraph workflow for the College AI Assistant."""

from langgraph.graph import END, START, StateGraph

from agents.admission_agent import admission_agent
from agents.exam_agent import exam_agent
from agents.fees_agent import fees_agent
from agents.intent_classifier import classify_intent
from agents.response_agent import response_agent
from agents.scholarship_agent import scholarship_agent
from state import CollegeAssistantState
from utils.constants import OFFICIAL_SOURCES


def classify_node(state: CollegeAssistantState) -> dict:
    return {"intent": classify_intent(state["user_query"])}


def admission_node(state: CollegeAssistantState) -> dict:
    return {"agent_response": admission_agent(state["user_query"]), "source_note": OFFICIAL_SOURCES["admission"]}


def exam_node(state: CollegeAssistantState) -> dict:
    return {"agent_response": exam_agent(state["user_query"]), "source_note": OFFICIAL_SOURCES["exam"]}


def fees_node(state: CollegeAssistantState) -> dict:
    return {"agent_response": fees_agent(state["user_query"]), "source_note": OFFICIAL_SOURCES["fees"]}


def scholarship_node(state: CollegeAssistantState) -> dict:
    return {"agent_response": scholarship_agent(state["user_query"]), "source_note": OFFICIAL_SOURCES["scholarship"]}


def unknown_node(_: CollegeAssistantState) -> dict:
    return {"agent_response": "I can help with admission, exams, fees, and scholarships. Please ask a question in one of these areas."}


def response_node(state: CollegeAssistantState) -> dict:
    return {"final_response": response_agent(state.get("agent_response", ""), state.get("source_note", ""))}


def route_intent(state: CollegeAssistantState) -> str:
    return state.get("intent", "unknown")


workflow = StateGraph(CollegeAssistantState)
workflow.add_node("intent_classifier", classify_node)
workflow.add_node("admission_agent", admission_node)
workflow.add_node("exam_agent", exam_node)
workflow.add_node("fees_agent", fees_node)
workflow.add_node("scholarship_agent", scholarship_node)
workflow.add_node("unknown", unknown_node)
workflow.add_node("response_agent", response_node)

workflow.add_edge(START, "intent_classifier")
workflow.add_conditional_edges(
    "intent_classifier",
    route_intent,
    {
        "admission": "admission_agent",
        "exam": "exam_agent",
        "fees": "fees_agent",
        "scholarship": "scholarship_agent",
        "unknown": "unknown",
    },
)
for agent_name in ("admission_agent", "exam_agent", "fees_agent", "scholarship_agent", "unknown"):
    workflow.add_edge(agent_name, "response_agent")
workflow.add_edge("response_agent", END)

college_assistant_graph = workflow.compile()
