# Angel One Support RAG Chatbot

A locally hosted RAG chatbot that uses customer support docs + insurance PDFs from Angel One to answer queries. Built with:
- `llama-cpp-python` for local LLM
- `FAISS` for vector search
- `Gradio` for web UI

## Setup

```bash
pip install -r requirements.txt
python build_index.py   # Create vector index
python app.py           # Launch Gradio chatbot
```

## Hosted Demo (Huggingface Spaces)

Check it out at: [Demo Link]
