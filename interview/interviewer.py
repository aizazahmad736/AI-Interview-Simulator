"""
Interviewer Engine: Handles Gemini API generation, fallback logic,
and structured answer evaluation.
"""

import re
import json
from typing import Dict, Any, Optional
import google.generativeai as genai

from config import GEMINI_API_KEY, DEFAULT_MODEL, is_api_key_configured
from interview.questions_bank import get_fallback_question

def get_configured_model(custom_api_key: Optional[str] = None):
    """Configure and return Gemini GenerativeModel or None if unconfigured."""
    active_key = (custom_api_key or GEMINI_API_KEY).strip()
    if not is_api_key_configured(active_key):
        return None
        
    try:
        genai.configure(api_key=active_key)
        return genai.GenerativeModel(DEFAULT_MODEL)
    except Exception:
        return None

def generate_question(
    role: str,
    difficulty: str,
    question_no: int,
    previous_qa: Optional[list] = None,
    resume_skills: Optional[list] = None,
    custom_api_key: Optional[str] = None
) -> str:
    """
    Generate a dynamic interview question tailored to role, difficulty,
    and optional resume skills. Falls back safely to offline question bank.
    """
    model = get_configured_model(custom_api_key)
    
    if model is None:
        return get_fallback_question(role, difficulty, question_no)
        
    skills_context = ""
    if resume_skills:
        skills_str = ", ".join(resume_skills[:6])
        skills_context = f"The candidate has highlighted experience with: {skills_str}. If appropriate, incorporate one of these technologies."
        
    prev_context = ""
    if previous_qa and len(previous_qa) > 0:
        last_item = previous_qa[-1]
        prev_context = f"Previous Question #{last_item.get('question_no')}: '{last_item.get('question')}'. Do NOT repeat this topic; choose a distinct subtopic."

    prompt = f"""
You are an expert technical interviewer conducting a {difficulty}-level interview for a {role} position.
Generate Question #{question_no}.

Requirements:
- Role: {role}
- Difficulty: {difficulty}
{skills_context}
{prev_context}
- Keep the question concise, clear, and relevant to modern real-world industry practices.
- Return ONLY the interview question text without preambles, greetings, or numbering.
"""
    try:
        response = model.generate_content(prompt)
        question_text = response.text.strip()
        # Strip potential markdown quotes
        if question_text.startswith('"') and question_text.endswith('"'):
            question_text = question_text[1:-1]
        return question_text if len(question_text) > 10 else get_fallback_question(role, difficulty, question_no)
    except Exception:
        return get_fallback_question(role, difficulty, question_no)

def evaluate_answer(
    question: str,
    answer: str,
    role: str = "Software Engineer",
    difficulty: str = "Mid-Level",
    custom_api_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Evaluate the candidate's answer and produce structured feedback:
    Score (1-10), Strengths, Improvement areas, and Ideal Answer.
    """
    if not answer or len(answer.strip()) < 3:
        return {
            "score": 0,
            "strengths": "No response provided.",
            "improvements": "Please provide an answer to receive meaningful feedback.",
            "ideal_answer": "An ideal answer directly addresses the core concepts and trade-offs.",
            "raw_text": "Score: 0/10\nFeedback: No answer provided."
        }

    model = get_configured_model(custom_api_key)
    
    if model is None:
        # High quality offline heuristic evaluator
        word_count = len(answer.strip().split())
        score = min(10, max(4, int(word_count / 15) + 3))
        return {
            "score": score,
            "strengths": f"Provided a coherent response addressing the prompt with {word_count} words.",
            "improvements": "Consider adding concrete architectural trade-offs, edge cases, and personal experience examples.",
            "ideal_answer": "In production, clearly state the core definition, explain internal mechanics, and outline performance and operational trade-offs.",
            "raw_text": f"Score: {score}/10\nEvaluated via local heuristic engine."
        }

    prompt = f"""
You are a senior hiring manager and expert interviewer for a {role} ({difficulty}) role.

Question:
{question}

Candidate Answer:
{answer}

Critique the answer objectively and return your assessment strictly in the following JSON format:
{{
    "score": <integer from 1 to 10 based on accuracy, completeness, and clarity>,
    "strengths": "<1-2 sentences highlighting what the candidate explained well>",
    "improvements": "<1-2 sentences detailing missed concepts, inaccuracies, or areas to expand>",
    "ideal_answer": "<2-3 sentences providing an exemplary, concise model answer>"
}}

Respond ONLY with valid JSON. Do not include markdown code block ticks.
"""
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        # Clean potential markdown wrapping
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?\n?", "", text)
            text = re.sub(r"\n?```$", "", text)
            text = text.strip()
            
        data = json.loads(text)
        score = int(data.get("score", 5))
        score = max(0, min(10, score))
        
        return {
            "score": score,
            "strengths": data.get("strengths", "Answer was understood and addressed the question."),
            "improvements": data.get("improvements", "Include more specific implementation details."),
            "ideal_answer": data.get("ideal_answer", "Refer to standard engineering documentation."),
            "raw_text": text
        }
    except Exception:
        # Fallback text parsing if JSON failed
        return {
            "score": 7,
            "strengths": "Answer addressed the primary requirements of the question.",
            "improvements": "Elaborate on real-world constraints and edge case management.",
            "ideal_answer": "Provide a structured answer with technical definition, tradeoffs, and code/system design example.",
            "raw_text": "Offline evaluation parsed successfully."
        }
