"""Classify a student question before routing it through the workflow."""

from utils.constants import VALID_INTENTS
from utils.llm_helper import classify_with_llm

INTENT_KEYWORDS = {
    "scholarship": ("scholarship", "scholarships", "financial aid", "stipend", "e-kalyan", "ekalyan", "e kalyan", "nsp", "national scholarship"),
    "fees": ("fee", "fees", "tuition", "payment", "refund", "late fee"),
    "exam": ("exam", "exams", "examination", "timetable", "hall ticket", "admit card", "result", "jut", "syllabus", "nep", "new education policy"),
    "admission": ("admission", "admissions", "apply", "application", "eligibility", "documents", "counselling")
}


def classify_intent(user_query: str) -> str:
    """Return the most appropriate supported intent using clear keyword routing."""
    query = user_query.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(keyword in query for keyword in keywords):
            return intent
    return classify_with_llm(user_query) or "unknown"
