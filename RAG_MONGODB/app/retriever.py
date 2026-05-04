from app.model import get_embedding_model

class Retriever:
    def __init__(self,vector_store,chunks):
        self.vector_store = vector_store
        self.chunks = chunks

    def retrieve(self,query,k=2):
        query_embedding = get_embedding_model().encode([query])
        indices = self.vector_store.search(query_embedding,k)

        return [self.chunks[i] for i in indices[0]]
        
        
        