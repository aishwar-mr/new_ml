import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./memory_store")
collection = client.get_or_create_collection("study_memory")
model = SentenceTransformer("all-MiniLM-L6-v2")

def save_memory(text, metadata={}):
    embedding = model.encode(text).tolist()
    collection.add(
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata],
        ids=[str(collection.count() + 1)]
    )

def retrieve_memory(query, n_results=3):
    embedding = model.encode(query).tolist()
    results = collection.query(
        query_embeddings=[embedding],
        n_results=n_results
    )
    return results["documents"][0] if results["documents"] else []