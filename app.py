import gradio as gr
from sentence_transformers import SentenceTransformer
import faiss
import pickle
from llama_cpp import Llama

# Load local LLM
llm = Llama(
    model_path="mistral.gguf",
    n_ctx=2048,
    n_threads=6,
    n_gpu_layers=0
)

# Load vector index and chunks
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("faiss_index.index")
with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# RAG function
def rag_chatbot(query):
    query_vec = model.encode([query])
    D, I = index.search(query_vec, k=4)
    retrieved_docs = [chunks[i] for i in I[0] if i < len(chunks)]

    if not retrieved_docs:
        return "I Don't know"

    context = "\n".join(retrieved_docs)

    prompt = f"""You are a helpful customer support assistant. Answer ONLY using the context provided below.
If the answer is not in the context, say "I Don't know".

Context:
{context}

Question: {query}
Answer:"""

    response = llm(prompt, max_tokens=256, temperature=0.7, stop=["</s>"])
    return response["choices"][0]["text"].strip()

# Gradio interface
iface = gr.Interface(fn=rag_chatbot, inputs="text", outputs="text", title="Angel One Support Bot (Local)")
iface.launch()
