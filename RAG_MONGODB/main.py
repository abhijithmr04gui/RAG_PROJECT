from app.ingest import load_and_process_data
from app.vector_store import VectorStore
from app.retriever import Retriever
from app.generator import generate_answer

def main():
    print("RAG system started")   # add this for debugging

    chunks, embeddings = load_and_process_data("data/data.txt")

    vector_store = VectorStore(embeddings)
    retriever = Retriever(vector_store, chunks)

    while True:
        query = input("\nAsk a question (or type 'exit'): ")

        if query.lower() == "exit":
            break

        results = retriever.retrieve(query)
        context = "\n".join(results)

        answer = generate_answer(query, context)

        print("\nAnswer:\n", answer)


if __name__ == "__main__":
    main()