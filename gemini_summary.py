import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

def get_summary(job_description, resume_text):
    prompt = f"""
You're an AI assistant helping a recruiter. Given the following job description and candidate resume,
generate a 3-4 sentence summary of why this candidate is a great fit.

Job Description:
{job_description}

Candidate Resume:
{resume_text}

Summary:
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_interview_questions(job_description, resume_text):
    prompt = f"""
You're a technical recruiter preparing for an interview.

Based on the job description and candidate resume, write 3 personalized, insightful interview questions to assess the candidate's fit.

Job Description:
{job_description}

Resume:
{resume_text}

Questions:
"""
    response = model.generate_content(prompt)
    return [q.strip("- ") for q in response.text.strip().split("\n") if q.strip()]
