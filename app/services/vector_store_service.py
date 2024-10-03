import chromadb
from sentence_transformers import SentenceTransformer

class VectorStoreService:
    def __init__(self, persist_directory):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection("notes")
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')

    def add_documents(self, documents):
        ids = [doc['path'] for doc in documents]
        embeddings = self.encoder.encode([doc['content'] for doc in documents]).tolist()
        metadatas = [{'path': doc['path']} for doc in documents]
        self.collection.add(
            embeddings=embeddings,
            documents=[doc['content'] for doc in documents],
            metadatas=metadatas,
            ids=ids
        )

    def update_document(self, document):
        id = document['path']
        embedding = self.encoder.encode([document['content']]).tolist()[0]
        metadata = {'path': document['path']}
        self.collection.update(
            embeddings=[embedding],
            documents=[document['content']],
            metadatas=[metadata],
            ids=[id]
        )

    def query(self, query_text, n_results=5):
        query_embedding = self.encoder.encode([query_text]).tolist()
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        return results

    def batch_add_or_update_documents(self, documents, batch_size=100):
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i+batch_size]
            ids = [doc['path'] for doc in batch]
            embeddings = self.encoder.encode([doc['content'] for doc in batch]).tolist()
            metadatas = [{'path': doc['path']} for doc in batch]
            self.collection.upsert(
                embeddings=embeddings,
                documents=[doc['content'] for doc in batch],
                metadatas=metadatas,
                ids=ids
            )
