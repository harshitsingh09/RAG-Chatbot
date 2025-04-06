from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
import faiss
import pickle
import os

docs = []
for file in os.listdir("docs"):
    path = os.path.join("docs", file)
    if file.endswith(".pdf"):
        docs.extend(PyPDFLoader(path).load())
    elif file.endswith(".docx"):
        docs.extend(Docx2txtLoader(path).load())

# Split text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)
texts = [chunk.page_content for chunk in chunks]

# Save chunked texts for retrieval
with open("chunks.pkl", "wb") as f:
    pickle.dump(texts, f)

# Create FAISS index
model = SentenceTransformer("all-MiniLM-L6-v2")
vectors = model.encode(texts, show_progress_bar=True)
index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)
faiss.write_index(index, "faiss_index.index")

print("✅ Index and chunks created!")
