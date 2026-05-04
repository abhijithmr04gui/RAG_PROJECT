from transformers import pipeline
print("STARTING MAIN")

generator = pipeline("text-generation", model="google/flan-t5-base")


def generate_answer(query, context):
    prompt = f"""
    You are a helpful assistant.

    Answer the question using ONLY the context below.
    If the answer is present, respond in one short sentence.
    If not, say "I don't know".

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    output = generator(prompt, max_length=100)

    return output[0]["generated_text"]