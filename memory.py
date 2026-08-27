import chromadb

client = chromadb.PersistentClient(path="./memory_store")
collection = client.get_or_create_collection("study_memory")

def save_memory(text):
    collection.add(documents=[text], ids=[str(collection.count() + 1)])

def retrieve_memory(query, n_results=3):
    return collection.query(query_texts=[query], n_results=n_results)["documents"][0]
