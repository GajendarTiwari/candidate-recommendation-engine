import fitz  # PyMuPDF
import docx
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text(file):
    if file.name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return " ".join(page.get_text() for page in doc)
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return " ".join(p.text for p in doc.paragraphs)
    else:
        return file.read().decode("utf-8")

def embed_text(text):
    return model.encode(text)

def calculate_similarity(job_embedding, resume_embeddings):
    return cosine_similarity([job_embedding], resume_embeddings)[0]

