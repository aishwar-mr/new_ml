import streamlit as st
import cohere
from memory import save_memory, retrieve_memory

client = cohere.Client(st.secrets["COHERE_API_KEY"])

def build_system_prompt(memories):
    memory_text = "\n".join(f"- {m}" for m in memories) if memories else "No past memory yet."

    return f"""You are a helpful study buddy assistant. You help users learn and understand topics deeply.

You have access to the user's past study history:
{memory_text}

Guidelines:
- Reference what the user has already learned when relevant
- Build on past knowledge instead of repeating basics
- Track their understanding and encourage progress
- At the end of each response, summarize what was just learned in one line starting with "📝 Learned:"
- Be encouraging and patient
"""

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
    summary_response = client.chat(
        model="command-r-plus-08-2024",
        message=f"""Summarize the key topics and concepts learned in this conversation in 1-2 sentences.
Be specific about what was understood and any areas of difficulty.

Conversation:
{conversation_text}

Summary:"""
    )
    save_memory(summary_response.text)
