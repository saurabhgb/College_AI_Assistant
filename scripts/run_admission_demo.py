"""Run sample admission questions from the terminal."""

from agents.admission_agent import admission_agent


QUESTIONS = [
    "What documents are required for admission?",
    "What is the eligibility criteria?",
    "Tell me the admission process.",
    "What is the last date for admission?",
]


for question in QUESTIONS:
    print("=" * 60)
    print(f"Question: {question}\n")
    print(admission_agent(question))
    print()
