from fastapi import FastAPI

app = FastAPI()

knowledge_base = {
    "sitecore": "Sitecore XM Cloud is a modern SaaS headless CMS platform.",
    "rag": "RAG stands for Retrieval-Augmented Generation."
}

@app.get("/")
def home():
    return {"message": "Enterprise RAG Assistant Running"}

@app.get("/ask")
def ask(question: str):
    question = question.lower()

    for key in knowledge_base:
        if key in question:
            return {
                "question": question,
                "answer": knowledge_base[key]
            }

    return {
        "question": question,
        "answer": "No matching enterprise knowledge found."
    }
