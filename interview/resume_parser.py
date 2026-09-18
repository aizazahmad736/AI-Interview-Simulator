"""
Resume Parser for extracting candidate skills, experience, and project context.
Supports PDF (via pypdf) and plain text (.txt).
"""

import io
import re
from typing import Dict, List, Any

# Common high-value technical keywords for detection
TECH_KEYWORDS = [
    "Python", "JavaScript", "TypeScript", "React", "Next.js", "Vue", "Angular",
    "Node.js", "Express", "FastAPI", "Flask", "Django", "SQL", "PostgreSQL",
    "MySQL", "MongoDB", "Redis", "Docker", "Kubernetes", "AWS", "Azure", "GCP",
    "Git", "CI/CD", "Linux", "Machine Learning", "Deep Learning", "PyTorch",
    "TensorFlow", "Scikit-Learn", "Pandas", "NumPy", "NLP", "Computer Vision",
    "LLM", "RAG", "LangChain", "REST API", "GraphQL", "Tailwind CSS", "HTML5",
    "CSS3", "C++", "Java", "Go", "Rust", "Streamlit"
]

def extract_text_from_file(uploaded_file) -> str:
    """Extract raw text from an uploaded file (PDF or TXT)."""
    if uploaded_file is None:
        return ""
    
    filename = uploaded_file.name.lower()
    
    # Text file
    if filename.endswith(".txt"):
        try:
            return uploaded_file.read().decode("utf-8", errors="ignore")
        except Exception:
            return ""
            
    # PDF file
    if filename.endswith(".pdf"):
        try:
            try:
                from pypdf import PdfReader
            except ImportError:
                from PyPDF2 import PdfReader
            pdf_bytes = io.BytesIO(uploaded_file.read())
            reader = PdfReader(pdf_bytes)
            text_chunks = []
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text_chunks.append(extracted)
            return "\n".join(text_chunks)
        except Exception as e:
            return f"Error extracting PDF text: {str(e)}"
            
    return ""

def parse_resume_content(text: str) -> Dict[str, Any]:
    """Parse resume text to extract skills and contextual summary."""
    if not text or len(text.strip()) < 20:
        return {"skills": [], "summary": "", "char_count": 0}
        
    found_skills = []
    text_lower = text.lower()
    
    for kw in TECH_KEYWORDS:
        pattern = r"\b" + re.escape(kw.lower()) + r"\b"
        if re.search(pattern, text_lower):
            found_skills.append(kw)
            
    # Clean and summarize key preview lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    preview_lines = lines[:12]
    summary = " ".join(preview_lines)[:350]
    
    return {
        "skills": found_skills,
        "summary": summary,
        "char_count": len(text),
        "total_skills_detected": len(found_skills)
    }
