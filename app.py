"""Streamlit web interface for the College AI Assistant."""

import streamlit as st

from graph import college_assistant_graph


st.set_page_config(page_title="Dumka Engineering College Assistant", page_icon="🎓")

st.title("🎓 Dumka Engineering College Assistant")
st.caption("Ask about admissions, exams, fees, or scholarships.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input("Type your question here"):
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Finding information..."):
            result = college_assistant_graph.invoke({"user_query": user_query})
            answer = result["final_response"]
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

if st.sidebar.button("Clear chat"):
    st.session_state.messages = []
    st.rerun()

st.sidebar.markdown("### Supported topics")
st.sidebar.markdown("- Admission\n- Exams\n- Fees\n- Scholarships")
st.sidebar.caption("Always confirm time-sensitive information with the official college notice or office.")
