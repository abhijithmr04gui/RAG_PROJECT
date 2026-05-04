import faiss
import numpy as np

class VectorStore:
    def __init__(self,embedddings):
        self.dimension = embedddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(embedddings)

    def search(self,query,k=2):
        distances,indices = self.index.search(query,k)
        return indices
        