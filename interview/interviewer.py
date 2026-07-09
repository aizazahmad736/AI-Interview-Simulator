import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_question(role, difficulty):
    prompt = f"""
Generate ONE {difficulty} interview question for a {role}.

Return ONLY the question.
"""

    response = model.generate_content(prompt)
    return response.text.strip()


def evaluate_answer(question, answer):
    prompt = f"""
You are an expert technical interviewer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return EXACTLY in this format:

Score: X/10

Feedback:
(2-3 lines)

Correct Answer:
(Provide the ideal answer)
"""

    response = model.generate_content(prompt)
    return response.text.strip()