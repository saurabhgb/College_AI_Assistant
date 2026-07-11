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
    return f'<span class="badge" style="display:inline-block;padding:0.2rem 0.55rem;border-radius:999px;background:#dbeafe;color:#1d4ed8;font-size:0.8rem;font-weight:600;">{label}</span>'


st.set_page_config(page_title="Dumka Engineering College Assistant", page_icon="🎓")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f7fbff 0%, #eef6ff 100%);
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }
    div[data-testid="stChatMessage"] {
        border-radius: 12px;
        padding: 0.6rem 0.8rem;
        margin-bottom: 0.5rem;
    }
    .typing-indicator {
        display: inline-flex;
        align-items: center;
        gap: 0.2rem;
        color: #4b5563;
        font-style: italic;
    }
    .typing-indicator span {
        display: inline-block;
        width: 0.35rem;
        height: 0.35rem;
        border-radius: 50%;
        background: #4b5563;
        animation: pulse 1.2s infinite ease-in-out;
    }
    .typing-indicator span:nth-child(2) { animation-delay: 0.2s; }
    .typing-indicator span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes pulse {
        0%, 80%, 100% { transform: scale(0.7); opacity: 0.5; }
        40% { transform: scale(1); opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎓 Dumka Engineering College Assistant")
st.caption("Ask about admissions, exams, fees, or scholarships.")

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.recent_topics = []
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": (
                "Welcome! I can help with admissions, exams, fees, and scholarships. "
                "Try asking: \"What is the last date for admission?\" or \"When are the exams?\""
            ),
        }
    )


def handle_user_query(query: str) -> None:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        typing_placeholder = st.empty()
        typing_placeholder.markdown(
            """
            <div class="typing-indicator">
                Thinking<span></span><span></span><span></span>
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
        st.markdown(answer)

    if topic not in st.session_state.recent_topics:
        st.session_state.recent_topics.insert(0, topic)
        st.session_state.recent_topics = st.session_state.recent_topics[:4]

    st.session_state.messages.append({"role": "assistant", "content": answer})


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None

if st.session_state.pending_prompt:
    handle_user_query(st.session_state.pending_prompt)
    st.session_state.pending_prompt = None


if user_query := st.chat_input("Type your question here"):
    handle_user_query(user_query)


st.sidebar.markdown("### Quick questions")
for prompt in [
    "What is the last date for admission?",
    "When are the exams?",
    "What is the annual tuition fee?",
    "How do I apply for a scholarship?",
]:
    if st.sidebar.button(prompt, use_container_width=True):
        st.session_state.pending_prompt = prompt
        st.rerun()

if st.sidebar.button("Clear chat", use_container_width=True):
    st.session_state.messages = []
    st.session_state.pending_prompt = None
    st.session_state.recent_topics = []
    st.rerun()

st.sidebar.markdown("### Recent topics")
if st.session_state.recent_topics:
    for topic in st.session_state.recent_topics:
        st.sidebar.markdown(f"- {get_topic_badge_html(topic)}", unsafe_allow_html=True)
else:
    st.sidebar.caption("Your recent topics will appear here.")

st.sidebar.markdown("### Supported topics")
st.sidebar.markdown("- Admission\n- Exams\n- Fees\n- Scholarships")
st.sidebar.caption("Always confirm time-sensitive information with the official college notice or office.")
