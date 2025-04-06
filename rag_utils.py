import os
import pdfplumber
import docx

def load_pdf_text(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def load_docx_text(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_all_documents(folder_path):
    texts = []
    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)
        if filename.endswith(".pdf"):
            texts.append(load_pdf_text(path))
        elif filename.endswith(".docx"):
            texts.append(load_docx_text(path))
    return texts
