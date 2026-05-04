from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text,chunk_size = 2):
    sentences = text.split(". ")
    chunks = []
    
    for i in range(0,len(sentences),chunk_size):
        chunk = ".".join(sentences[i:i+chunk_size])
        if chunk:
            chunks.append(chunk)
    return chunks

def load_and_process_data(path):
    with open(path,"r") as f:
        text = f.read()
        
        chunks = chunk_text(text)
        embeddings = model.encode(chunks)
        
        return chunks,embeddings



    