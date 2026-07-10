"""Answer examination-related questions from the college data."""

from utils.data_loader import load_json
from utils.llm_helper import answer_from_context
from utils.query_handler import handle_query
from prompts.exam_prompt import EXAM_PROMPT

EXAM_DATA = load_json("data/exam.json")

KEYWORDS = {
    "nep_syllabus": ["new education policy", "nep", "syllabus"],
    "exam_authority": ["jut ranchi", "jut", "exam authority", "who conducts exams"],
    "hall_ticket": ["hall ticket", "admit card"],
    "timetable_release": ["timetable", "time table", "schedule released"],
    "exam_results": ["result", "results", "marks"],
    "exam_guidelines": ["guideline", "rules", "exam hall", "instructions"],
    "exam_schedule": ["exam date", "exams", "exam", "examination"]
}


def exam_agent(user_query: str) -> str:
    response = handle_query(user_query, EXAM_DATA, KEYWORDS)
    return response or answer_from_context(user_query, EXAM_DATA, EXAM_PROMPT) or "I can answer questions about exam dates, timetables, hall tickets, results, and guidelines."
