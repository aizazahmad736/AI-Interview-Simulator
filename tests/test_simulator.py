"""
Unit Tests for AI Interview Simulator
Verifies question generation, fallback bank, resume parser, and PDF generator.
"""

import io
import pytest
from interview.questions_bank import get_fallback_question, QUESTION_BANK
from interview.resume_parser import parse_resume_content
from interview.interviewer import evaluate_answer, generate_question
from interview.report_generator import generate_pdf_report

def test_fallback_question_bank():
    """Verify offline question bank returns valid questions for all roles."""
    for role in QUESTION_BANK:
        for diff in ["Junior", "Mid-Level", "Senior"]:
            q = get_fallback_question(role, diff, 1)
            assert isinstance(q, str)
            assert len(q) > 10

def test_resume_parser_skills_detection():
    """Verify resume parser correctly extracts technical skills from text."""
    sample_text = """
    Experienced Python Developer with expertise in FastAPI, Docker, and PostgreSQL.
    Also proficient in React and AWS cloud deployments.
    """
    parsed = parse_resume_content(sample_text)
    assert "Python" in parsed["skills"]
    assert "FastAPI" in parsed["skills"]
    assert "Docker" in parsed["skills"]
    assert parsed["char_count"] > 50

def test_evaluate_answer_empty():
    """Verify evaluate_answer handles empty responses gracefully."""
    res = evaluate_answer("What is GIL?", "")
    assert res["score"] == 0
    assert "No response" in res["strengths"]

def test_evaluate_answer_offline_heuristic():
    """Verify fallback evaluation gives structured scores and text."""
    res = evaluate_answer(
        question="Explain Python decorators.",
        answer="A decorator in Python is a function that takes another function as an argument and extends its behavior without modifying it.",
        custom_api_key=""
    )
    assert 0 <= res["score"] <= 10
    assert "strengths" in res
    assert "improvements" in res
    assert "ideal_answer" in res

def test_generate_pdf_report():
    """Verify PDF generator produces valid PDF bytes."""
    history = [
        {
            "question_no": 1,
            "question": "Explain Python list comprehensions.",
            "answer": "List comprehensions provide a concise way to create lists using brackets.",
            "evaluation": {
                "score": 9,
                "strengths": "Accurate definition.",
                "improvements": "Can mention generator expressions for memory efficiency.",
                "ideal_answer": "List comprehensions provide concise syntax: [expr for item in iterable]."
            }
        }
    ]
    pdf_bytes = generate_pdf_report(
        candidate_name="Test User",
        role="Python Developer",
        difficulty="Mid-Level",
        total_score=9,
        max_score=10,
        qa_history=history
    )
    assert isinstance(pdf_bytes, bytes)
    assert pdf_bytes.startswith(b"%PDF-")
