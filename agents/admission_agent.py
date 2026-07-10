"""Answer admission-related questions from the college data."""

from utils.data_loader import load_json
from utils.llm_helper import answer_from_context
from utils.query_handler import handle_query
from prompts.admission_prompt import ADMISSION_PROMPT

ADMISSION_DATA = load_json("data/admission.json")

# Specific questions must come before the broad admission-process keywords.
KEYWORDS = {
    "admission_deadline": ["deadline", "last date", "last day", "closing date", "apply by"],
    "documents_required": ["document", "documents", "certificate", "certificates"],
    "eligibility": ["eligibility", "eligible"],
    "admission_process": ["process", "procedure", "how to apply", "apply for admission"]
}


def admission_agent(user_query: str) -> str:
    response = handle_query(user_query, ADMISSION_DATA, KEYWORDS)
    if response:
        return response

    return answer_from_context(user_query, ADMISSION_DATA, ADMISSION_PROMPT) or (
        "I can answer questions about:\n"
        "- Admission process\n"
        "- Eligibility\n"
        "- Required documents\n"
        "- Admission deadline"
    )
