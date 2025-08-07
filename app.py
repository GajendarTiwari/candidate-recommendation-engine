import streamlit as st
import os
from gemini_summary import get_summary, generate_interview_questions
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from dotenv import load_dotenv
from utils import extract_text  # Import the extract_text function

load_dotenv()

# Load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")  # Updated path for deployment

st.set_page_config(page_title="Candidate Recommendation Engine", page_icon="📄", layout="centered")
st.title("🔍 Candidate Recommendation Engine")
st.markdown("Upload a job description and candidate resumes to find the best matches.")

# Input job description
job_desc = st.text_area("📋 Paste the Job Description", height=200)

# Upload resume files - Updated to accept multiple formats
uploaded_files = st.file_uploader(
    "📎 Upload Candidate Resumes (.txt, .pdf, .docx)", 
    type=["txt", "pdf", "docx"], 
    accept_multiple_files=True
)

# Process and display results
if st.button("🚀 Recommend Candidates") and job_desc and uploaded_files:
    with st.spinner("Processing resumes and generating recommendations..."):
        resumes = []
        for file in uploaded_files:
            # Use the extract_text function to handle multiple formats
            content = extract_text(file)
            resumes.append({"name": file.name, "text": content})

        # Vectorization
        texts = [job_desc] + [r["text"] for r in resumes]
        vectorizer = TfidfVectorizer().fit_transform(texts)
        job_vector = vectorizer[0]
        resume_vectors = vectorizer[1:]

        # Compute cosine similarity
        similarities = cosine_similarity(job_vector, resume_vectors).flatten()

        # Rank resumes by similarity
        top_indices = similarities.argsort()[::-1]
        top_resumes = [resumes[i] for i in top_indices]

        # Display top 5 results
        st.subheader("🏆 Top Candidates:")
        for i, idx in enumerate(top_indices[:5]):
            candidate = resumes[idx]
            score = similarities[idx]

            summary = get_summary(job_desc, candidate["text"])
            questions = generate_interview_questions(job_desc, candidate["text"])

            st.markdown(f"### 🧑 Candidate {i+1}: `{candidate['name']}`")
            st.write(f"**Similarity Score:** `{score:.2f}`")
            st.markdown(f"**Summary:** {summary}")
            st.markdown("**Interview Questions:**")
            for q in questions:
                st.markdown(f"- {q}")
            st.markdown("---")
