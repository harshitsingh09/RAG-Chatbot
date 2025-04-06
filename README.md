# Angel One Support Bot (RAG Chatbot)

A Retrieval-Augmented Generation (RAG) chatbot built to answer customer support queries using Angel One’s documentation and insurance PDFs.

Powered by FAISS for vector search and a lightweight LLM (TinyLlama) for local inference.

![Chatbot Screenshot](output images\Gradio output (ONLINE).jpg)

---------------------------

FEATURES

- Answers user queries using real support documents  
- Uses FAISS vector store for efficient retrieval  
- Semantic chunk search using SentenceTransformers  
- Local LLM (TinyLlama or Mistral 7B via GGUF or Hugging Face Transformers)  
- Gradio UI for an interactive chatbot interface  
- Handles both general support topics and insurance-related queries  

---------------------------

LIVE DEMO

Try it live: https://huggingface.co/spaces/harshitsingh911/alltius

---------------------------

TECH STACK

Component      - Technology  
UI             - Gradio  
Model          - TinyLlama (transformers pipeline)  
Embeddings     - SentenceTransformers (all-MiniLM-L6-v2)  
Vector Store   - FAISS  
Backend        - Python  

---------------------------

HOW IT WORKS

1. Documents Loading: PDFs (Angel One support docs + insurance info) are loaded and chunked into manageable segments.  
2. Embedding & Indexing: Chunks are converted into dense embeddings and stored using FAISS.  
3. Retrieval: On user query, top relevant chunks are fetched from FAISS using cosine similarity.  
4. Prompt Construction: The selected chunks are added to the query and sent as a prompt to the LLM.  
5. Response Generation: The LLM generates an answer based only on the retrieved documents.  

---------------------------

SAMPLE QUERIES

- What is SIP?  
- How do I reset my trading password?  
- How to buy insurance using Angel One?  
- What are brokerage charges?  

---------------------------

RUN LOCALLY

1. Clone the repo

git clone https://github.com/harshitsingh09/RAG-Chatbot.git 
cd angelone-rag-bot

2. Install dependencies

pip install -r requirements.txt

3. Run the app

python app.py

This will launch the Gradio app at http://127.0.0.1:7860

---------------------------

FILE STRUCTURE

.
├── app.py                  -> Gradio frontend + chatbot logic  
├── requirements.txt        -> Python dependencies  
├── vectorstore.index       -> FAISS index file  
├── metadata.pkl            -> Chunk metadata for retrieval  
├── README.md               -> Project info and guide  

---------------------------

