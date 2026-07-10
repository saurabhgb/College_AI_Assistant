# Internship Demo Guide

## Project title

**Dumka Engineering College AI Assistant using LangGraph**

## Problem

Students need quick answers about admissions, examinations, fees, and scholarships. Important information can change, so the application uses curated JSON data and links students back to official notices.

## Architecture

`START -> Intent Classifier -> Specialist Agent -> Response Agent -> END`

- **Intent Classifier:** routes the student question to admission, exam, fees, scholarship, or unknown.
- **Specialist Agents:** retrieve an answer from their own JSON knowledge source.
- **Gemini fallback (optional):** understands unmatched wording but is instructed to use only the selected agent's verified JSON data.
- **Response Agent:** adds an official source note to time-sensitive answers.
- **Streamlit UI:** provides a browser chat interface.

## Demo steps

1. Start the app with `.\.venv\Scripts\python.exe -m streamlit run app.py`.
2. Ask: `What is the last date for admission?`
3. Ask: `What is the first-year B.Tech fee?`
4. Ask: `How do I apply for a scholarship?`
5. Ask an unrelated question to show the unknown-intent route.
6. Open `graph.py` and explain the conditional LangGraph routing.

## Important note

The assistant is configured with official-source guidance, but deadlines, notices, and fees can change. Students should always confirm these details through Dumka Engineering College's official channels.
