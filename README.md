# 🧠 Study Buddy — Memory-Based AI Chatbot

A study assistant that remembers what you've learned across sessions and builds on it, instead of re-explaining the basics every time.

🔗 **Live Demo:** _not deployed yet_

---

## ✨ Features
- 💬 Chat with an AI tutor about any topic
- 🧠 Remembers past sessions — memory persists on disk, not just in the browser tab
- 📚 Builds on what you already know instead of repeating fundamentals
- 📝 Auto-summarizes what you learned after each exchange
- 🔍 Semantic search over your learning history using vector embeddings

## 🛠️ Tech Stack
- **Frontend** — Streamlit
- **LLM** — Cohere Command R+
- **Vector store + embeddings** — ChromaDB (default `all-MiniLM-L6-v2`, runs locally)
- **Language** — Python

## 💡 How It Works

Each message you send triggers one pass through this loop:

```
you type
   ↓
embed the question, find the 3 nearest past summaries   memory.py
   ↓
paste them into the system preamble                     app.py
   ↓
Cohere chat(message, preamble, chat_history)            ← call 1: the answer
   ↓
Cohere chat("summarize this exchange")                  ← call 2: the memory
   ↓
store that summary in ChromaDB                          memory.py
```

Two kinds of memory are doing different jobs:

- **Short-term** — `st.session_state.messages`, held in RAM and passed as `chat_history`. Keeps the current conversation coherent. Gone on refresh.
- **Long-term** — the `memory_store/` folder. Survives restarts, and holds *summaries* rather than raw transcripts, so retrieval isn't flooded with "ok" and "thanks".

Embeddings are computed locally by ChromaDB's built-in model — no embedding API calls. The effect is RAG with the corpus pointed at yourself: the store is written by the conversations it later serves.

## 🚀 Run Locally

1. Clone and enter the repo
   ```
   git clone git@github.com:aishwar05/new_ml.git
   cd new_ml
   ```
2. Install dependencies
   ```
   pip install -r requirements.txt
   ```
3. Add your Cohere API key to `.streamlit/secrets.toml`
   ```
   COHERE_API_KEY = "your-key-here"
   ```
4. Run
   ```
   streamlit run app.py
   ```

First launch downloads the embedding model (~80MB). To wipe your history, delete the `memory_store/` folder.

## 📁 Project Structure
```
├── app.py           # Streamlit UI, chat loop, prompt templates
├── memory.py        # ChromaDB read/write
├── requirements.txt # Dependencies
```

## ⚠️ Notes
- Memory is **global**, not per-user — anyone hitting a deployed instance shares one store.
- On Streamlit Cloud the filesystem is ephemeral, so `memory_store/` resets on redeploy. Persistent hosting needs Chroma Cloud or a mounted volume.
