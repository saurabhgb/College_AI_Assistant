"""Answer scholarship-related questions from the college data."""

from utils.data_loader import load_json
from utils.llm_helper import answer_from_context
from utils.query_handler import handle_query
from prompts.scholarship_prompt import SCHOLARSHIP_PROMPT

SCHOLARSHIP_DATA = load_json("data/scholarship.json")

KEYWORDS = {
    "jharkhand_ekalyan": ["e-kalyan", "ekalyan", "e kalyan", "jharkhand scholarship"],
    "nsp_scholarship": ["nsp", "national scholarship portal", "national scholarship"],
    "application_deadline": ["deadline", "last date", "closing date", "apply by"],
    "required_documents": ["document", "documents", "certificate", "proof"],
    "application_process": ["how to apply", "application process", "apply", "procedure"],
    "eligibility": ["eligibility", "eligible", "qualify"],
    "available_scholarships": ["scholarship", "scholarships", "financial aid"]
}


def scholarship_agent(user_query: str) -> str:
    response = handle_query(user_query, SCHOLARSHIP_DATA, KEYWORDS)
    return response or answer_from_context(user_query, SCHOLARSHIP_DATA, SCHOLARSHIP_PROMPT) or "I can answer questions about scholarships, eligibility, applications, deadlines, and documents."
