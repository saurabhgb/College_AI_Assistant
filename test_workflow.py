from app import get_topic_badge_html
from graph import college_assistant_graph


def test_admission_deadline_routes_to_admission_agent():
    result = college_assistant_graph.invoke({"user_query": "What is the last date for admission?"})
    assert result["intent"] == "admission"
    assert "2026-27" in result["final_response"]
    assert "Official admissions" in result["final_response"]


def test_exam_question_routes_to_exam_agent():
    result = college_assistant_graph.invoke({"user_query": "When are the exams?"})
    assert result["intent"] == "exam"
    assert "academic calendar" in result["final_response"].lower()
    assert "official jut b.tech syllabus" in result["final_response"].lower()


def test_unknown_question_returns_help_message():
    result = college_assistant_graph.invoke({"user_query": "Tell me a joke"})
    assert result["intent"] == "unknown"
    assert "admission" in result["final_response"].lower()


def test_response_includes_a_labeled_source_note():
    result = college_assistant_graph.invoke({"user_query": "What is the last date for admission?"})
    assert "Source note:" in result["final_response"]


def test_topic_badge_renders_a_human_readable_label():
    badge = get_topic_badge_html("admission")
    assert "Admission" in badge
    assert "badge" in badge.lower()


def test_ekalyan_question_routes_to_scholarship_agent():
    result = college_assistant_graph.invoke({"user_query": "How do I apply for Jharkhand e-Kalyan?"})
    assert result["intent"] == "scholarship"
    assert "2026-27" in result["final_response"]


def test_jut_syllabus_question_routes_to_exam_agent():
    result = college_assistant_graph.invoke({"user_query": "Where can I find the JUT NEP B.Tech syllabus?"})
    assert result["intent"] == "exam"
    assert "2023-24" in result["final_response"]
