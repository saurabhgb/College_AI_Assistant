# College AI Assistant

A LangGraph-based multi-agent assistant for answering college questions about admissions, exams, fees, and scholarships.

## Features

- LangGraph workflow with intent-based routing across admission, exam, fees, and scholarship agents.
- Verified JSON knowledge sources for Dumka Engineering College, JUT, e-Kalyan, and NSP guidance.
- Official-source note added to every specialist response.
- Streamlit browser interface and terminal interface.
- Optional Gemini fallback for unmatched wording, restricted to the selected agent's JSON data.
- Automated workflow tests with `pytest`.

## Workflow

`START -> Intent Classifier -> Specialist Agent -> Response Agent -> END`

The intent classifier routes each question to one of four data-driven agents. Each agent reads information from the matching JSON file in `data/`.

## Run

```powershell
.\.venv\Scripts\python.exe main.py
```

Type `exit` to close the assistant.

## Web interface

Install the dependencies, then run:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

This opens the chatbot in your browser.

## Example questions

- What is the last date for admission?
- When are the exams?
- What is the annual tuition fee?
- How do I apply for a scholarship?

## Data

The JSON records are configured for **Dumka Engineering College** using its official website and 2026 B.Tech fee document. Details that can change, such as deadlines, timetables, scholarship eligibility, and payment instructions, intentionally direct students to the current official notice or college office.

## Optional Gemini fallback

The assistant uses deterministic routing and JSON data first. To let Gemini handle unmatched wording, copy `.env.example` to `.env`, set your `GOOGLE_API_KEY`, and set `ENABLE_LLM_FALLBACK=true`.

Gemini is given only the selected agent's JSON data and is instructed not to invent college facts. If the Gemini request fails, the assistant continues with its standard data-driven response.

## Tests

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Demo scripts

Manual demonstration scripts are kept in `scripts/` so they do not run as part of the automated test suite.

```powershell
.\.venv\Scripts\python.exe -m scripts.run_admission_demo
```

## License

This project is released under the [MIT License](LICENSE).
