"""Streamlit web interface for the College AI Assistant."""

import time

import streamlit as st

from graph import college_assistant_graph


def get_topic_badge_html(topic: str) -> str:
    labels = {
        "admission": "Admission",
        "exam": "Exam",
        "fees": "Fees",
        "scholarship": "Scholarship",
        "unknown": "General",
    }
    label = labels.get(topic, "General")
    return (
        f'<span class="badge" style="display:inline-flex;align-items:center;gap:0.35rem;padding:0.35rem 0.8rem;' \
        f'border-radius:999px;background:#e0f2fe;color:#1d4ed8;font-size:0.82rem;font-weight:700;' \
        f'letter-spacing:0.01em;">{label}</span>'
    )


st.set_page_config(
    page_title="Dumka Engineering College Assistant",
    page_icon="🎓",
    layout="wide",
)

st.markdown(
    """
    <style>
    body {
        color: #0f172a;
        background: linear-gradient(180deg, #f3f6ff 0%, #fbfbff 45%, #fdfbff 100%);
    }
    .stApp {
        background: transparent;
    }
    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 1.2rem;
    }
    .welcome-card {
        border-radius: 30px;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.95);
        border: 1px solid rgba(59, 130, 246, 0.18);
        box-shadow: 0 26px 60px rgba(59, 130, 246, 0.08);
        margin-bottom: 1.4rem;
    }
    .welcome-card h1 {
        margin: 0;
        font-size: 2.4rem;
        letter-spacing: -0.04em;
    }
    .welcome-card p {
        margin: 0.9rem 0 0;
        color: #475569;
        line-height: 1.8;
        font-size: 1rem;
    }
    .sidebar-block {
        border-radius: 24px;
        background: rgba(255, 255, 255, 0.92);
        padding: 1rem 1rem 0.9rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(148, 163, 184, 0.18);
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.05);
    }
    .sidebar-block h3 {
        margin-bottom: 0.8rem;
    }
    .chat-card {
        border-radius: 28px;
        background: rgba(255, 255, 255, 0.96);
        padding: 1.2rem;
        box-shadow: 0 28px 65px rgba(15, 23, 42, 0.08);
    }
    .user-bubble,
    .assistant-bubble {
        border-radius: 20px;
        padding: 1rem 1rem;
        margin-bottom: 0.9rem;
        max-width: 88%;
        line-height: 1.75;
        white-space: pre-wrap;
        font-size: 0.98rem;
    }
    .user-bubble {
        background: #dbeafe;
        color: #0f172a;
        margin-left: auto;
        border-top-right-radius: 6px;
    }
    .assistant-bubble {
        background: #eef2ff;
        color: #1e293b;
        margin-right: auto;
        border-top-left-radius: 6px;
    }
    .typing-indicator {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        color: #475569;
        font-weight: 600;
        margin-bottom: 0.85rem;
    }
    .typing-indicator span {
        width: 0.37rem;
        height: 0.37rem;
        border-radius: 50%;
        background: #1e293b;
        opacity: 0.45;
        animation: pulse 1s infinite ease-in-out;
    }
    .typing-indicator span:nth-child(2) { animation-delay: 0.14s; }
    .typing-indicator span:nth-child(3) { animation-delay: 0.28s; }
    @keyframes pulse {
        0%, 80%, 100% { transform: scale(0.7); opacity: 0.35; }
        40% { transform: scale(1); opacity: 1; }
    }
    .stButton>button {
        border-radius: 16px;
        border: none;
        box-shadow: 0 16px 30px rgba(59, 130, 246, 0.14);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .stButton>button:hover {
        transform: translateY(-1px);
    }
    .stTextInput>div>div>input {
        border-radius: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="welcome-card">
        <h1>🎓 Dumka Engineering College Assistant</h1>
        <p>Ask about admissions, exams, fees, or scholarships and get crisp, college-focused answers instantly.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.recent_topics = []
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": (
                "Welcome to your college assistant! Ask about admissions, exams, fees, or scholarships to get started."
            ),
        }
    )


def render_message(role: str, content: str) -> None:
    class_name = "assistant-bubble" if role == "assistant" else "user-bubble"
    st.markdown(f"<div class='{class_name}'>{content}</div>", unsafe_allow_html=True)


def handle_user_query(query: str) -> None:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        render_message("user", query)

    with st.chat_message("assistant"):
        typing_placeholder = st.empty()
        typing_placeholder.markdown(
            """
            <div class="typing-indicator">
                Processing<span></span><span></span><span></span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for _ in range(3):
            time.sleep(0.35)
        typing_placeholder.empty()

        result = college_assistant_graph.invoke({"user_query": query})
        topic = result.get("intent", "unknown")
        answer = result["final_response"]
        st.markdown(get_topic_badge_html(topic), unsafe_allow_html=True)
        render_message("assistant", answer)

    if topic not in st.session_state.recent_topics:
        st.session_state.recent_topics.insert(0, topic)
        st.session_state.recent_topics = st.session_state.recent_topics[:4]

    st.session_state.messages.append({"role": "assistant", "content": answer})


with st.container():
    st.markdown("<div class='chat-card'>", unsafe_allow_html=True)
    for message in st.session_state.messages:
        render_message(message["role"], message["content"])
    st.markdown("</div>", unsafe_allow_html=True)

if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None

if st.session_state.pending_prompt:
    handle_user_query(st.session_state.pending_prompt)
    st.session_state.pending_prompt = None

if user_query := st.chat_input("Type your question here"):
    handle_user_query(user_query)

with st.sidebar:
    st.markdown("<div class='sidebar-block'>", unsafe_allow_html=True)
    st.markdown("### Quick questions")
    for prompt in [
        "What is the last date for admission?",
        "When are the exams?",
        "What is the annual tuition fee?",
        "How do I apply for a scholarship?",
    ]:
        if st.button(prompt, use_container_width=True):
            st.session_state.pending_prompt = prompt
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='sidebar-block'>", unsafe_allow_html=True)
    st.markdown("### Recent topics")
    if st.session_state.recent_topics:
        for topic in st.session_state.recent_topics:
            st.markdown(f"- {get_topic_badge_html(topic)}", unsafe_allow_html=True)
    else:
        st.caption("Your recent topics will appear here after your first question.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='sidebar-block'>", unsafe_allow_html=True)
    st.markdown("### Supported topics")
    st.markdown("- Admission\n- Exams\n- Fees\n- Scholarships")
    st.caption("Always confirm time-sensitive information with the official college notice or office.")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.pending_prompt = None
        st.session_state.recent_topics = []
