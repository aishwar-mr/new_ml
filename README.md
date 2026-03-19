# 🧠 Study Buddy — Memory-Based AI Chatbot

A smart study assistant that remembers what you've learned across sessions and builds on your knowledge over time.

🔗 **Live Demo:** [Click here](https://your-streamlit-url-here)

---

## ✨ Features
- 💬 Chat with an AI tutor about any topic
- 🧠 Remembers past conversations across sessions
- 📚 Builds on what you already know instead of repeating basics
- 📝 Auto-summarizes what you learned after each chat
- 🔍 Semantic memory search using vector embeddings

## 🛠️ Tech Stack
- **Frontend** — Streamlit
- **LLM** — Cohere Command R
- **Vector Database** — ChromaDB
- **Embeddings** — Sentence Transformers (all-MiniLM-L6-v2)
- **Language** — Python

## 🚀 How to Run Locally
1. Clone the repo
```
   git clone git@github.com:aishwar05/your-repo-name.git
```
2. Install dependencies
```
   pip install -r requirements.txt
```
3. Add your Cohere API key in `.streamlit/secrets.toml`
```
   COHERE_API_KEY = "your-key-here"
```
4. Run the app
```
   streamlit run app.py
```

## 💡 How It Works
- Every conversation is converted into vector embeddings and stored in ChromaDB
- Before each reply, relevant past memories are retrieved using semantic search
- Retrieved memories are injected into the system prompt so the AI remembers you
- Similar concept to RAG (Retrieval Augmented Generation) but applied to personal learning memory

## 📁 Project Structure
```
├── app.py           # Main Streamlit app
├── memory.py        # ChromaDB read/write logic
├── prompts.py       # System prompt templates
├── requirements.txt # Dependencies
```
```

Replace `your-streamlit-url-here` with your actual Streamlit URL. Hit **Ctrl + S**, then push to GitHub:
```
git add .
git commit -m "add README"
git push