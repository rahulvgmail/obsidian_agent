import chromadb
from sentence_transformers import SentenceTransformer

class VectorStoreService:
    def __init__(self, persist_directory):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection("notes")
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')

    def add_documents(self, documents):
        ids = [str(i) for i in range(len(documents))]
        embeddings = self.encoder.encode([doc['content'] for doc in documents]).tolist()
        metadatas = [{'path': doc['path']} for doc in documents]
        self.collection.add(
            embeddings=embeddings,
            documents=[doc['content'] for doc in documents],
            metadatas=metadatas,
            ids=ids
        )

    def query(self, query_text, n_results=5):
        query_embedding = self.encoder.encode([query_text]).tolist()
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        return results
