# 🤖 AI Interview Simulator

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-red?logo=streamlit)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini%20Flash-4285F4?logo=google)](https://ai.google.dev/)
[![CI Test Suite](https://github.com/aizazahmad736/AI-Interview-Simulator/actions/workflows/ci.yml/badge.svg)](https://github.com/aizazahmad736/AI-Interview-Simulator/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent, full-featured **AI Interview Simulator** built with **Streamlit** and **Google Gemini**. Practice real-world technical and behavioral interviews, receive instant AI scoring and critique, personalize questions from your resume, and download comprehensive PDF performance scorecards.

---

## 🌟 Key Features

- 🎯 **Role-Based Dynamic Questions**: Choose from Python Developer, Machine Learning Engineer, Data Analyst, Frontend Developer, Full Stack Developer, or HR & Behavioral.
- 📊 **3 Experience Levels**: Junior, Mid-Level, and Senior difficulty adjustments.
- 📄 **Resume Personalization**: Upload your resume (PDF or TXT) to automatically extract skills and receive tailored questions relevant to your background.
- 🧠 **Structured AI Evaluation**: Every answer receives an objective score (1–10), specific strengths, missed concepts/improvements, and an exemplary ideal answer.
- 🔊 **Voice Speech Integration**: Listen to interview questions read aloud directly in your browser.
- 📥 **Downloadable PDF Scorecards**: Export polished interview summary reports generated with ReportLab.
- 🛡️ **Zero-Crash Offline Mode**: Includes a comprehensive offline question bank and local evaluation heuristics so the app works seamlessly even without an API key.
- 🧪 **Automated CI/CD**: Fully tested with `pytest` and automated via GitHub Actions.

---

## 🏗️ Architecture

```
AI-Interview-Simulator/
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI automated testing
├── app.py                       # Main Streamlit interactive application
├── config.py                    # Environment settings and API key validator
├── requirements.txt             # Clean, pinned dependencies
├── .env.example                 # Template for API credentials
├── .gitignore                   # Ignored files (venv, env, cache, pdfs)
├── README.md                    # Project documentation
├── interview/
│   ├── __init__.py
│   ├── interviewer.py           # Gemini API question generator & grading engine
│   ├── questions_bank.py        # Curated technical & behavioral question bank
│   ├── resume_parser.py         # PDF & text parser for skill extraction
│   └── report_generator.py      # Downloadable PDF report builder (ReportLab)
└── tests/
    ├── __init__.py
    └── test_simulator.py        # Automated test suite
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- (Optional) A free [Google Gemini API Key](https://aistudio.google.com/)

### 2. Installation

```bash
# Clone repository
git clone https://github.com/aizazahmad736/AI-Interview-Simulator.git
cd AI-Interview-Simulator

# Create virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment

Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Add your Gemini API key (or enter it directly inside the app UI):
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run the Application

```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 🧪 Running Unit Tests

Run the test suite with `pytest`:
```bash
pytest tests/ -v
```

---

## 🗺️ Roadmap Status

- [x] Resume upload & parsing to personalize questions
- [x] Multi-question interactive sessions with progress tracking
- [x] AI-scored feedback with strengths, weaknesses, and ideal answers
- [x] Downloadable PDF interview report
- [x] Offline fallback support for zero-crash demonstrations
- [x] Automated CI testing workflow via GitHub Actions

---

## 📄 License
This project is licensed under the MIT License.
