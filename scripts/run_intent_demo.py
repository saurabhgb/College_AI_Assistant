"""Run sample intent-classification questions from the terminal."""

from agents.intent_classifier import classify_intent


QUERIES = [
    "How can I get admission?",
    "What is the semester fee?",
    "When are exams?",
    "How do I apply for Jharkhand e-Kalyan?",
    "Tell me a joke.",
]


for query in QUERIES:
    print(f"Query: {query}")
    print(f"Intent: {classify_intent(query)}")
    print("-" * 40)
