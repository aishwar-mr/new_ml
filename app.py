import streamlit as st
import cohere
from memory import save_memory, retrieve_memory
from prompts import build_system_prompt, build_memory_summary

client = cohere.Client(st.secrets["COHERE_API_KEY"])

st.set_page_config(page_title="Study Buddy", page_icon="🧠")
st.title("🧠 Study Buddy")
st.caption("I remember everything you've learned!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    relevant_memories = retrieve_memory(prompt)
    system_prompt = build_system_prompt(relevant_memories)

    history = [
        {"role": "USER" if m["role"] == "user" else "CHATBOT", "message": m["content"]}
        for m in st.session_state.messages[:-1]
    ]

    response = client.chat(
        model="command-r-plus-08-2024",
        message=prompt,
        preamble=system_prompt,
        chat_history=history
    )
    reply = response.text

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    conversation_text = f"User: {prompt}\nAssistant: {reply}"
    summary_prompt = build_memory_summary(conversation_text)
    summary_response = client.chat(
        model="command-r-plus-08-2024",
        message=summary_prompt
    )
    save_memory(summary_response.text, metadata={"topic": prompt[:50]})