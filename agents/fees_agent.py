"""Answer fee-related questions from the college data."""

from utils.data_loader import load_json
from utils.llm_helper import answer_from_context
from utils.query_handler import handle_query
from prompts.fees_prompt import FEES_PROMPT

FEES_DATA = load_json("data/fees.json")

KEYWORDS = {
    "payment_deadline": ["deadline", "last date", "due date", "pay by"],
    "payment_methods": ["payment method", "how to pay", "payment options", "pay fees"],
    "late_fee": ["late fee", "late charge", "penalty"],
    "refund_policy": ["refund", "refund policy"],
    "tuition_fee": ["fee", "fees", "tuition", "cost", "amount"]
}


def fees_agent(user_query: str) -> str:
    response = handle_query(user_query, FEES_DATA, KEYWORDS)
    return response or answer_from_context(user_query, FEES_DATA, FEES_PROMPT) or "I can answer questions about tuition fees, payment deadlines, payment methods, late fees, and refunds."
